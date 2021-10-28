<script setup lang="ts">
import { NPageHeader, NSpace, NBreadcrumb, NIcon, NSkeleton, NLayoutContent, NAvatar, NButton, NTabs, NTabPane } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { MaterialIcon, NotesIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'
import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialBreadcrumbItem from '../../components/breadcrumbs/MaterialBreadcrumbItem.vue'
import SchemaSwitcher from '../../schemas/SchemaSwitcher.vue'
import NoteIndex from '../notes/NoteIndex.vue'

const route = useRoute();
const router = useRouter();
const store = useStore();
const params = <{
    id: string
}>route.params;

const data = await store.state.api.materials.get(params.id);
document.title = `${data.metadata.name} - Paperead`;
</script>

<script lang="ts">
export default {
    components: {
        MaterialIcon,
        NotesIcon,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header @back="() => router.back()">
                <template #title>{{ data.metadata.name }}</template>
                <template #header>
                    <n-breadcrumb>
                        <HomeBreadcrumbItem />
                        <MaterialBreadcrumbItem :id="data.id" />
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <MaterialIcon />
                        </n-icon>
                    </n-avatar>
                </template>
                <template #extra>
                    <MetadataDetailViewer :data="data" />
                </template>
                <template #footer>
                    <MetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content style="height: 100%;">
            <n-tabs type="segment" style="height: 100%;">
                <n-tab-pane name="description" tab="Description" style="height: calc(100% - 52px);">
                    <suspense>
                        <template #default>
                            <SchemaSwitcher :data="data" />
                        </template>
                        <template #fallback>
                            <n-skeleton text :repeat="10" />
                        </template>
                    </suspense>
                </n-tab-pane>
                <n-tab-pane name="notes" tab="Notes" style="height: calc(100% - 52px);">
                    <NoteIndex :id="params.id"></NoteIndex>
                </n-tab-pane>
            </n-tabs>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>