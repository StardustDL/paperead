<script setup lang="ts">
import { onMounted, ref, computed, watch, h } from 'vue'
import { useStore } from '../services/store'
import MarkdownPreviewOutline from './MarkdownPreviewOutline.vue';
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NAnchor, NAnchorLink, NBackTop } from 'naive-ui'
import Vditor from 'vditor';
import "vditor/dist/index.css";
import { isRelativeUrl } from '../helpers';

const store = useStore();

const osThemeRef = useOsTheme();

const props = defineProps<{
    value: string,
    baseUrl?: string
}>();

const baseUrl = computed(() => props.baseUrl ?? "");

const theme = computed(() => osThemeRef.value == "dark" ? "dark" : "light");

const element = ref<HTMLDivElement>();
const outline = ref<any>();

async function renderMarkdown() {
    await Vditor.preview(element.value!, props.value, {
        mode: theme.value,
        hljs: {
            lineNumber: true
        },
        markdown: {
            toc: true,
            linkBase: baseUrl.value,
            mark: true,
        },
        theme: {
            current: theme.value,
        },
    });

    await outline.value.renderOutline();

    // let tagAs = element.value!.getElementsByTagName("a");
    // for (let i = 0; i < tagAs.length; i++) {
    //     let item = tagAs.item(i);
    //     let rawHref = item?.getAttribute("href") as string;
    //     if (isRelativeUrl(rawHref)) {
    //         item?.setAttribute("href", `${baseUrl.value}/${rawHref}`);
    //     }
    // }
    {
        let tags = element.value!.getElementsByTagName("img");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            if (item == null)
                continue;
            item.onclick = ev => {
                Vditor.previewImage(item!, undefined, theme.value);
            }
            // let rawSrc = item?.getAttribute("src");
            // if (isRelativeUrl(rawSrc as string)) {
            //     item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
            // }
        }
    }
    // {
    //     let tags = element.value!.getElementsByTagName("video");
    //     for (let i = 0; i < tags.length; i++) {
    //         let item = tags.item(i);
    //         let rawSrc = item?.getAttribute("src");
    //         if (isRelativeUrl(rawSrc as string)) {
    //             item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
    //         }
    //     }
    // }
    // {
    //     let tags = element.value!.getElementsByTagName("audio");
    //     for (let i = 0; i < tags.length; i++) {
    //         let item = tags.item(i);
    //         let rawSrc = item?.getAttribute("src");
    //         if (isRelativeUrl(rawSrc as string)) {
    //             item?.setAttribute("src", `${baseUrl.value}/${rawSrc}`);
    //         }
    //     }
    // }
}

onMounted(renderMarkdown);
watch(props, renderMarkdown);
watch(osThemeRef, renderMarkdown);
</script>

<template>
    <n-layout style="height: 100%;" has-sider sider-placement="right" content-style="padding: 10px;">
        <n-layout-content style="height: 100%;" :native-scrollbar="false">
            <div ref="element"></div>
            <n-back-top :right="250"></n-back-top>
        </n-layout-content>
        <n-layout-sider
            style="height: 100%;"
            collapse-mode="width"
            :collapsed-width="0"
            :width="200"
            show-trigger="bar"
            bordered
            :default-collapsed="false"
        >
            <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="padding: 10px;">
                <MarkdownPreviewOutline :element="element" ref="outline" />
            </n-layout-content>
        </n-layout-sider>
    </n-layout>
</template>