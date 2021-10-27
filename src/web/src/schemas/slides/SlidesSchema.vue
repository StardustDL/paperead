<script setup lang="ts">
import { isRelativeUrl } from '../../helpers';
import { Document } from '../../models'
import { useOsTheme } from 'naive-ui';
import Reveal from './Reveal.vue';

const osThemeRef = useOsTheme();

const props = defineProps<{
  data: Document,
}>();
</script>

<template>
  <Reveal :data="data" />
</template>