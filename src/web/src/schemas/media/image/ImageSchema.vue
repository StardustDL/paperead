<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { isRelativeUrl } from '../../../helpers'
import { Document } from '../../../models'
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NCollapse, NCollapseItem, NCarousel, NImage, NCard, NSpace } from 'naive-ui'
import { parse, Media } from '../media'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const container = ref<HTMLDivElement>();

const images = ref<Media[]>([]);

const current = ref<Media>();

const currentIndex = ref(0);

function loadVideo() {
  if (images.value.length == 0) {
    current.value = undefined;
    return;
  }

  if (currentIndex.value >= images.value.length) {
    currentIndex.value = images.value.length - 1;
  }

  current.value = images.value[currentIndex.value];
}

function onClickVideo(names: string[]) {
  if (names.length == 0)
    return;
  currentIndex.value = parseInt(names[0]);
}

onMounted(() => {
  images.value = parse(props.data);
});
watch(images, loadVideo);
watch(currentIndex, loadVideo);
</script>

<template>
  <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="padding: 20px;">
    <n-space style="justify-content: center;">
      <n-card
        hoverable
        embedded
        :title="item.title"
        v-for="(item, index) in images"
        :key="index"
        style="max-width: 300px;"
      >
        <template #cover>
          <n-image object-fit="cover" :alt="item.title" :src="item.url"></n-image>
        </template>
        <div v-html="item.renderedDescription"></div>
      </n-card>
    </n-space>
  </n-layout-content>
</template>