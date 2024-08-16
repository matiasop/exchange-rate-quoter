const getFlagUrl = (isoCode: string): string => {
  return `https://cdnjs.cloudflare.com/ajax/libs/flag-icon-css/4.1.4/flags/4x3/${isoCode.toLowerCase()}.svg`;
};

export default getFlagUrl;
