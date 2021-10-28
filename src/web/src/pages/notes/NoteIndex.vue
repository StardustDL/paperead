<script setup lang="ts">
import { NPageHeader, NBreadcrumb, NIcon, NLayoutContent, NAvatar } from 'naive-ui'
import { NotesIcon } from '../../components/icons'
import PageLayout from '../../components/PageLayout.vue'
import NoteItem from '../../components/NoteItem.vue'
import { useRouter, useRoute } from 'vue-router'
import { useStore } from '../../services/store'
import PaginationList from '../../components/PaginationList.vue'

const store = useStore();
const props = defineProps<{
    id: string
}>();

const items = await store.state.api.materials.notes(props.id).all();
</script>

<script lang="ts">
export default {
    components: {
        NotesIcon,
    }
}
</script>

<template>
    <n-layout-content
        content-style="padding: 10px;"
        :native-scrollbar="false"
        style="height: 100%;"
    >
        <PaginationList :items="items">
            <template v-slot:default="slotProps">
                <NoteItem :id="id" :noteId="slotProps.item"></NoteItem>
            </template>
        </PaginationList>
    </n-layout-content>
</template>