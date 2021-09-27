<script setup lang="ts">
import { ref } from 'vue'
import { NThing, NIcon, NAvatar, NTime, NSpace, NCard, NEllipsis } from 'naive-ui'
import { useRoute } from 'vue-router'
import { Book } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { MaterialRepository } from '../services/repository'

import { useStore } from '../services/store'

const store = useStore();

const props = defineProps<{
    id: string
}>();

const data = await store.state.materials.get(props.id);
</script>

<script lang="ts">
export default {
    components: {
        Book,
    }
}
</script>

<template>
    <n-card>
        <template #header>
            <router-link :to="`/materials/${data.id}`">{{ data.metadata.name }}</router-link>
        </template>
        <template #header-extra></template>
        <n-ellipsis :line-clamp="5">{{ data.content }}</n-ellipsis>
        <template #action>
            <n-space>
                <span>Creation:</span>
                <n-time :time="data.metadata.creation" type="relative"></n-time>
                <span>Modification:</span>
                <n-time :time="data.metadata.modification" type="relative"></n-time>
            </n-space>
        </template>
    </n-card>
</template>

<style scoped>
a {
    text-decoration: none;
    color: inherit;
}
</style>