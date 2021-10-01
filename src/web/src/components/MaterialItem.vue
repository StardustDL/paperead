<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { NThing, NIcon, NAvatar, NTime, NSpace, NCard, NEllipsis } from 'naive-ui'
import { useRoute } from 'vue-router'
import { Book, Clock } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
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

<script lang="ts">
export default {
    components: {
        Book,
        Clock,
    }
}
</script>

<template>
    <n-card v-if="data">
        <template #header>
            <router-link :to="`/materials/${data.id}`">{{ data.metadata.name }}</router-link>
        </template>
        <template #header-extra></template>
        <n-ellipsis
            :tooltip="false"
            :line-clamp="5"
            v-if="data.content.length > 0"
        >{{ data.content }}</n-ellipsis>
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