<script setup lang="ts">
import { Document } from '../models'
import MarkdownSchema from './markdown/MarkdownSchema.vue'
import SlidesSchema from './slides/SlidesSchema.vue'

const props = defineProps<{
    data: Document,
}>();
</script>

<template>
    <span v-if="data.metadata.schema == 'empty'">Empty data</span>
    <SlidesSchema v-else-if="data.metadata.schema == 'slides'" :data="data"/>
    <MarkdownSchema v-else :data="data" />
</template>
