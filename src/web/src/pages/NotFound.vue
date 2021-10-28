<script setup lang="ts">
import { NButton, NIcon,  NResult } from 'naive-ui'
import { AlertCircle } from '@vicons/tabler'
import { HomeIcon } from '../components/icons'
import { RouterLink, useRoute } from 'vue-router'
import { useStore } from '../services/store'

const route = useRoute();

const params = <{
    path: string[]
}>route.params;

console.log("NotFound")

</script>

<script lang="ts">
export default {
    components: {
        HomeIcon,
        AlertCircle,
    }
}
</script>

<template>
    <n-result :status="'404'" title="Not Found" :description="`Path: /${params.path.join('/')}`" style="margin: 50px;">
        <template #footer>
            <n-button>
                <template #icon>
                    <n-icon>
                        <HomeIcon />
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