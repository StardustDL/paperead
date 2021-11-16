<script setup lang="ts">
import { NSkeleton, useMessage } from 'naive-ui'
import { onMounted, ref } from 'vue'
import { NotesIcon } from '../../components/icons'
import NoteItem from '../../components/NoteItem.vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'
import NotFound from '../../components/NotFound.vue'

const props = defineProps<{
    id: string
}>();

const store = useStore();
const message = useMessage();
const router = useRouter();

const items = ref<string[]>();
const error = ref<boolean>(false);

onMounted(async () => {
    try {
        items.value = await store.state.api.materials.notes(props.id).all();
    }
    catch {
        error.value = true;
        message.error(`Failed to load note list for material ${props.id}.`)
        document.title = `Not Found - ${await store.state.api.title()}`;
    }
});
</script>

<script lang="ts">
export default {
    components: {
        NotesIcon,
    }
}
</script>

<template>
    <NotFound v-if="error" :path="router.currentRoute.value.fullPath"></NotFound>
    <PaginationList v-else-if="items" :items="items">
        <template v-slot:default="slotProps">
            <NoteItem :id="id" :noteId="slotProps.item"></NoteItem>
        </template>
    </PaginationList>
    <n-skeleton v-else text :repeat="20" />
</template>