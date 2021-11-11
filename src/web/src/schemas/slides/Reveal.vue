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
  "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/white.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/github.min.css"
];
const darkTheme = [
  "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/black.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/monokai.min.css"
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