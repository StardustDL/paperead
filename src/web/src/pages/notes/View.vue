<script setup lang="ts">
import { NPageHeader, NBreadcrumb, NIcon, NSkeleton, NLayoutContent, NAvatar } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { NoteIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'
import MarkdownPreview from '../../components/MarkdownPreview.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'

import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialsBreadcrumbItem from '../../components/breadcrumbs/MaterialsBreadcrumbItem.vue'
import MaterialBreadcrumbItem from '../../components/breadcrumbs/MaterialBreadcrumbItem.vue'
import NotesBreadcrumbItem from '../../components/breadcrumbs/NotesBreadcrumbItem.vue'
import NoteBreadcrumbItem from '../../components/breadcrumbs/NoteBreadcrumbItem.vue'

const route = useRoute();
const router = useRouter();
const store = useStore();
const params = <{
    id: string,
    noteId: string,
}>route.params;

const data = await store.state.api.materials.notes(params.id).get(params.noteId);

const material = await store.state.api.materials.get(params.id);

document.title = `${data.metadata.name} - Notes - ${material.metadata.name} - Materials - Paperead`;
</script>

<script lang="ts">
export default {
    components: {
        NoteIcon,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header :subtitle="data.id" @back="() => router.back()">
                <template #title>{{ data.metadata.name }}</template>
                <template #header>
                    <n-breadcrumb>
                        <HomeBreadcrumbItem />
                        <MaterialsBreadcrumbItem />
                        <MaterialBreadcrumbItem :id="params.id" />
                        <NotesBreadcrumbItem :id="params.id" />
                        <NoteBreadcrumbItem :id="params.id" :note-id="data.id" />
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <NoteIcon />
                        </n-icon>
                    </n-avatar>
                </template>
                <template #extra>
                    <MetadataDetailViewer
                        :target-base-url="store.state.api.materials.resolveRelativeUrl(params.id, './notes')"
                        :data="data.metadata"
                    />
                </template>
                <template #footer>
                    <MetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content style="height: 100%;">
            <suspense>
                <template #default>
                    <MarkdownPreview
                        :value="data.content"
                        :base-url="store.state.api.materials.resolveRelativeUrl(params.id, './notes')"
                    />
                </template>
                <template #fallback>
                    <n-skeleton text :repeat="10" />
                </template>
            </suspense>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>