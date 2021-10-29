<script setup lang="ts">
import { NSpace } from 'naive-ui'
import { Document } from '../../models'
import MetadataTimeViewer from './MetadataTimeViewer.vue'
import MetadataTagViewer from './MetadataTagViewer.vue'
import MetadataWordCountViewer from './MetadataWordCountViewer.vue';
import MetadataReadTimeViewer from './MetadataReadTimeViewer.vue';

const props = defineProps<{
    data: Document
}>();

</script>

<template>
    <n-space>
        <MetadataTimeViewer :creation="data.metadata.creation" :modification="data.metadata.modification" />
        <MetadataTagViewer :tags="data.metadata.tags" v-if="data.metadata.tags.length > 0" />
        <MetadataWordCountViewer :content="data.content" />
        <MetadataReadTimeViewer :content="data.content" />
    </n-space>
</template>
