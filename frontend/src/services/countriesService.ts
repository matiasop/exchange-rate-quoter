import axios from "axios";
import { type CountryCurrency } from "@/types/countries";

const API_BASE_URL = "https://elb.currencybird.cl/apigateway-cb/api/public";

const fetchFromApi = async <T>(endpoint: string): Promise<T> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/${endpoint}`);
    return response.data;
  } catch (error) {
    console.error(`Error fetching data from ${endpoint}:`, error);
    throw error;
  }
};

export const fetchSendCountries = async (): Promise<CountryCurrency[]> => {
  return fetchFromApi<CountryCurrency[]>("sendCountries");
};

export const fetchIncomingCountries = async (): Promise<CountryCurrency[]> => {
  return fetchFromApi<CountryCurrency[]>("IncomingCountries");
};
