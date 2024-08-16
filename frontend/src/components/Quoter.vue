<script setup lang="ts">
import CurrencySelect from "./CurrencySelect.vue";
import CountryFlag from "./CountryFlag.vue";
import SpinnerLoading from "./SpinnerLoading.vue";
import { ref, defineProps, computed } from "vue";
import { useQuery } from "@tanstack/vue-query";
import fetchQuote from "@/services/quotesService";
import formatCurrency from "@/utils/currency";
import {
  fetchSendCountries,
  fetchIncomingCountries,
} from "@/services/countriesService";
import { type QuoteResponse } from "@/types/quote";

const props = defineProps({
  initialOriginCurrency: { type: String, required: true },
  initialOriginCountry: { type: String, required: true },
  initialDestinationCurrency: { type: String, required: true },
  initialDestinationCountry: { type: String, required: true },
});

const originCurrency = ref<string>(props.initialOriginCurrency);
const destinationCurrency = ref<string>(props.initialDestinationCurrency);
const amount = ref<number>(1000);

const isSendCLP = computed(() => originCurrency.value === "clp");

const selectedCurrency = computed({
  get: () =>
    isSendCLP.value ? destinationCurrency.value : originCurrency.value,
  set: (value) => {
    if (isSendCLP.value) destinationCurrency.value = value;
    else originCurrency.value = value;
  },
});

const fetchQuoteData = async () => {
  return fetchQuote({
    originCurrency: originCurrency.value,
    destinationCurrency: destinationCurrency.value,
    amount: amount.value,
  });
};

const {
  data: quoteData,
  isLoading: quoteIsLoading,
  error: quoteError,
} = useQuery<QuoteResponse, Error>({
  queryKey: ["quote", originCurrency, destinationCurrency, amount],
  queryFn: fetchQuoteData,
});

const {
  data: sendCountries,
  isLoading: sendCountriesIsLoading,
  error: sendCountriesError,
} = useQuery({
  queryKey: ["sendCountries"],
  queryFn: fetchSendCountries,
  enabled: isSendCLP.value,
});

const {
  data: incomingCountries,
  isLoading: incomingCountriesIsLoading,
  error: incomingCountriesError,
} = useQuery({
  queryKey: ["incomingCountries"],
  queryFn: fetchIncomingCountries,
  enabled: !isSendCLP.value,
});
</script>

<template>
  <SpinnerLoading
    v-if="
      quoteIsLoading || sendCountriesIsLoading || incomingCountriesIsLoading
    "
  />
  <div
    v-else
    class="w-full max-w-xs p-6 border border-blue-200 rounded-lg bg-gray-50"
  >
    <div class="flex flex-col space-y-3">
      <div class="flex items-center space-x-2">
        <span class="font-semibold text-gray-800">Envías:</span>
        <input
          class="w-full p-2 text-gray-700 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500"
          v-model.number="amount"
          type="number"
          placeholder="Amount"
        />
      </div>
      <div v-if="isSendCLP" class="flex items-center space-x-2">
        <CountryFlag countryISO="cl" />
        <span class="text-sm text-gray-600">Chile - CLP</span>
      </div>
      <CurrencySelect
        v-else
        :countries="incomingCountries"
        v-model:selectedCurrency="selectedCurrency"
        :inititialCountry="initialOriginCountry"
      />
    </div>
    <hr class="my-3 border-gray-300" />
    <div class="flex flex-col space-y-3">
      <div class="flex items-center space-x-2">
        <span class="font-semibold text-gray-800">Recibe:</span>
        <span class="font-medium text-gray-800">{{
          formatCurrency(quoteData?.value)
        }}</span>
      </div>
      <CurrencySelect
        v-if="isSendCLP"
        :countries="sendCountries"
        v-model:selectedCurrency="selectedCurrency"
        :inititialCountry="initialDestinationCountry"
      />
      <div v-else class="flex items-center space-x-2">
        <CountryFlag countryISO="cl" />
        <span class="text-sm text-gray-600">Chile - CLP</span>
      </div>
    </div>
    <hr class="my-3 border-gray-300" />
    <p class="mt-2 text-sm font-medium text-gray-500">
      *tipo de cambio: {{ formatCurrency(quoteData?.exchangeRate) }}
    </p>
  </div>
  <div v-if="quoteError || sendCountriesError || incomingCountriesError">
    <p class="text-red-500">Error fetching data</p>
  </div>
</template>
