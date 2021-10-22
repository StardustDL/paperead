<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NText, NBreadcrumb, NBreadcrumbItem, NIcon, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NStatistic, NCard } from 'naive-ui'
import { Home, Notebook } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../components/PageLayout.vue'
import ProjectStatus from '../components/ProjectStatus.vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useStore } from '../services/store'

const store = useStore();
const router = useRouter();

const version = import.meta.env.PACKAGE_VERSION;
const apiMetadata = await store.state.api.metadata();
</script>

<script lang="ts">
export default {
    components: {
        Home,
        Notebook
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header subtitle="阅读与笔记" @back="() => router.back()">
                <template #avatar>
                    <n-avatar size="large">
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
                        <n-breadcrumb-item>Paperead</n-breadcrumb-item>
                    </n-breadcrumb>
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