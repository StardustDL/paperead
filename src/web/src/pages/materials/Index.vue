<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NBreadcrumbItem, NIcon, NSkeleton, NPagination, NLayout, NLayoutFooter, NLayoutContent, NLayoutHeader, NAvatar } from 'naive-ui'
import { Files } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import MaterialItem from '../../components/MaterialItem.vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'

const store = useStore();
const router = useRouter();

const items = await store.state.api.materials.all();
</script>

<script lang="ts">
export default {
    components: {
        Files,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header subtitle="所有材料" @back="() => router.back()">
                <template #title>Materials</template>
                <template #header>
                    <n-breadcrumb>
                        <n-breadcrumb-item>
                            <router-link to="/">Paperead</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>Materials</n-breadcrumb-item>
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <files />
                        </n-icon>
                    </n-avatar>
                </template>
                <template
                    #footer
                >Totally {{ items.length }} material{{ items.length > 1 ? 's' : '' }}.</template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <PaginationList :items="items">
                <template v-slot:default="slotProps">
                    <MaterialItem :id="slotProps.item"></MaterialItem>
                </template>
            </PaginationList>
        </n-layout-content>
    </PageLayout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>