<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { NLayout, NLayoutContent, NLayoutHeader, NBackTop } from 'naive-ui'

const props = defineProps<{ headerHeight?: number, floatHeader?: boolean }>();

const headerHeight = props.headerHeight ?? 130;
const floatHeader = props.floatHeader ?? false;
</script>

<template>
    <n-layout style="height: 100%;" v-if="floatHeader" :native-scrollbar="false">
        <n-layout-header bordered :style="`height: ${headerHeight}px;`">
            <slot name="header"></slot>
        </n-layout-header>
        <n-layout-content>
            <slot name="default"></slot>
        </n-layout-content>
        <n-back-top :right="100"></n-back-top>
    </n-layout>
    <n-layout style="height: 100%;" v-else>
        <n-layout-header bordered :style="`height: ${headerHeight}px;`">
            <slot name="header"></slot>
        </n-layout-header>
        <n-layout-content :style="`height: calc(100% - ${headerHeight}px);`" :native-scrollbar="false">
            <slot name="default"></slot>
            <n-back-top :right="100"></n-back-top>
        </n-layout-content>
    </n-layout>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>