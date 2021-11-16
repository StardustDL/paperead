<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { RouterLink } from 'vue-router'
import { NCard, NEllipsis, NSkeleton, useMessage, NAvatar, NIcon, NSpace } from 'naive-ui'
import { renderToPlainText } from '../helpers'
import MetadataViewer from './metadata/MetadataViewer.vue'

import { NoteIcon } from './icons'
import { useStore } from '../services/store'
import { Note } from '../models/notes'
import SchemaIcon from './SchemaIcon.vue'

const store = useStore();
const message = useMessage();

const props = defineProps<{
    id: string,
    noteId: string,
}>();


const data = ref<Note>();

async function loadData() {
    data.value = undefined;
    try {
        data.value = await store.state.api.materials.notes(props.id).get(props.noteId);
    }
    catch {
        data.value = undefined;
        message.error(`Failed to load note ${props.noteId} of material ${props.id}.`);
    }
}

onMounted(loadData);
watch(props, loadData);
</script>

<script lang="ts">
export default {
    components: {
        NoteIcon,
    }
}
</script>

<template>
    <n-card hoverable>
        <template #header>
            <n-space>
                <n-avatar>
                    <n-icon>
                        <SchemaIcon :schema="(data ? data.metadata.schema : '')">
                            <NoteIcon />
                        </SchemaIcon>
                    </n-icon>
                </n-avatar>
                <router-link :to="`/${props.id}/${noteId}`" style="vertical-align: middle;">
                    <span v-if="data">{{ data.metadata.name }}</span>
                    <span v-else>{{ noteId }}</span>
                </router-link>
            </n-space>
        </template>
        <n-ellipsis
            :tooltip="false"
            :line-clamp="5"
            v-if="data"
        >{{ renderToPlainText(data.content) }}</n-ellipsis>
        <n-skeleton v-else text :repeat="10"></n-skeleton>
        <template #action>
            <MetadataViewer v-if="data" :data="data" />
        </template>
    </n-card>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>