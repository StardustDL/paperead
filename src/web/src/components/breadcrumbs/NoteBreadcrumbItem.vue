<script setup lang="ts">
import { NIcon, NBreadcrumbItem } from 'naive-ui'
import { NoteIcon } from '../icons'
import { RouterLink } from 'vue-router'

const props = defineProps<{
    id: string,
    noteId: string,
}>();

</script>

<script lang="ts">
export default {
    components: {
        NoteIcon
    }
}
</script>

<template>
    <n-breadcrumb-item>
        <router-link :to="`/materials/${id}/${noteId}`">
            <n-icon>
                <NoteIcon />
            </n-icon>
            {{ noteId }}
        </router-link>
    </n-breadcrumb-item>
</template>