<script setup lang="ts">

// @ts-ignore
import DPlayer from 'dplayer'
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { isRelativeUrl } from '../../../helpers'
import { Document } from '../../../models'
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NCollapse, NCollapseItem } from 'naive-ui'
import { parse, Media } from '../media'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const container = ref<HTMLDivElement>();

const media = ref<Media[]>([]);

const currentIndex = ref(0);

const dplayer = ref<DPlayer>();

function loadVideo() {
  if (media.value.length == 0)
    return;

  if (currentIndex.value >= media.value.length) {
    currentIndex.value = media.value.length - 1;
  }

  let current = media.value[currentIndex.value];

  dplayer.value.switchVideo({
    url: current.url
  });
}

function onClickVideo(names: string[]) {
  if (names.length == 0)
    return;
  currentIndex.value = parseInt(names[0]);
}

onMounted(() => {
  dplayer.value = new DPlayer({
    container: container.value,
    video: {}
  });
  media.value = parse(props.data);
});
watch(media, loadVideo);
watch(currentIndex, loadVideo);
onBeforeUnmount(() => {
  if (dplayer.value != null)
    dplayer.value.destroy();
})
</script>

<template>
  <n-layout has-sider sider-placement="right" style="height: 100%;" :native-scrollbar="false">
    <n-layout-content style="height: 100%;" :native-scrollbar="false">
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
          @update-expanded-names="onClickVideo"
        >
          <n-collapse-item
            v-for="(item, index) in media"
            :title="item.title"
            :name="index.toString()"
          >
            <div v-html="item.renderedDescription"></div>
          </n-collapse-item>
        </n-collapse>
      </n-layout-content>
    </n-layout-sider>
  </n-layout>
</template>