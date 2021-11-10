<script setup lang="ts">
import { Document } from '../../models'
import { NLayoutContent } from 'naive-ui'
import { ExternalLink } from '@vicons/tabler'

const props = defineProps<{
  data: Document,
}>();

</script>

<template>
  <n-layout-content style="height: 100%;" :native-scrollbar="false" content-style="height: 100%;">
    <iframe height="100%" width="100%" :srcdoc="data.content" style="border:0;"></iframe>
  </n-layout-content>
</template>