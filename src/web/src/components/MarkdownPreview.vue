<script setup lang="ts">
import { onMounted, ref, computed, watch, h } from 'vue'
import { useStore } from '../services/store'
import MarkdownPreviewOutline from './MarkdownPreviewOutline.vue';
import { useOsTheme, NLayout, NLayoutContent, NLayoutSider, NAnchor, NAnchorLink, NBackTop, NAffix, NButton, NSpace, NIcon, NButtonGroup } from 'naive-ui'
import { Maximize, Minimize, Bookmark, BookmarkOff } from '@vicons/tabler'
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

const readerBackgroundColor = "#f9f5e9";

const element = ref<HTMLDivElement>();
const outline = ref<any>();
const collapsed = ref<boolean>(true);
const isFullscreen = ref<boolean>(false);
const isReader = ref<boolean>(false);

const rootStyle = computed(() => {
    let result = {};
    if (isFullscreen.value) {
        result = {
            height: '100%', width: '100%', position: 'fixed',
            top: 0, bottom: 0, left: 0, right: 0, padding: "5px 5px 5px 200px",
            ...result
        };
    }
    else {
        result = {
            height: '100%',
            ...result
        };
    }
    if (isReader.value) {
        result = {
            'background-color': readerBackgroundColor,
            ...result,
        };
    }
    return result;
});

async function renderMarkdown() {
    await Vditor.preview(element.value!, props.value, {
        mode: theme.value,
        speech: {
            enable: true
        },
        hljs: {
            lineNumber: true,
            style: theme.value == "dark" ? "dracula" : "github",
        },
        markdown: {
            linkBase: baseUrl.value,
            mark: true,
        },
        theme: {
            current: theme.value,
            // current: "vscode-light",
            // path:
            //     "https://cdn.jsdelivr.net/gh/HerbertHe/vditor-theme@main/content-theme",
        },
    });

    await outline.value.renderOutline();

    {
        let tags = element.value!.getElementsByTagName("img");
        for (let i = 0; i < tags.length; i++) {
            let item = tags.item(i);
            if (item == null)
                continue;
            item.onclick = ev => {
                Vditor.previewImage(item!, undefined, theme.value);
            }
        }
    }
}

function fullscreen(enable: boolean = true) {
    isFullscreen.value = enable;
}

function reader(enable: boolean = true) {
    isReader.value = enable;
}

onMounted(renderMarkdown);
watch(props, renderMarkdown);
watch(osThemeRef, renderMarkdown);

defineExpose({
    fullscreen,
    reader
});

</script>

<script lang="ts">
export default {
    components: {
        Maximize,
        Minimize,
        Bookmark,
        BookmarkOff,
    }
}
</script>

<template>
    <n-layout :style="rootStyle" has-sider sider-placement="right">
        <n-layout-content
            style="height: 100%; background-color: inherit;"
            :native-scrollbar="false"
        >
            <article ref="element" style="padding-bottom: 200px;"></article>
            <n-back-top :right="(collapsed ? 50 : 250)"></n-back-top>
        </n-layout-content>
        <n-layout-sider
            style="height: 100%; background-color: inherit;"
            collapse-mode="width"
            :collapsed-width="0"
            :width="200"
            show-trigger="bar"
            :default-collapsed="true"
            :show-collapsed-content="false"
            v-model:collapsed="collapsed"
        >
            <n-layout-content
                style="height: 100%; background-color: inherit;"
                :native-scrollbar="false"
                content-style="padding: 10px;"
            >
                <n-space>
                    <n-button-group>
                        <n-button title="Full screen" @click="() => fullscreen(!isFullscreen)">
                            <template #icon>
                                <n-icon>
                                    <Minimize v-if="isFullscreen" />
                                    <Maximize v-else />
                                </n-icon>
                            </template>
                        </n-button>
                        <n-button title="Reader mode" @click="() => reader(!isReader)">
                            <template #icon>
                                <n-icon>
                                    <BookmarkOff v-if="isReader" />
                                    <Bookmark v-else />
                                </n-icon>
                            </template>
                        </n-button>
                    </n-button-group>

                    <MarkdownPreviewOutline :element="element" ref="outline" />
                </n-space>
            </n-layout-content>
        </n-layout-sider>
    </n-layout>
</template>