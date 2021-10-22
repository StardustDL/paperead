<script setup lang="ts">
import { h, computed } from 'vue'
import { NSpace, NPopover, NDropdown, NTable, NIcon, NButton } from 'naive-ui'
import { Book, ArrowRight, ExternalLink, InfoSquare } from '@vicons/tabler'
import { BaseMetadata } from '../../models'
import { isRelativeUrl } from '../../helpers'

const props = defineProps<{
    data: BaseMetadata,
    targetBaseUrl: string,
}>();

const targetOptions = computed(() => {
    let result: {
        label: any,
        key: string
    }[] = [];
    for (let key in props.data.targets) {
        let target = props.data.targets[key];
        let href = isRelativeUrl(target) ? `${props.targetBaseUrl}/${target}` : target;
        result.push({
            label: () => h("a", {
                target: "_blank",
                href,
            }, key),
            key: key,
        });
    };
    return result;
})
</script>

<script lang="ts">
export default {
    components: {
        Book,
        ArrowRight,
        ExternalLink,
        InfoSquare,
    }
}
</script>

<template>
    <n-space>
        <n-popover
            placement="bottom-start"
            trigger="hover"
            v-if="Object.keys(data.extra).length > 0"
        >
            <template #trigger>
                <n-button :bordered="false" size="large" title="Extra">
                    <template #icon>
                        <n-icon>
                            <info-square />
                        </n-icon>
                    </template>
                </n-button>
            </template>
            <n-table>
                <thead>
                    <tr>
                        <th>Key</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, key) in data.extra" :key="key">
                        <td>{{ key }}</td>
                        <td>{{ item }}</td>
                    </tr>
                </tbody>
            </n-table>
        </n-popover>
        <n-dropdown
            :options="targetOptions"
            placement="bottom-start"
            v-if="Object.keys(data.targets).length > 0"
        >
            <n-button :bordered="false" size="large" title="Targets">
                <template #icon>
                    <n-icon>
                        <external-link />
                    </n-icon>
                </template>
            </n-button>
        </n-dropdown>
    </n-space>
</template>
