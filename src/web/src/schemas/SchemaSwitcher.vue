<script setup lang="ts">
import { Document } from '../models';
import MarkdownSchema from './markdown/MarkdownSchema.vue';

const props = defineProps<{
    data: Document,
}>();
</script>

<template>
    <span v-if="data.metadata.schema == 'empty'">Empty data</span>
    <MarkdownSchema v-else :data="data" />
</template>
