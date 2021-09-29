<script setup lang="ts">
import { ref } from 'vue'
import { NPageHeader, NSpace, NThing, NBreadcrumb, NButton, NBreadcrumbItem, NIcon, NSkeleton, NLayout, NLayoutContent, NResult, NLayoutHeader, NAvatar } from 'naive-ui'
import { Home, AlertCircle } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { RouterLink, RouterView, useRoute } from 'vue-router'
import { useStore } from '../services/store'

const store = useStore();
const route = useRoute();

const params = <{
    path: string[]
}>route.params;

</script>

<script lang="ts">
export default {
    components: {
        Home,
        AlertCircle,
    }
}
</script>

<template>
    <n-result :status="'404'" title="Not Found" :description="`Path: /${params.path.join('/')}`">
        <template #footer>
            <n-button>
                <template #icon>
                    <n-icon>
                        <home />
                    </n-icon>
                </template>
                <router-link to="/">Home</router-link>
            </n-button>
        </template>
    </n-result>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>