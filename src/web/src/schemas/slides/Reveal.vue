<script setup lang="ts">
import { Document } from '../../models'
import { useOsTheme } from 'naive-ui';
import { onMounted, watch, ref } from 'vue';
// @ts-ignore
import Reveal from 'reveal.js'
// @ts-ignore
import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js';
// @ts-ignore
import Math from 'reveal.js/plugin/math/math.esm.js';
// @ts-ignore
import Search from 'reveal.js/plugin/search/search.esm.js';
// @ts-ignore
import Notes from 'reveal.js/plugin/notes/notes.esm.js';
// @ts-ignore
import Zoom from 'reveal.js/plugin/zoom/zoom.esm.js';
// @ts-ignore
import Highlight from 'reveal.js/plugin/highlight/highlight.esm.js';
import 'reveal.js/dist/reveal.css'
import Resource from '../../components/Resource.vue';

const props = defineProps<{
  data: Document,
}>();

const osThemeRef = useOsTheme();

const element = ref<HTMLDivElement>();

const whiteTheme = [
  "/static/css/reveal-white.min.css",
  "/static/css/highlight-white.min.css",
];
const darkTheme = [
  "/static/css/reveal-black.min.css",
  "/static/css/highlight-black.min.css",
];

onMounted(() => {
  const deck = new Reveal({
    plugins: [Markdown, Math, Highlight, Zoom, Notes, Search],
    center: false,
    markdown: {
      baseUrl: props.data.dataUrl,
      smartLists: true,
      smartypants: true,
    },
    slideNumber: "c/t",
    hash: true,
    embedded: true,
    transitionSpeed: "fast",
  });
  deck.initialize();
});
</script>

<template>
  <Resource :css="(osThemeRef == 'dark' ? darkTheme : whiteTheme)"></Resource>
  <div class="reveal" ref="element">
    <div class="slides">
      <section
        data-markdown
        data-separator="^\r?\n===\r?\n$"
        data-separator-vertical="^\r?\n---\r?\n$"
        data-separator-notes="notes?:"
      >
        <textarea data-template>{{ data.content }}</textarea>
      </section>
    </div>
  </div>
</template>