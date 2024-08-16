<script setup lang="ts">
import Quoter from "@/components/Quoter.vue";
</script>

<template>
  <div class="flex flex-col items-center w-screen h-screen">
    <p class="mt-8 text-4xl font-bold">Cotizador</p>
    <div class="h-16"></div>
    <div class="flex flex-col gap-8 sm:flex-row">
      <Quoter
        initial-origin-currency="clp"
        initial-origin-country="cl"
        initial-destination-currency="usd"
        initial-destination-country="ac"
      />
      <Quoter
        initial-origin-currency="eur"
        initial-origin-country="at"
        initial-destination-currency="clp"
        initial-destination-country="cl"
      />
    </div>
  </div>
</template>
