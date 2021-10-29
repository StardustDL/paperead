<script setup lang="ts">
import { min2read } from '../../helpers';
import { NIcon, NTime, NSpace, NTooltip } from 'naive-ui'
import { Clock } from '@vicons/tabler'
import { computed } from 'vue';

const props = defineProps<{
    content: string;
}>();

const display = computed(() => {
    let result = min2read(props.content);
    if (result <= 1) {
        return "1 minute";
    }
    else {
        return `${Math.round(result)} minutes`;
    }
})
</script>

<script lang="ts">
export default {
    components: {
        Clock,
    }
}
</script>

<template>
    <n-space size="small">
        <n-icon size="large">
            <clock />
        </n-icon>
        <span>{{ display }}</span>
    </n-space>
</template>