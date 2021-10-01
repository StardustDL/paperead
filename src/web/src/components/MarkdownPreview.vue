<script setup lang="ts">
import { onMounted, ref, computed, watch } from 'vue'
import { useStore } from '../services/store'
import VditorPreview from "vditor";
import "vditor/dist/index.css";
import { isRelativeUrl } from '../helpers';

const store = useStore();

const props = defineProps<{
    value: string,
    baseUrl?: string
}>();

const baseUrl = computed(() => props.baseUrl ?? "");

const element = ref<HTMLDivElement>();

async function renderMarkdown() {
    await VditorPreview.preview(element.value!, props.value);

    let tagAs = element.value!.getElementsByTagName("a");
    for (let i = 0; i < tagAs.length; i++) {
        let item = tagAs.item(i);
        let rawHref = item?.getAttribute("href") as string;
        if (isRelativeUrl(rawHref)) {
            item?.setAttribute("href", `${baseUrl.value}/${rawHref}`);
        }
    }
    {
        let tags = element.value!.getElementsByTagName("img");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (isRelativeUrl(rawSrc as string)) {
                item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
            }
        }
    }
    {
        let tags = element.value!.getElementsByTagName("video");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (isRelativeUrl(rawSrc as string)) {
                item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
            }
        }
    }
    {
        let tags = element.value!.getElementsByTagName("audio");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (isRelativeUrl(rawSrc as string)) {
                item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
            }
        }
    }
}

onMounted(renderMarkdown);
watch(props, renderMarkdown);
</script>

<template>
    <div ref="element"></div>
</template>