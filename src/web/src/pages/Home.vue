<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NBreadcrumbItem, NIcon, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar } from 'naive-ui'
import { Home } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../components/PageLayout.vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useStore } from '../services/store'

const store = useStore();
const router = useRouter();

const version = import.meta.env.PACKAGE_VERSION;
const apiMetadata = await store.state.api.metadata();
</script>

<script lang="ts">
export default {
    components: {
        Home,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header subtitle="主页" @back="() => router.back()">
                <template #title>Home</template>
                <template #header>
                    <n-breadcrumb>
                        <n-breadcrumb-item>Paperead</n-breadcrumb-item>
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <home />
                        </n-icon>
                    </n-avatar>
                </template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <n-space vertical>
                <span>
                    Server:&nbsp;
                    <a :href="store.state.api.baseUrl">{{ store.state.api.baseUrl }}</a>
                </span>
                <span>
                    Client Version:&nbsp;
                    <a
                        :href="`https://github.com/StardustDL/paperead/releases/tag/v${version}`"
                    >{{ version }}</a>
                </span>
                <span>
                    Server Version:&nbsp;
                    <a
                        :href="`https://github.com/StardustDL/paperead/releases/tag/v${apiMetadata.version}`"
                    >{{ apiMetadata.version }}</a>
                </span>
            </n-space>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>