<script setup lang="ts">
import { ref } from 'vue'
import { NIcon, NBreadcrumbItem } from 'naive-ui'
import { HomeIcon } from '../icons'
import { RouterLink } from 'vue-router'

</script>

<script lang="ts">
export default {
    components: {
        HomeIcon,
    }
}
</script>

<template>
    <n-breadcrumb-item>
        <router-link to="/">
            <n-icon>
                <HomeIcon />
            </n-icon>
            Paperead
        </router-link>
    </n-breadcrumb-item>
</template>