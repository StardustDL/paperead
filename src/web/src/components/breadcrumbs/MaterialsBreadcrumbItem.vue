<script setup lang="ts">
import { NIcon, NBreadcrumbItem } from 'naive-ui'
import { MaterialsIcon } from '../icons'
import { RouterLink } from 'vue-router'

</script>

<script lang="ts">
export default {
    components: {
        MaterialsIcon
    }
}
</script>

<template>
    <n-breadcrumb-item>
        <router-link to="/materials">
            <n-icon>
                <MaterialsIcon />
            </n-icon>
            Materials
        </router-link>
    </n-breadcrumb-item>
</template>