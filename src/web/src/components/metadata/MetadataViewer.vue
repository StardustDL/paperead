<script setup lang="ts">
import { NSpace } from 'naive-ui'
import { BaseMetadata } from '../../models'
import MetadataTimeViewer from './MetadataTimeViewer.vue'
import MetadataTagViewer from './MetadataTagViewer.vue'

const props = defineProps<{
    data: BaseMetadata
}>();

</script>

<template>
    <n-space>
        <MetadataTimeViewer :creation="data.creation" :modification="data.modification" />
        <MetadataTagViewer :tags="data.tags" v-if="data.tags.length > 0" />
    </n-space>
</template>
