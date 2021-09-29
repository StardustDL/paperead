<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NBreadcrumb, NTooltip, NPopover, NDropdown, NTable, NBreadcrumbItem, NIcon, NTime, NBackTop, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NLayoutSider, NButton } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { Book, Notes } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import MarkdownPreview from '../../components/MarkdownPreview.vue'

import { useStore } from '../../services/store'
import MetadataViewer from '../../components/metadata/MetadataViewer.vue'
import MetadataDetailViewer from '../../components/metadata/MetadataDetailViewer.vue'

const route = useRoute();
const router = useRouter();
const store = useStore();
const params = <{
    id: string
}>route.params;

const headerHeight = 120;

const data = await store.state.materials.get(params.id);

document.title = `${data.metadata.name} - Materials - Paperead`;
</script>

<script lang="ts">
export default {
    components: {
        Book,
        Notes,
    }
}
</script>

<template>
    <PageLayout float-header>
        <template #header>
            <n-page-header :subtitle="data.id" @back="() => router.back()">
                <template #title>{{ data.metadata.name }}</template>
                <template #header>
                    <n-breadcrumb>
                        <n-breadcrumb-item>
                            <router-link to="/">Paperead</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>
                            <router-link to="/materials">Materials</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>{{ data.id }}</n-breadcrumb-item>
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <book />
                        </n-icon>
                    </n-avatar>
                </template>
                <template #extra>
                    <n-space>
                        <n-button
                            :bordered="false"
                            @click="router.push(`/materials/${data.id}/notes`)"
                        >
                            <template #icon>
                                <n-icon>
                                    <notes />
                                </n-icon>
                            </template>
                        </n-button>
                        <MetadataDetailViewer :target-base-url="store.state.materials.resolveRelativeUrl(data.id)" :data="data.metadata"/>
                    </n-space>
                </template>
                <template #footer>
                    <MetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <suspense>
                <template #default>
                    <MarkdownPreview
                        :value="data.content"
                        :base-url="store.state.materials.resolveRelativeUrl(data.id)"
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