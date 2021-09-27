<script setup lang="ts">
import { ref } from 'vue'
import { NIcon, NTime, NSpace, NTag } from 'naive-ui'
import { Tag } from '@vicons/tabler'
import { Icon } from '@vicons/utils'

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
    <n-space>
        <n-icon size="large">
            <tag />
        </n-icon>
        <n-tag v-for="item in props.tags" :key="item" size="small">{{ item }}</n-tag>
    </n-space>
</template>
