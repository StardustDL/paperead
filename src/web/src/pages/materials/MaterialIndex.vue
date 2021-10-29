<script setup lang="ts">
import { NLayoutContent } from 'naive-ui'
import MaterialItem from '../../components/MaterialItem.vue'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'

const store = useStore();

const items = await store.state.api.materials.all();
</script>

<template>
    <PaginationList :items="items">
        <template v-slot:default="slotProps">
            <MaterialItem :id="slotProps.item"></MaterialItem>
        </template>
    </PaginationList>
</template>