<script setup lang="ts">
import { Document } from '../models'
import MarkdownSchema from './markdown/MarkdownSchema.vue'
import SlidesSchema from './slides/SlidesSchema.vue'
import MediaSchema from './media/media/MediaSchema.vue';
import ImageSchema from './media/image/ImageSchema.vue';
import PdfSchema from './media/pdf/PdfSchema.vue';

const props = defineProps<{
    data: Document,
}>();
</script>

<template>
    <span v-if="data.metadata.schema == 'empty'">Empty data</span>
    <SlidesSchema v-else-if="data.metadata.schema == 'slides'" :data="data"/>
    <MediaSchema v-else-if="data.metadata.schema == 'media'" :data="data"/>
    <ImageSchema v-else-if="data.metadata.schema == 'image'" :data="data"/>
    <PdfSchema v-else-if="data.metadata.schema == 'pdf'" :data="data"/>
    <MarkdownSchema v-else :data="data" />
</template>
