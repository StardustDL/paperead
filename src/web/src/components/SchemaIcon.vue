<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useMessage, NIcon } from 'naive-ui'
import { Music, Video, File, Presentation, Photo, Link, Browser, Box } from '@vicons/tabler'

import { useStore } from '../services/store'

const store = useStore();
const message = useMessage();

const props = defineProps<{
    schema: string
}>();
</script>

<script lang="ts">
export default {
    components: {
        Music,
        Video,
        File,
        Presentation,
        Photo,
        Link,
        Browser,
        Box
    }
}
</script>

<template>
    <File v-if="schema == 'empty'" />
    <Presentation v-else-if="schema == 'slides'" />
    <Video v-else-if="schema == 'video'" />
    <Music v-else-if="schema == 'audio'" />
    <Photo v-else-if="schema == 'image'" />
    <Link v-else-if="schema == 'link'" />
    <Browser v-else-if="schema == 'html'" />
    <Box v-else-if="schema == 'raw'" />
    <slot v-else name="default"></slot>
</template>