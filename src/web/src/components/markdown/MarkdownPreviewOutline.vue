<script setup lang="ts">
import { onMounted, ref, watch} from 'vue'
import { NAnchor } from 'naive-ui'
import Vditor from 'vditor'
import MarkdownPreviewOutlineItem from './MarkdownPreviewOutlineItem.vue'
import { AnchorItem } from '../AnchorItem'

const props = defineProps<{
    element?: HTMLElement,
}>();

const result = ref<AnchorItem[]>();

function buildAnchorItem(element: HTMLLIElement) {
    let span = element.children[0] as HTMLSpanElement;

    let id = span.getAttribute("data-target-id") ?? "";

    let title = document.getElementById(id)?.innerText ?? id;

    let result = new AnchorItem(title, `#${id}`);

    if (element.children.length > 1) {
        let ul = element.children[1] as HTMLUListElement;

        for (let i = 0; i < ul.children.length; i++) {
            result.children.push(buildAnchorItem(ul.children[i] as HTMLLIElement))
        }
    }

    return result;
}

async function renderOutline() {
    if (props.element == undefined)
        return false;

    let temp = document.createElement("div");

    Vditor.outlineRender(props.element!, temp);

    if (temp.children.length == 0) {
        result.value = [];
        return false;
    }

    let ul = temp.children[0] as HTMLUListElement;

    let anchors = [];

    for (let i = 0; i < ul.children.length; i++) {
        anchors.push(buildAnchorItem(ul.children[i] as HTMLLIElement));
    }

    result.value = anchors;

    return true;
}

onMounted(renderOutline);
watch(props, renderOutline);

defineExpose({
    renderOutline,
});
</script>


<template>
    <n-anchor type="block" :listen-to="element" :ignore-gap="true">
        <MarkdownPreviewOutlineItem v-for="item in result" :key="item.href" :value="item" />
    </n-anchor>
</template>