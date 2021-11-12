<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { Document } from '../../../models'
import { ExternalLink } from '@vicons/tabler'
import { useOsTheme, NLayoutContent, NImage, NCard, NSpace, NButton, NIcon, NBackTop } from 'naive-ui'
import { parse, Media } from '../media'
import Resource from '../../../components/Resource.vue'

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();

const images = ref<Media[]>([]);

onMounted(() => {
  images.value = parse(props.data);
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
        <article
          v-html="item.renderedDescription"
          class="markdown-body"
          style="background-color: inherit;"
        ></article>
      </n-card>
    </n-space>
    <n-back-top right="100"></n-back-top>
  </n-layout-content>
</template>