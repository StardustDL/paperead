<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { RouterLink } from 'vue-router'
import { NCard, NEllipsis } from 'naive-ui'
import { renderToPlainText } from '../helpers'
import MetadataViewer from './metadata/MetadataViewer.vue'

import { useStore } from '../services/store'
import { Note } from '../models/notes'

const store = useStore();

const props = defineProps<{
    id: string,
    noteId: string,
}>();


const data = ref<Note | undefined>();

async function loadData() {
    data.value = await store.state.api.materials.notes(props.id).get(props.noteId);
}

onMounted(loadData);
watch(props, loadData);
</script>

<template>
    <n-card v-if="data" hoverable>
        <template #header>
            <router-link :to="`/materials/${props.id}/${data.id}`">{{ data.metadata.name }}</router-link>
        </template>
        <n-ellipsis
            :tooltip="false"
            :line-clamp="5"
            v-if="data.content.length > 0"
        >{{ renderToPlainText(data.content) }}</n-ellipsis>
        <template #action>
            <MetadataViewer :data="data.metadata" />
        </template>
    </n-card>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>