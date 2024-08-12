import apiClient from "./apiClient";
import { transformToSnakeCase, transformToCamelCase } from "@/utils/changeCase";
import { type FetchQuoteParams, type QuoteResponse } from "@/types/quote";

const fetchQuote = async (params: FetchQuoteParams): Promise<QuoteResponse> => {
  try {
    const response = await apiClient.get("/quote", {
      params: transformToSnakeCase(params),
    });
    const quoteResponse = transformToCamelCase<QuoteResponse>(response.data);
    return quoteResponse;
  } catch (error) {
    console.error("Error fetching data from quote endpoint:", error);
    throw error;
  }
};

export default fetchQuote;
