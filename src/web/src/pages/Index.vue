<script setup lang="ts">
import { ref } from 'vue'
import { MaterialRepository } from '../services/repository'


const count = ref(0)

let repo = new MaterialRepository("http://localhost:8000/api");
let item = await repo.get("a");
console.log(item.metadata.creation.toDateString());

</script>

<template>
<p>{{ item.metadata.modification }}</p>
</template>
