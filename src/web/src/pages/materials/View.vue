<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NBreadcrumbItem, NIcon, NTime, NBackTop, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NLayoutSider } from 'naive-ui'
import { useRoute } from 'vue-router'
import { Book } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import MarkdownPreview from '../../components/MarkdownPreview.vue'

import { useStore } from '../../services/store'

const route = useRoute();
const store = useStore();
const params = <{
    id: string
}>route.params;

const data = await store.state.materials.get(params.id);
</script>

<script lang="ts">
export default {
    components: {
        Book,
    }
}
</script>

<template>
    <n-layout style="height: 100%;">
        <n-layout-header bordered style="height: 18%">
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
                    <n-space>
                        <span>Creation:</span>
                        <n-time :time="data.metadata.creation" type="relative"></n-time>
                        <span>Modification:</span>
                        <n-time :time="data.metadata.modification" type="relative"></n-time>
                    </n-space>
                </template>
            </n-page-header>
        </n-layout-header>
        <n-layout style="height: 82%" has-sider sider-placement="right">
            <n-layout-content
                content-style="padding: 10px;"
                :native-scrollbar="false"
                style="height: 100%"
            >
                <MarkdownPreview :value="data.content" />

                <n-back-top :right="200"/>
            </n-layout-content>
            <n-layout-sider
                collapse-mode="transform"
                :collapsed-width="120"
                :width="240"
                :native-scrollbar="false"
                show-trigger="arrow-circle"
                content-style="padding: 24px;"
                bordered
            >
                <p>asdasd</p>
            </n-layout-sider>
        </n-layout>
    </n-layout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>