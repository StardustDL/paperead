<script setup lang="ts">
import { ref, h } from 'vue'
import { NGrid, NGi, NLayout, NLayoutSider, NLayoutContent, NLayoutHeader, NMenu, NPageHeader, NText, NIcon, NSpin, NAvatar } from 'naive-ui'
import { Notebook, Home, Files } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { RouterLink, RouterView, useRouter } from 'vue-router'

import ProjectStatus from '../components/ProjectStatus.vue'
import { MaterialRepository } from '../services/repository'

const router = useRouter();

function renderIcon(icon: any) {
    return () => h(NIcon, null, { default: () => h(icon) })
}

const menuActiveKey = ref("home");

const menuOptions = [
    {
        label: "Home",
        key: "home",
        icon: renderIcon(Home),
        route: "/"
    },
    {
        label: "Materials",
        key: "materials",
        icon: renderIcon(Files),
        route: "/materials"
    },
];

async function onMenuClick(key: string, item: any) {
    await router.push(item.route);
}

</script>


<script lang="ts">
export default {
    components: {
        Notebook,
    }
}
</script>

<template>
    <n-layout style="height: 100%">
        <n-layout-header style="padding: 8px; height: 7%" bordered>
            <n-page-header subtitle="阅读与笔记">
                <template #extra>
                    <suspense>
                        <ProjectStatus />
                    </suspense>
                </template>
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
            </n-page-header>
        </n-layout-header>
        <n-layout-content style="height: 93%;">
            <n-layout has-sider style="height: 100%;">
                <n-layout-sider
                    collapse-mode="width"
                    :collapsed-width="48"
                    :width="180"
                    show-trigger="bar"
                    bordered
                >
                    <n-menu
                        v-model:value="menuActiveKey"
                        @update:value="onMenuClick"
                        :options="menuOptions"
                    />
                </n-layout-sider>
                <n-layout-content content-style="padding: 15px;">
                    <suspense>
                        <template #default>
                            <router-view></router-view>
                        </template>
                        <template #fallback>
                            <n-spin :size="80" id="loading-spin" style="width: 100%" />
                        </template>
                    </suspense>
                </n-layout-content>
            </n-layout>
        </n-layout-content>
    </n-layout>
</template>
