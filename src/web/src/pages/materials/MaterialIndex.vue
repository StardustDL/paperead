<script setup lang="ts">
import { NSkeleton, useMessage } from 'naive-ui'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import MaterialItem from '../../components/MaterialItem.vue'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'
import NotFound from '../../components/NotFound.vue'

const store = useStore();
const message = useMessage();
const router = useRouter();

const items = ref<string[]>()
const error = ref<boolean>(false);

onMounted(async () => {
    try {
        items.value = await store.state.api.materials.all();
    }
    catch {
        error.value = true;
        message.error(`Failed to load material list.`)
        document.title = `Not Found - ${await store.state.api.title()}`;
    }
});
</script>

<template>
    <NotFound v-if="error" :path="router.currentRoute.value.fullPath"></NotFound>
    <PaginationList v-else-if="items" :items="items">
        <template v-slot:default="slotProps">
            <MaterialItem :id="slotProps.item"></MaterialItem>
        </template>
    </PaginationList>
    <n-skeleton v-else text :repeat="20" />
</template>