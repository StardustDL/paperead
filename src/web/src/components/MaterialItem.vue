<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { NCard, NEllipsis, NSkeleton, useMessage, NAvatar, NIcon, NSpace } from 'naive-ui'
import { RouterLink } from 'vue-router'
import { renderToPlainText } from '../helpers'

import { MaterialIcon } from './icons'
import SchemaIcon from './SchemaIcon.vue'
import MetadataViewer from './metadata/MetadataViewer.vue'

import { useStore } from '../services/store'
import { Material } from '../models/materials'

const store = useStore();
const message = useMessage();

const props = defineProps<{
    id: string
}>();


const data = ref<Material>();

async function loadData() {
    data.value = undefined;
    try {
        data.value = await store.state.api.materials.get(props.id);
    }
    catch {
        data.value = undefined;
        message.error(`Failed to load meterial ${props.id}.`);
    }
}

onMounted(loadData);
watch(props, loadData);
</script>


<script lang="ts">
export default {
    components: {
        MaterialIcon,
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
                            <MaterialIcon />
                        </SchemaIcon>
                    </n-icon>
                </n-avatar>
                <router-link :to="`/${id}`" style="vertical-align: middle;">
                    <span v-if="data">{{ data.metadata.name }}</span>
                    <span v-else>{{ id }}</span>
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