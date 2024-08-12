export interface FetchQuoteParams {
  originCurrency: string;
  destinationCurrency: string;
  amount: number;
}

export interface QuoteResponse {
  value: number;
  exchangeRate: number;
}
