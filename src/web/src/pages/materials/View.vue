<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NCollapse, NCollapseItem, NBreadcrumbItem, NIcon, NTime, NBackTop, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NLayoutSider, NButton, NList, NListItem } from 'naive-ui'
import { useRoute } from 'vue-router'
import { Book, ArrowRight } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import MarkdownPreview from '../../components/MarkdownPreview.vue'

import { useStore } from '../../services/store'
import MaterialMetadataViewer from '../../components/metadata/MaterialMetadataViewer.vue'

const route = useRoute();
const store = useStore();
const params = <{
    id: string
}>route.params;

const headerHeight = 120;

const data = await store.state.materials.get(params.id);
</script>

<script lang="ts">
export default {
    components: {
        Book,
        ArrowRight,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header :subtitle="data.id">
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
                <template #footer>
                    <MaterialMetadataViewer :data="data.metadata" />
                </template>
            </n-page-header>
        </template>
        <n-layout has-sider sider-placement="right" style="height: 100%;">
            <n-layout-content
                style="height: 100%;"
                content-style="padding: 10px;"
                :native-scrollbar="false"
            >
                <MarkdownPreview :value="data.content" />

                <n-back-top :right="200" />
            </n-layout-content>
            <n-layout-sider
                collapse-mode="transform"
                :collapsed-width="120"
                :width="240"
                :native-scrollbar="false"
                show-trigger="arrow-circle"
                content-style="padding: 8px;"
                bordered
            >
                <n-collapse>
                    <n-collapse-item title="Targets" name="targets">
                        <n-space vertical style="margin-left: 10px;">
                            <n-button text v-for="(value, key) in data.metadata.targets" :key="key">
                                <template #icon>
                                    <n-icon>
                                        <arrow-right />
                                    </n-icon>
                                </template>
                                <a :href="value">{{ key }}</a>
                            </n-button>
                        </n-space>
                    </n-collapse-item>
                    <n-collapse-item title="Metadata" name="metadata">
                        <n-space vertical style="margin-left: 10px;">
                            <n-button text v-for="(value, key) in data.metadata.extra" :key="key">
                                <template #icon>
                                    <n-icon>
                                        <arrow-right />
                                    </n-icon>
                                </template>
                                <a :href="value">{{ key }}</a>
                            </n-button>
                        </n-space>
                    </n-collapse-item>
                </n-collapse>
            </n-layout-sider>
        </n-layout>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>