export interface CountryCurrency {
  isoCode: string;
  currency: string;
  id: string;
}

export interface CountryNames {
  [isoCode: string]: string;
}
