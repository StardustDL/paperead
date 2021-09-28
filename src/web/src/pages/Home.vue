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
                <template #footer>API Server: {{ store.state.apiUrl }}</template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <n-space vertical></n-space>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>