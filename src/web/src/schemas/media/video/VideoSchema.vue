<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount, computed } from 'vue'
import Artplayer from 'artplayer'
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

const player = ref<Artplayer>();

const options = computed(() => {
  if (media.value.length == 0)
    return;

  if (currentIndex.value >= media.value.length) {
    currentIndex.value = media.value.length - 1;
  }
  let current = media.value[currentIndex.value];
  return {
    url: current.url,
    poster: current.cover,
    title: current.title,
    subtitle: {
      url: current.subtitle,
      encoding: 'utf-8',
      bilingual: true,
    },
    thumbnails: {
      url: current.thumbnails,
      number: 100,
      width: 160,
      height: 90,
      column: 10,
    },
  };
})

function loadVideo() {
  if (media.value.length == 0)
    return;

  if (currentIndex.value >= media.value.length) {
    currentIndex.value = media.value.length - 1;
  }

  if (player.value != undefined) {
    // @ts-ignore
    player.value.destroy();
    player.value = undefined;
  }

  // @ts-ignore
  player.value = new Artplayer({
    container: container.value!,
    pip: true,
    autoMini: true,
    screenshot: true,
    setting: true,
    loop: true,
    flip: true,
    rotate: true,
    playbackRate: true,
    aspectRatio: true,
    fullscreen: true,
    fullscreenWeb: true,
    subtitleOffset: true,
    miniProgressBar: true,
    localVideo: true,
    localSubtitle: true,
    networkMonitor: false,
    mutex: true,
    light: true,
    backdrop: true,
    log: true,
    theme: '#ffad00',
    // @ts-ignore
    lang: navigator.language.toLowerCase(),
    ...options.value
  });
}

function onClickItem(names: string[]) {
  if (names.length == 0)
    return;
  currentIndex.value = parseInt(names[0]);
  loadVideo();
}

onMounted(() => {
  media.value = parse(props.data);
  loadVideo();
});
onBeforeUnmount(() => {
  if (player.value != undefined)
    // @ts-ignore
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
      <div ref="container" style="height: 100%;"></div>
    </n-layout-content>
    <n-layout-sider
      style="height: 100%; z-index: 100;"
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
            <article
              v-html="item.renderedDescription"
              class="markdown-body"
              style="background-color: inherit;"
            ></article>
          </n-collapse-item>
        </n-collapse>
      </n-layout-content>
    </n-layout-sider>
  </n-layout>
</template>