<script setup lang="ts">
import { NPageHeader, NBreadcrumb, NIcon, NLayoutContent, NAvatar } from 'naive-ui'
import { MaterialsIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'
import MaterialItem from '../../components/MaterialItem.vue'
import { useRouter } from 'vue-router'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'
import HomeBreadcrumbItem from '../../components/breadcrumbs/HomeBreadcrumbItem.vue'
import MaterialsBreadcrumbItem from '../../components/breadcrumbs/MaterialsBreadcrumbItem.vue'

const store = useStore();
const router = useRouter();

const items = await store.state.api.materials.all();
</script>

<script lang="ts">
export default {
    components: {
        MaterialsIcon
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
                        <HomeBreadcrumbItem />
                        <MaterialsBreadcrumbItem />
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <MaterialsIcon />
                        </n-icon>
                    </n-avatar>
                </template>
                <template
                    #footer
                >Totally {{ items.length }} material{{ items.length > 1 ? 's' : '' }}.</template>
            </n-page-header>
        </template>
        <n-layout-content
            content-style="padding: 10px;"
            :native-scrollbar="false"
            style="height: 100%;"
        >
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