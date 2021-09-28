<script setup lang="ts">
import { ref } from 'vue'
import { NIcon, NTime, NSpace, NTag } from 'naive-ui'
import { Tag } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { MaterialMetadata } from '../../models/materials'
import MetadataTimeViewer from './MetadataTimeViewer.vue'
import MetadataTagViewer from './MetadataTagViewer.vue'

const props = defineProps<{
    data: MaterialMetadata
}>();

</script>

<template>
    <n-space>
        <MetadataTimeViewer :creation="data.creation" :modification="data.modification" />
        <MetadataTagViewer :tags="data.tags" v-if="data.tags.length > 0" />
    </n-space>
</template>
