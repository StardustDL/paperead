<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useStore } from '../services/store'
import VditorPreview from "vditor";
import "vditor/dist/index.css";

const store = useStore();

const props = defineProps<{
    value: string,
    baseApiUrl?: string
}>();

const baseApiUrl = props.baseApiUrl ?? "";

const element = ref<HTMLDivElement>();

onMounted(async () => {
    await VditorPreview.preview(element.value!, props.value);

    let tagAs = element.value!.getElementsByTagName("a");
    for (let i = 0; i < tagAs.length; i++) {
        let item = tagAs.item(i);
        let rawHref = item?.getAttribute("href");
        if (rawHref?.startsWith("./") || rawHref?.startsWith("../")) {
            item?.setAttribute("href", `${baseApiUrl}/${rawHref}`);
        }
    }
    {
        let tags = element.value!.getElementsByTagName("img");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (rawSrc?.startsWith("./") || rawSrc?.startsWith("../")) {
                item?.setAttribute("src", `${baseApiUrl}/${rawSrc}`);
            }
        }
    }
    {
        let tags = element.value!.getElementsByTagName("video");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (rawSrc?.startsWith("./") || rawSrc?.startsWith("../")) {
                item?.setAttribute("src", `${baseApiUrl}/${rawSrc}`);
            }
        }
    }
    {
        let tags = element.value!.getElementsByTagName("audio");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            let rawSrc = item?.getAttribute("src");
            if (rawSrc?.startsWith("./") || rawSrc?.startsWith("../")) {
                item?.setAttribute("src", `${baseApiUrl}/${rawSrc}`);
            }
        }
    }
});
</script>

<template>
    <div ref="element"></div>
</template>