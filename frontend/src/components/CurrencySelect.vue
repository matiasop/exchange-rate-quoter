<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import { type CountryCurrency } from "@/types/countries";

const props = defineProps<{
  countries: CountryCurrency[];
  selectedCurrency: string;
}>();

const emit = defineEmits<{
  (e: "update:selectedCurrency", value: string): void;
}>();

const handleSelection = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  emit("update:selectedCurrency", target.value);
};
</script>

<template>
  <select :value="selectedCurrency" @change="handleSelection">
    <option
      v-for="country in countries"
      :key="country.id"
      :value="country.currency.toLowerCase()"
    >
      {{ country.isoCode.toLowerCase() }} - {{ country.currency }}
    </option>
  </select>
</template>
