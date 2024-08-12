<script setup lang="ts">
import CurrencySelect from "./CurrencySelect.vue";
import { ref, defineProps, computed } from "vue";
import { useQuery } from "@tanstack/vue-query";
import fetchQuote from "@/services/quotesService";
import {
  fetchSendCountries,
  fetchIncomingCountries,
} from "@/services/countriesService";
import { type QuoteResponse } from "@/types/quote";

const props = defineProps({
  initialOriginCurrency: { type: String, required: true },
  initialDestinationCurrency: { type: String, required: true },
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
  <div v-if="quoteIsLoading">Loading...</div>
  <div v-else>
    <div>
      <span>Tú envías:</span>
      <input v-model.number="amount" type="number" placeholder="Amount" />
      <span v-if="isSendCLP">clp</span>
      <CurrencySelect
        v-else
        :countries="incomingCountries"
        v-model:selectedCurrency="selectedCurrency"
      />
      <br />
      <span>El destinatario recibe: {{ quoteData?.value }}</span>
      <CurrencySelect
        v-if="isSendCLP"
        :countries="sendCountries"
        v-model:selectedCurrency="selectedCurrency"
      />
      <span v-else>clp</span>
      <div class="h-4"></div>
      <p>Exchange Rate: {{ quoteData?.exchangeRate }}</p>
    </div>
  </div>
  <div v-if="quoteError || sendCountriesError || incomingCountriesError">
    <p>Error fetching data</p>
  </div>
</template>
