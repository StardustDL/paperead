<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import { Document } from '../../../models'
import { ExternalLink } from '@vicons/tabler'
import { useOsTheme, NLayoutContent, NImage, NCard, NSpace, NButton, NIcon } from 'naive-ui'
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


<script lang="ts">
export default {
  components: {
    ExternalLink,
  }
}
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
      </n-card>
    </n-space>
  </n-layout-content>
</template>