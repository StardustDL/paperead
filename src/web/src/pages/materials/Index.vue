<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NBreadcrumbItem, NIcon, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar } from 'naive-ui'
import { Files } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import MaterialItem from '../../components/MaterialItem.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useStore } from '../../services/store'

const store = useStore();

const items = await store.state.materials.all();

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
            <n-page-header subtitle="所有材料">
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
        <n-layout-content
            content-style="padding: 10px;"
            style="height: 100%"
            :native-scrollbar="false"
        >
            <n-space vertical>
                <suspense v-for="item in items" :key="item">
                    <template #default>
                        <MaterialItem :id="item"></MaterialItem>
                    </template>
                    <template #fallback>
                        <n-skeleton text :repeat="2" />
                    </template>
                </suspense>
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