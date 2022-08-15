<script setup lang="ts">
import { NPageHeader, NSpace, NBreadcrumb, NIcon, NSkeleton, NLayoutContent, NAvatar, NButton, NTabs, NTabPane, useMessage } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { MaterialIcon, NotesIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'
import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialBreadcrumbItem from '../../components/breadcrumbs/MaterialBreadcrumbItem.vue'
import SchemaSwitcher from '../../schemas/SchemaSwitcher.vue'
import NoteIndex from '../notes/NoteIndex.vue'
import { Material } from '../../models/materials'
import NotFound from '../../components/NotFound.vue'
import SchemaIcon from '../../components/SchemaIcon.vue'

const route = useRoute();
const router = useRouter();
const message = useMessage();
const store = useStore();
const params = route.params as {
    id: string
};

const data = ref<Material>();
const error = ref<boolean>(false);

onMounted(async () => {
    try {
        data.value = await store.state.api.materials.get(params.id);
        document.title = `${data.value.metadata.name} - ${await store.state.api.title()}`;
    }
    catch {
        error.value = true;
        message.error(`Failed to load material ${params.id}.`);
        document.title = `Not Found - ${await store.state.api.title()}`;
    }
});
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
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <SchemaIcon :schema="(data ? data.metadata.schema : '')">
                                <MaterialIcon />
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
        <n-tabs type="segment" style="height: 100%;">
            <n-tab-pane name="description" tab="Description" style="height: calc(100% - 52px);">
                <SchemaSwitcher v-if="data" :data="data" />
                <n-skeleton v-else text :repeat="20" />
            </n-tab-pane>
            <n-tab-pane name="notes" tab="Notes" style="height: calc(100% - 52px);">
                <n-layout-content
                    content-style="padding: 10px;"
                    style="height: 100%;"
                    :native-scrollbar="false"
                >
                    <NoteIndex :id="params.id"></NoteIndex>
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