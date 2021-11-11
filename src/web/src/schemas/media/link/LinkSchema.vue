<script setup lang="ts">
import DPlayer, { DPlayerDanmaku, DPlayerEvents } from 'dplayer'
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { isRelativeUrl } from '../../../helpers'
import { Document } from '../../../models'
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NCollapse, NCollapseItem, NButton, NIcon } from 'naive-ui'
import { ExternalLink } from '@vicons/tabler'
import { parse, Media } from '../media'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const media = ref<Media[]>([]);

const currentIndex = ref(0);

function onClickItem(names: string[]) {
  if (names.length == 0)
    return;
  currentIndex.value = parseInt(names[0]);
}

onMounted(() => {
  media.value = parse(props.data);
});
</script>

<script lang="ts">
export default {
    components: {
        ExternalLink,
    }
}
</script>

<template>
  <n-layout has-sider sider-placement="right" style="height: 100%;">
    <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="height: 100%;">
      <iframe height="100%" width="100%" v-if="currentIndex < media.length" :src="media[currentIndex].url" style="border:0;"></iframe>
    </n-layout-content>
    <n-layout-sider
      style="height: 100%;"
      collapse-mode="width"
      :collapsed-width="0"
      :width="200"
      show-trigger="bar"
      :default-collapsed="true"
      :show-collapsed-content="false"
    >
      <n-layout-content
        style="height: 100%;"
        :native-scrollbar="false"
        content-style="padding: 10px;"
      >
        <n-collapse
          :accordion="true"
          arrow-placement="right"
          :expanded-names="currentIndex.toString()"
          @update-expanded-names="onClickItem"
        >
          <n-collapse-item
            v-for="(item, index) in media"
            :title="item.title"
            :name="index.toString()"
          >
            <template #header-extra>
              <n-button :bordered="false" size="large" :href="item.url" tag="a" target="_blank">
                <template #icon>
                  <n-icon>
                    <external-link />
                  </n-icon>
                </template>
              </n-button>
            </template>
            <div v-html="item.renderedDescription"></div>
          </n-collapse-item>
        </n-collapse>
      </n-layout-content>
    </n-layout-sider>
  </n-layout>
</template>