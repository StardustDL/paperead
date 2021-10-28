<script setup lang="ts">
import { ref } from 'vue'
import { NIcon, NBreadcrumbItem } from 'naive-ui'
import { MaterialIcon } from '../icons'
import { RouterLink } from 'vue-router'

const props = defineProps<{
    id: string
}>();

</script>

<script lang="ts">
export default {
    components: {
        MaterialIcon
    }
}
</script>

<template>
    <n-breadcrumb-item>
        <router-link :to="`/${id}`">
            <n-icon>
                <MaterialIcon />
            </n-icon>
            {{ id }}
        </router-link>
    </n-breadcrumb-item>
</template>