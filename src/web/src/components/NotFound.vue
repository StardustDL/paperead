<script setup lang="ts">
import { NButton, NIcon,  NResult } from 'naive-ui'
import { AlertCircle } from '@vicons/tabler'
import { HomeIcon } from './icons'
import { RouterLink, useRoute } from 'vue-router'
import { useStore } from '../services/store'

const store = useStore();

const props = defineProps<{
    path: string
}>();

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
    <n-result :status="'404'" title="Not Found" :description="`Path: ${path}`" style="margin: 50px;">
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