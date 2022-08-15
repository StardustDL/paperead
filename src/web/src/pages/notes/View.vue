<script setup lang="ts">
import { NPageHeader, NBreadcrumb, NIcon, NSkeleton, NLayoutContent, NAvatar, NSpin, useMessage } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { onMounted, ref } from 'vue'
import { NoteIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'

import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialBreadcrumbItem from '../../components/breadcrumbs/MaterialBreadcrumbItem.vue'
import NoteBreadcrumbItem from '../../components/breadcrumbs/NoteBreadcrumbItem.vue'
import SchemaSwitcher from '../../schemas/SchemaSwitcher.vue'
import { Note } from '../../models/notes'
import { Material } from '../../models/materials'
import NotFound from '../../components/NotFound.vue'
import SchemaIcon from '../../components/SchemaIcon.vue'

const route = useRoute();
const message = useMessage();
const router = useRouter();
const store = useStore();
const params = route.params as {
    id: string,
    noteId: string,
};

const data = ref<Note>();
const material = ref<Material>();
const error = ref<boolean>(false);

onMounted(async () => {
    try {
        data.value = await store.state.api.materials.notes(params.id).get(params.noteId);
        material.value = await store.state.api.materials.get(params.id);
        document.title = `${data.value.metadata.name} - ${material.value.metadata.name} - ${await store.state.api.title()}`;
    }
    catch {
        error.value = true;
        message.error(`Failed to load note ${params.noteId} for material ${params.id}.`);
        document.title = `Not Found - ${await store.state.api.title()}`;
    }
});
</script>

<script lang="ts">
export default {
    components: {
        NoteIcon,
    }
}
</script>

<template>
    <NotFound v-if="error" :path="router.currentRoute.value.fullPath"></NotFound>
    <PageLayout v-else>
        <template #header>
            <n-page-header @back="() => router.back()">
                <template #title>
                    <span v-if="data">{{ data.metadata.name }}</span>
                    <span v-else>Loading...</span>
                </template>
                <template #header>
                    <n-breadcrumb>
                        <HomeBreadcrumbItem />
                        <MaterialBreadcrumbItem :id="params.id" />
                        <NoteBreadcrumbItem :id="params.id" :note-id="params.noteId" />
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <SchemaIcon :schema="(data ? data.metadata.schema : '')">
                                <NoteIcon />
                            </SchemaIcon>
                        </n-icon>
                    </n-avatar>
                </template>
                <template #extra>
                    <MetadataDetailViewer v-if="data" :data="data" />
                </template>
                <template #footer>
                    <MetadataViewer v-if="data" :data="data" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content style="height: 100%;">
            <SchemaSwitcher v-if="data" :data="data" />
            <n-skeleton v-else text :repeat="20" />
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>