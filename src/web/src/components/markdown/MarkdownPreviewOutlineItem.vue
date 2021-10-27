<script setup lang="ts">
import { NAnchorLink } from 'naive-ui'
import { AnchorItem } from '../AnchorItem'

const props = defineProps<{
    value: AnchorItem,
}>();
</script>

<template>
    <n-anchor-link :title="props.value.title" :href="props.value.href">
        <MarkdownPreviewOutlineItem
            v-for="item in props.value.children"
            :key="item.href"
            :value="item"
        />
    </n-anchor-link>
</template>