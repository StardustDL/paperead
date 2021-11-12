<script setup lang="ts">
import DPlayer, { DPlayerDanmaku } from 'dplayer'
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { Document } from '../../../models'
import { ExternalLink } from '@vicons/tabler'
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NCollapse, NCollapseItem, NButton, NIcon } from 'naive-ui'
import { parse, Media } from '../media'
import Resource from '../../../components/Resource.vue'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const container = ref<HTMLDivElement>();

const media = ref<Media[]>([]);

const currentIndex = ref(0);

const player = ref<DPlayer>();

function loadVideo(play: boolean = false) {
  if (media.value.length == 0)
    return;

  if (currentIndex.value >= media.value.length) {
    currentIndex.value = media.value.length - 1;
  }

  let current = media.value[currentIndex.value];

  player.value?.switchVideo({
    url: current.url,
    pic: current.cover,
  }, undefined as unknown as DPlayerDanmaku);

  if (play) {
    player.value?.play();
  }
}

function onClickItem(names: string[]) {
  if (names.length == 0)
    return;
  currentIndex.value = parseInt(names[0]);
  loadVideo();
}

onMounted(() => {
  player.value = new DPlayer({
    container: container.value!,
    screenshot: true,
    video: {
      url: ""
    },
  });
  media.value = parse(props.data);
  loadVideo();
});
onBeforeUnmount(() => {
  if (player.value != null)
    player.value.destroy();
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
  <Resource :css="['/static/css/github-markdown.min.css']"></Resource>
  <n-layout has-sider sider-placement="right" style="height: 100%;">
    <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="height: 100%;">
      <div ref="container"></div>
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
            <article v-html="item.renderedDescription" class="markdown-body" style="background-color: inherit;"></article>
          </n-collapse-item>
        </n-collapse>
      </n-layout-content>
    </n-layout-sider>
  </n-layout>
</template>