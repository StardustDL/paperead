<script setup lang="ts">
import { NPageHeader, NSpace, NBreadcrumb, NIcon, NSkeleton, NLayoutContent, NAvatar, NButton } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { MaterialIcon, NotesIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'
import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialsBreadcrumbItem from '../../components/breadcrumbs/MaterialsBreadcrumbItem.vue'
import MaterialBreadcrumbItem from '../../components/breadcrumbs/MaterialBreadcrumbItem.vue'
import SchemaSwitcher from '../../schemas/SchemaSwitcher.vue'

const route = useRoute();
const router = useRouter();
const store = useStore();
const params = <{
    id: string
}>route.params;

const data = await store.state.api.materials.get(params.id);

document.title = `${data.metadata.name} - Materials - Paperead`;
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
                        <MaterialsBreadcrumbItem />
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
                    <n-space>
                        <n-button
                            size="large"
                            :bordered="false"
                            @click="router.push(`/materials/${data.id}/notes`)"
                            title="Notes"
                        >
                            <template #icon>
                                <n-icon>
                                    <NotesIcon />
                                </n-icon>
                            </template>
                        </n-button>
                        <MetadataDetailViewer :data="data" />
                    </n-space>
                </template>
                <template #footer>
                    <MetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content style="height: 100%;">
            <suspense>
                <template #default>
                    <SchemaSwitcher :data="data" />
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