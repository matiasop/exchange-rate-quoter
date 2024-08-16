<script setup lang="ts">
import getFlagUrl from "@/utils/flags";

const props = defineProps<{
  countryISO: string;
}>();
</script>

<template>
  <img class="w-8" :src="getFlagUrl(countryISO)" :alt="countryISO" />
</template>
