<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { NPageHeader, NSpace, NText, NBreadcrumb, NIcon, NLayoutContent, NAvatar, NStatistic, NTabs, NTabPane, NCard, NButton, useOsTheme, useMessage } from 'naive-ui'
import { Notebook } from '@vicons/tabler'
import { MaterialsIcon, EnableReaderIcon, DisableReaderIcon } from '../components/icons'
import PageLayout from '../components/PageLayout.vue'
import { useRouter } from 'vue-router'
import HomeBreadcrumbItem from '../components/breadcrumbs/HomeBreadcrumbItem.vue'
import SchemaSwitcher from '../schemas/SchemaSwitcher.vue'
import { useStore } from '../services/store'
import MaterialIndex from './materials/MaterialIndex.vue'
import { Note } from '../models/notes'

const store = useStore();
const router = useRouter();
const message = useMessage();

const osThemeRef = useOsTheme();

const isReader = computed(() => store.state.readerMode && osThemeRef.value != "dark");

function reader(enable: boolean = true) {
    store.commit("setReaderMode", enable);
}

const version = import.meta.env.PACKAGE_VERSION;
const apiMetadata = await store.state.api.metadata();
const subtitle = apiMetadata.site.subtitle != '' ? apiMetadata.site.subtitle : "";
const description = apiMetadata.site.description != '' ? apiMetadata.site.description : `Welcome to ${await store.state.api.title()}.`;

document.title = `Home - ${await store.state.api.title()}`;

const data = ref<Note>();

onMounted(async () => {
    try {
        data.value = await store.state.api.materials.builtins().home();
    }
    catch {
    }
});
</script>

<script lang="ts">
export default {
    components: {
        Notebook,
        MaterialsIcon, EnableReaderIcon, DisableReaderIcon
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header :subtitle="subtitle" @back="() => router.back()">
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <notebook />
                        </n-icon>
                    </n-avatar>
                </template>
                <template #title>
                    <span v-if="apiMetadata.site.title == ''">
                        <n-text type="info">Reading</n-text>&nbsp;and
                        <n-text type="success">Notes</n-text>
                    </span>
                    <span v-else>{{ apiMetadata.site.title }}</span>
                </template>
                <template #header>
                    <n-breadcrumb>
                        <HomeBreadcrumbItem />
                    </n-breadcrumb>
                </template>
                <template #extra>
                    <n-button size="large" :bordered="false" title="Reader mode" @click="() => reader(!isReader)">
                        <template #icon>
                            <n-icon>
                                <DisableReaderIcon v-if="isReader" />
                                <EnableReaderIcon v-else />
                            </n-icon>
                        </template>
                    </n-button>
                </template>
                <template #footer>{{ description }}</template>
            </n-page-header>
        </template>
        <n-tabs type="segment" style="height: 100%;">
            <n-tab-pane name="info" tab="Information" style="height: calc(100% - 52px);">
                <n-layout-content content-style="padding: 10px;" style="height: 100%;" :native-scrollbar="false">
                    <SchemaSwitcher v-if="data" :data="data" />
                    <!--
                    <n-space vertical size="large">
                        <n-card title="Server" hoverable embedded>
                            <n-space size="large">
                                <n-statistic label="Server Endpoint">
                                    <a :href="store.state.api.baseUrl">{{ store.state.api.baseUrl }}</a>
                                </n-statistic>
                                <n-statistic label="Server Version">
                                    <a
                                        :href="`https://github.com/StardustDL/paperead/releases/tag/v${apiMetadata.version}`"
                                    >{{ apiMetadata.version }}</a>
                                </n-statistic>
                                <n-statistic label="Client Version">
                                    <a
                                        :href="`https://github.com/StardustDL/paperead/releases/tag/v${version}`"
                                    >{{ version }}</a>
                                </n-statistic>
                            </n-space>
                        </n-card>
                        <n-card title="Paperead" hoverable embedded>
                            <suspense>
                                <ProjectStatus />
                            </suspense>
                        </n-card>
                    </n-space>
                    -->
                </n-layout-content>
            </n-tab-pane>
            <n-tab-pane name="materials" tab="Materials" style="height: calc(100% - 52px);">
                <n-layout-content content-style="padding: 10px;" style="height: 100%;" :native-scrollbar="false">
                    <MaterialIndex></MaterialIndex>
                </n-layout-content>
            </n-tab-pane>
        </n-tabs>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>