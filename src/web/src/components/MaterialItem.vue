<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { NCard, NEllipsis } from 'naive-ui'
import { RouterLink } from 'vue-router'
import { renderToPlainText } from '../helpers'
import MetadataViewer from './metadata/MetadataViewer.vue'

import { useStore } from '../services/store'
import { Material } from '../models/materials'

const store = useStore();

const props = defineProps<{
    id: string
}>();


const data = ref<Material | undefined>();

async function loadData() {
    data.value = await store.state.api.materials.get(props.id);
}

onMounted(loadData);
watch(props, loadData);
</script>

<template>
    <n-card v-if="data" hoverable>
        <template #header>
            <router-link :to="`/${data.id}`">{{ data.metadata.name }}</router-link>
        </template>
        <n-ellipsis
            :tooltip="false"
            :line-clamp="5"
            v-if="data.content.length > 0"
        >{{ renderToPlainText(data.content) }}</n-ellipsis>
        <template #action>
            <MetadataViewer :data="data" />
        </template>
    </n-card>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>