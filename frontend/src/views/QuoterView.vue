<script setup lang="ts">
import Quoter from "@/components/Quoter.vue";
</script>

<template>
  <p>QUOTER VIEW</p>
  <Quoter initial-origin-currency="clp" initial-destination-currency="usd" />
  <Quoter initial-origin-currency="usd" initial-destination-currency="clp" />
</template>
