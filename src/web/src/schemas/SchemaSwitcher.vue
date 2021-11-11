<script setup lang="ts">
import { Document } from '../models'
import MarkdownSchema from './markdown/MarkdownSchema.vue'
import SlidesSchema from './slides/SlidesSchema.vue'
import ImageSchema from './media/image/ImageSchema.vue';
import LinkSchema from './media/link/LinkSchema.vue';
import HtmlSchema from './html/HtmlSchema.vue';
import RawSchema from './raw/RawSchema.vue';
import VideoSchema from './media/video/VideoSchema.vue';
import AudioSchema from './media/audio/AudioSchema.vue';

const props = defineProps<{
    data: Document,
}>();
</script>

<template>
    <span v-if="data.metadata.schema == 'empty'">Empty data</span>
    <SlidesSchema v-else-if="data.metadata.schema == 'slides'" :data="data"/>
    <VideoSchema v-else-if="data.metadata.schema == 'video'" :data="data"/>
    <AudioSchema v-else-if="data.metadata.schema == 'audio'" :data="data"/>
    <ImageSchema v-else-if="data.metadata.schema == 'image'" :data="data"/>
    <LinkSchema v-else-if="data.metadata.schema == 'link'" :data="data"/>
    <HtmlSchema v-else-if="data.metadata.schema == 'html'" :data="data"/>
    <RawSchema v-else-if="data.metadata.schema == 'raw'" :data="data"/>
    <MarkdownSchema v-else :data="data" />
</template>
