<script setup lang="ts">
import { defineProps, defineEmits, watch, ref, onMounted } from "vue";
import countryNamesData from "@/assets/countryNames.json";
import CountryFlag from "./CountryFlag.vue";
import { type CountryCurrency, type CountryNames } from "@/types/countries";

const props = defineProps<{
  countries: CountryCurrency[];
  selectedCurrency: string;
  inititialCountry: string;
}>();

const selectedCountryISO = ref<string>(props.inititialCountry);

const countryNames = countryNamesData as CountryNames;

const emit = defineEmits<{
  (e: "update:selectedCurrency", value: string): void;
}>();

const handleSelection = (event: Event) => {
  const target = event.target as HTMLSelectElement;
  const selectedOption = target.options[target.selectedIndex];
  const countryISO = selectedOption.dataset.country as string;
  selectedCountryISO.value = countryISO;
  emit("update:selectedCurrency", target.value);
};

const getCountryName = (isoCode: string): string => {
  return countryNames[isoCode.toUpperCase()] || isoCode.toLowerCase();
};

const getCountryLabel = (country: CountryCurrency): string => {
  return `${getCountryName(country.isoCode)} - ${country.currency}`;
};
</script>

<template>
  <div class="flex gap-2">
    <CountryFlag :countryISO="selectedCountryISO" />
    <select
      class="w-full text-sm text-gray-500"
      :value="selectedCurrency"
      @change="handleSelection"
    >
      <option
        v-for="country in countries"
        :key="country.id"
        :value="country.currency.toLowerCase()"
        :data-country="country.isoCode.toLowerCase()"
      >
        <p>
          {{ getCountryLabel(country) }}
        </p>
      </option>
    </select>
  </div>
</template>
