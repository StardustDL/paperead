<script setup lang="ts">
import { Document } from '../../models'
import { NLayoutContent } from 'naive-ui'

const props = defineProps<{
  data: Document,
}>();

</script>

<template>
  <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="height: 100%;" v-html="data.content">
  </n-layout-content>
</template>