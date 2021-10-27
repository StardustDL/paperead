<script setup lang="ts">
import { Document } from '../../models'
import { useOsTheme } from 'naive-ui';
import { onMounted, watch, ref, onUnmounted } from 'vue';
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

const props = defineProps<{
  data: Document,
}>();

const osThemeRef = useOsTheme();

const element = ref<HTMLDivElement>();

const themeLink = ref<HTMLLinkElement>();
const highlightLink = ref<HTMLLinkElement>();

function render() {

}

function resetTheme() {
  let head = document.getElementsByTagName("head")[0];
  if (themeLink.value != null)
    head.removeChild(themeLink.value);
  if (highlightLink.value != null)
    head.removeChild(highlightLink.value);
}

function applyTheme() {
  let head = document.getElementsByTagName("head")[0];

  let themelk = document.createElement("link");
  themelk.type = "text/css";
  themelk.rel = "stylesheet";
  let highlightlk = document.createElement("link");
  highlightlk.type = "text/css";
  highlightlk.rel = "stylesheet";

  themelk.href = "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/white.min.css";
  highlightlk.href = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/github.min.css";

  if (osThemeRef.value == "dark") {
    themelk.href = "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.1.2/theme/black.min.css";
    highlightlk.href = "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.3.1/styles/monokai.min.css";
  }

  head.appendChild(themelk);
  head.appendChild(highlightlk);

  themeLink.value = themelk;
  highlightLink.value = highlightlk;
}

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
  });
  deck.initialize();
  applyTheme();
});

onUnmounted(resetTheme);
watch(osThemeRef, () => {
  resetTheme();
  applyTheme();
})
</script>

<template>
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