<script setup lang="ts">
import { ref } from 'vue'
import { NIcon, NTime, NSpace, NTag } from 'naive-ui'
import { Tag } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { NoteMetadata } from '../../models/notes'
import MetadataTimeViewer from './MetadataTimeViewer.vue'
import MetadataTagViewer from './MetadataTagViewer.vue'

const props = defineProps<{
    data: NoteMetadata
}>();

</script>

<template>
    <n-space>
        <MetadataTimeViewer
            :creation="data.creation"
            :modification="data.modification"
        />
    </n-space>
</template>
