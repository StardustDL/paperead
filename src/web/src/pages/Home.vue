<script setup lang="ts">
import { ref, computed } from 'vue'
import { NPageHeader, NSpace, NText, NBreadcrumb, NIcon, NLayoutContent, NAvatar, NStatistic, NCard, NButton, useOsTheme } from 'naive-ui'
import { Notebook } from '@vicons/tabler'
import { MaterialsIcon, EnableReaderIcon, DisableReaderIcon } from '../components/icons'
import PageLayout from '../components/PageLayout.vue'
import ProjectStatus from '../components/ProjectStatus.vue'
import { useRouter } from 'vue-router'
import HomeBreadcrumbItem from '../components/breadcrumbs/HomeBreadcrumbItem.vue'
import { useStore } from '../services/store'

const store = useStore();
const router = useRouter();

const osThemeRef = useOsTheme();

const isReader = computed(() => store.state.readerMode && osThemeRef.value != "dark");

function reader(enable: boolean = true) {
    store.commit("setReaderMode", enable);
}

const version = import.meta.env.PACKAGE_VERSION;
const apiMetadata = await store.state.api.metadata();
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
            <n-page-header subtitle="阅读与笔记" @back="() => router.back()">
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <notebook />
                        </n-icon>
                    </n-avatar>
                </template>
                <template #title>
                    <n-text type="info">Reading</n-text>&nbsp;and
                    <n-text type="success">Notes</n-text>
                </template>
                <template #header>
                    <n-breadcrumb>
                        <HomeBreadcrumbItem />
                    </n-breadcrumb>
                </template>
                <template #extra>
                    <n-space>
                        <n-button
                            size="large"
                            :bordered="false"
                            @click="router.push(`/materials`)"
                            title="Materials"
                        >
                            <template #icon>
                                <n-icon>
                                    <MaterialsIcon />
                                </n-icon>
                            </template>
                        </n-button>
                        <n-button
                            size="large"
                            :bordered="false"
                            title="Reader mode"
                            @click="() => reader(!isReader)"
                        >
                            <template #icon>
                                <n-icon>
                                    <DisableReaderIcon v-if="isReader" />
                                    <EnableReaderIcon v-else />
                                </n-icon>
                            </template>
                        </n-button>
                    </n-space>
                </template>
                <template #footer>Welcome to Paperead.</template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <n-space vertical size="large">
                <n-card title="Server Information" hoverable embedded>
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
                <n-card title="Paperead Information" hoverable embedded>
                    <suspense>
                        <ProjectStatus />
                    </suspense>
                </n-card>
            </n-space>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>