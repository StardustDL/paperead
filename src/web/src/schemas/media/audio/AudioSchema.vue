<script setup lang="ts">
// @ts-ignore
import APlayer from 'aplayer'
import { ref, onMounted, onBeforeUnmount, computed } from 'vue'
import { isRelativeUrl } from '../../../helpers'
import { Document } from '../../../models'
import { ExternalLink } from '@vicons/tabler'
import { useOsTheme, NLayout, NLayoutContent, NImage, NButton, NIcon, NSpace, NThing, NAvatar } from 'naive-ui'
import { parse, Media } from '../media'
import Resource from '../../../components/Resource.vue'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const container = ref<HTMLDivElement>();

const media = ref<Media[]>([]);

const currentIndex = ref(0);

const current = computed(() => {
  if (currentIndex.value < media.value.length) {
    return media.value[currentIndex.value];
  }
  return undefined;
})

const player = ref<APlayer>();

onMounted(() => {
  media.value = parse(props.data);

  let audios = [];

  for (let item of media.value) {
    audios.push({
      name: item.title,
      url: item.url,
      lrc: item.lrc,
      cover: item.cover,
      artist: item.author,
    })
  }

  player.value = new APlayer({
    container: container.value!,
    audio: audios,
    lrcType: 3,
  });

  player.value.on("listswitch", (item: { index: number }) => {
    currentIndex.value = item.index;
  });
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
  <Resource :css="['https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.0.0/github-markdown.min.css']"></Resource>
  <Resource :css="['https://cdnjs.cloudflare.com/ajax/libs/aplayer/1.10.1/APlayer.min.css']"></Resource>
  <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="height: 100%;">
    <n-space vertical style="padding: 10px;">
      <div ref="container"></div>
      <n-thing v-if="current" style="padding: 10px;">
        <template #avatar>
          <n-avatar size="large" :src="current.cover"></n-avatar>
        </template>
        <template #header>{{ current.title }}</template>
        <template #header-extra>
          <n-button :bordered="false" size="large" :href="current.url" tag="a" target="_blank">
            <template #icon>
              <n-icon>
                <external-link />
              </n-icon>
            </template>
          </n-button>
        </template>
        <article v-html="current.renderedDescription" class="markdown-body" style="background-color: inherit;"></article>
      </n-thing>
    </n-space>
  </n-layout-content>
</template>