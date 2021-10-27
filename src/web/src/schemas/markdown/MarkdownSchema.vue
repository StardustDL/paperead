<script setup lang="ts">
import { Document } from '../../models';
import MarkdownPreview from '../../components/markdown/MarkdownPreview.vue';

const props = defineProps<{
    data: Document,
}>();
</script>

<template>
    <MarkdownPreview :value="data.content" :base-url="data.dataUrl" />
</template>
