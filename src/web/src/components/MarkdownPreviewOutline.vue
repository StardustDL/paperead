<script setup lang="ts">
import { onMounted, ref, computed, watch, h } from 'vue'
import { useStore } from '../services/store'
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NAnchor, NAnchorLink } from 'naive-ui'
import Vditor from 'vditor';
import MarkdownPreviewOutlineItem from './MarkdownPreviewOutlineItem.vue';
import { AnchorItem } from './AnchorItem'
import "vditor/dist/index.css";

const osThemeRef = useOsTheme();

const props = defineProps<{
    element?: HTMLElement,
}>();

const target = computed(()=>props.element);

const result = ref<AnchorItem[]>();

function buildAnchorItem(element: HTMLLIElement) {
    let span = element.children[0] as HTMLSpanElement;

    let title = span.getAttribute("data-target-id") ?? "";

    let result = new AnchorItem(title, `#${title}`);

    if (element.children.length > 1) {
        let ul = element.children[1] as HTMLUListElement;

        for (let i = 0; i < ul.children.length; i++) {
            // console.log(ul.children[i]);
            result.children.push(buildAnchorItem(ul.children[i] as HTMLLIElement))
        }
    }

    return result;
}

async function renderOutline() {
    if (props.element == undefined)
        return;

    let temp = document.createElement("div");

    Vditor.outlineRender(props.element!, temp);

    if (temp.children.length == 0) {
        result.value = [];
        return;
    }

    let ul = temp.children[0] as HTMLUListElement;

    let anchors = [];

    for (let i = 0; i < ul.children.length; i++) {
        anchors.push(buildAnchorItem(ul.children[i] as HTMLLIElement));
    }

    result.value = anchors;
}

onMounted(renderOutline);
watch(props, renderOutline);

defineExpose({
    renderOutline,
});
</script>


<template>
    <n-anchor :offset-target="element" :show-rail="false">
        <MarkdownPreviewOutlineItem v-for="item in result" :key="item.href" :value="item" />
    </n-anchor>
</template>