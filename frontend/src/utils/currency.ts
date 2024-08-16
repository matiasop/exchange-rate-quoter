function formatCurrency(amount: number, locale: string = "en-US"): string {
  return new Intl.NumberFormat(locale, {
    style: "decimal",
    minimumFractionDigits: 2,
    maximumFractionDigits: 4,
  }).format(amount);
}

export default formatCurrency;
