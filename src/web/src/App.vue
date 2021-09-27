<script setup lang="ts">
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://v3.vuejs.org/api/sfc-script-setup.html#sfc-script-setup
import Layout from './pages/Layout.vue'
import { useRoute } from 'vue-router'
import { NGlobalStyle, NConfigProvider, NSpin, NBackTop, NMessageProvider, NSpace, NImage } from 'naive-ui'

const route = useRoute();
console.log(route);

</script>

<template>
  <n-config-provider style="height: 100%">
    <n-message-provider>
      <n-global-style />
      <suspense>
        <template #default>
          <Layout />
        </template>
        <template #fallback>
          <n-spin :size="80" id="loading-spin" />
        </template>
      </suspense>
    </n-message-provider>
  </n-config-provider>
</template>

<style scoped>
#loading-spin {
  text-align: center;
  width: 100%;
  height: 100vh;
}
</style>

<style>
html, body, #app {
  height: 100%;
}
</style>