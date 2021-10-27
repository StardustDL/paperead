<script setup lang="ts">
import { NIcon, NBreadcrumbItem } from 'naive-ui'
import { NotesIcon } from '../icons'
import { RouterLink } from 'vue-router'

const props = defineProps<{
    id: string
}>();

</script>

<script lang="ts">
export default {
    components: {
        NotesIcon,
    }
}
</script>

<template>
    <n-breadcrumb-item>
        <router-link :to="`/materials/${id}/notes`">
            <n-icon>
                <NotesIcon />
            </n-icon>
            Notes
        </router-link>
    </n-breadcrumb-item>
</template>