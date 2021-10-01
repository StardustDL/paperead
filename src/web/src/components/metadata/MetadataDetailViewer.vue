<script setup lang="ts">
import { ref, h, computed } from 'vue'
import { NPageHeader, NSpace, NBreadcrumb, NTooltip, NPopover, NDropdown, NTable, NBreadcrumbItem, NIcon, NTime, NBackTop, NSkeleton, NLayout, NLayoutContent, NLayoutHeader, NAvatar, NLayoutSider, NButton } from 'naive-ui'
import { Book, ArrowRight, ExternalLink, InfoSquare, Notes } from '@vicons/tabler'
import { Icon } from '@vicons/utils'
import { BaseMetadata } from '../../models'
import MetadataTimeViewer from './MetadataTimeViewer.vue'
import MetadataTagViewer from './MetadataTagViewer.vue'
import { useStore } from '../../services/store'
import { isRelativeUrl } from '../../helpers'

const store = useStore();

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
        Notes,
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
                <n-button :bordered="false">
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
            <n-button :bordered="false">
                <template #icon>
                    <n-icon>
                        <external-link />
                    </n-icon>
                </template>
            </n-button>
        </n-dropdown>
    </n-space>
</template>
