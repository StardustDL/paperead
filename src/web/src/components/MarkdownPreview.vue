<script setup lang="ts">
import { onMounted, ref } from 'vue'
import VditorPreview from "vditor";
import "vditor/dist/index.css";

const props = defineProps<{ value: string }>();

const element = ref();

onMounted(() => {
    VditorPreview.preview(element.value, props.value);
});
</script>

<template>
    <div ref="element"></div>
</template>