<script setup lang="ts">
import { NIcon, NSpace, NTag } from 'naive-ui'
import { Tag } from '@vicons/tabler'

const props = defineProps<{
    tags: string[]
}>();

</script>

<script lang="ts">
export default {
    components: {
        Tag,
    }
}
</script>

<template>
    <n-space size="small">
        <n-icon size="large">
            <tag />
        </n-icon>
        <n-tag v-for="item in props.tags" :key="item" size="small">{{ item }}</n-tag>
    </n-space>
</template>
