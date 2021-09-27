<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { NLayout, NLayoutContent, NLayoutHeader } from 'naive-ui'

const props = defineProps<{ headerHeight?: number }>();

const headerHeight = props.headerHeight ?? 130;
</script>

<template>
    <n-layout style="height: 100%;">
        <n-layout-header bordered :style="`height: ${headerHeight}px;`">
            <slot name="header"></slot>
        </n-layout-header>
        <n-layout-content :style="`height: calc(100% - ${headerHeight}px);`">
            <slot name="default"></slot>
        </n-layout-content>
    </n-layout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>