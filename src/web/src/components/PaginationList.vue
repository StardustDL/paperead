<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { NThing, NIcon, NAvatar, NTime, NSpace, NCard, NEllipsis, NPagination, NSkeleton } from 'naive-ui'
import { useRoute } from 'vue-router'
import { Book, Clock } from '@vicons/tabler'
import { Icon } from '@vicons/utils'

import { useStore } from '../services/store'

const store = useStore();

const props = defineProps<{
    items: string[]
}>();

const selectedItems = ref<string[]>([]);
const currentPage = ref(1);
const currentPageSize = ref(5);

function refreshItems() {
    let start = (currentPage.value - 1) * currentPageSize.value;
    selectedItems.value = props.items.slice(start, start + currentPageSize.value);
}

watch(currentPage, refreshItems);
watch(currentPageSize, refreshItems);
onMounted(refreshItems);
watch(props, () => currentPage.value = 1);
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
    <n-space vertical>
        <suspense v-for="item in selectedItems" :key="item">
            <template #default>
                <slot :item="item"></slot>
            </template>
            <template #fallback>
                <n-skeleton text :repeat="2" />
            </template>
        </suspense>

        <n-pagination
            style="justify-content: center; margin-top: 20px;"
            :item-count="items.length"
            v-model:page-size="currentPageSize"
            v-model:page="currentPage"
            :page-sizes="[5, 10, 20]"
            show-quick-jumper
            show-size-picker
        ></n-pagination>
    </n-space>
</template>
