<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NBreadcrumb, NTooltip, NPopover, NDropdown, NTable, NBreadcrumbItem, NIcon, NTime, NBackTop, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NLayoutSider, NButton } from 'naive-ui'
import { useRoute, useRouter } from 'vue-router'
import { Book, ArrowRight, ExternalLink, InfoSquare, Notes } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import MarkdownPreview from '../../components/MarkdownPreview.vue'

import { useStore } from '../../services/store'
import MaterialMetadataViewer from '../../components/metadata/MaterialMetadataViewer.vue'

const route = useRoute();
const router = useRouter();
const store = useStore();
const params = <{
    id: string
}>route.params;

const headerHeight = 120;

const data = await store.state.materials.get(params.id);

document.title = `${data.metadata.name} - Materials - Paperead`;

let targetOptions: {
    label: string,
    key: string
}[] = [];

for (let key in data.metadata.targets) {
    targetOptions.push({
        label: key,
        key: key,
    });
}

function onTargetClick(key: string) {
    window.open(store.state.materials.resolveRelativeUrl(data.id, data.metadata.targets[key]));
}
</script>

<script lang="ts">
export default {
    components: {
        Book,
        ArrowRight,
        ExternalLink,
        InfoSquare,
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
                        <n-popover placement="bottom-start" trigger="hover">
                            <template #trigger>
                                <n-button :bordered="false">
                                    <template #icon>
                                        <n-icon>
                                            <info-square />
                                        </n-icon>
                                    </template>
                                </n-button>
                            </template>
                            <n-table>
                                <thead>
                                    <tr>
                                        <th>Key</th>
                                        <th>Value</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(item, key) in data.metadata.extra" :key="key">
                                        <td>{{ key }}</td>
                                        <td>{{ item }}</td>
                                    </tr>
                                </tbody>
                            </n-table>
                        </n-popover>
                        <n-dropdown
                            :options="targetOptions"
                            placement="bottom-start"
                            @select="onTargetClick"
                        >
                            <n-button :bordered="false">
                                <template #icon>
                                    <n-icon>
                                        <external-link />
                                    </n-icon>
                                </template>
                            </n-button>
                        </n-dropdown>
                    </n-space>
                </template>
                <template #footer>
                    <MaterialMetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <suspense>
                <template #default>
                    <MarkdownPreview
                        :value="data.content"
                        :base-api-url="store.state.materials.resolveRelativeUrl(data.id)"
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