<script setup lang="ts">
import { NIcon, NTime, NSpace, NTooltip } from 'naive-ui'
import { FileText } from '@vicons/tabler'
import { wordcount } from '../../helpers';
import { computed } from 'vue';

const props = defineProps<{
    content: string;
}>();

const display = computed(() => {
    let result = wordcount(props.content);
    if (result < 1000) {
        return result.toString();
    }
    else {
        return `${Math.round(result / 1000)}k`;
    }
});

</script>

<script lang="ts">
export default {
    components: {
        FileText,
    }
}
</script>

<template>
    <n-space size="small">
        <n-icon size="large">
            <file-text />
        </n-icon>
        <span>{{ display }}</span>
    </n-space>
</template>