<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NBreadcrumbItem, NIcon, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar } from 'naive-ui'
import { Notes } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import PageLayout from '../../components/PageLayout.vue'
import NoteItem from '../../components/NoteItem.vue'
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
import { useStore } from '../../services/store'

const store = useStore();
const router = useRouter();
const route = useRoute();
const params = <{
    id: string
}>route.params;

const items = await store.state.materials.notes(params.id).all();

const material = await store.state.materials.get(params.id);
document.title = `Notes - ${material.metadata.name} - Materials - Paperead`

</script>

<script lang="ts">
export default {
    components: {
        Notes,
    }
}
</script>

<template>
    <PageLayout>
        <template #header>
            <n-page-header subtitle="所有笔记" @back="() => router.back()">
                <template #title>Notes</template>
                <template #header>
                    <n-breadcrumb>
                        <n-breadcrumb-item>
                            <router-link to="/">Paperead</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>
                            <router-link to="/materials">Materials</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>
                            <router-link :to="`/materials/${params.id}`">{{ params.id }}</router-link>
                        </n-breadcrumb-item>
                        <n-breadcrumb-item>Notes</n-breadcrumb-item>
                    </n-breadcrumb>
                </template>
                <template #avatar>
                    <n-avatar>
                        <n-icon>
                            <notes />
                        </n-icon>
                    </n-avatar>
                </template>
                <template
                    #footer
                >Totally {{ items.length }} note{{ items.length > 1 ? 's' : '' }}.</template>
            </n-page-header>
        </template>
        <n-layout-content content-style="padding: 10px;">
            <n-space vertical>
                <suspense v-for="item in items" :key="item">
                    <template #default>
                        <NoteItem :id="params.id" :noteId="item"></NoteItem>
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