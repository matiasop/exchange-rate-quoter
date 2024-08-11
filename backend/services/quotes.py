import requests
from pydantic import BaseModel

QUOTES_API_URL = "https://latest.currency-api.pages.dev/v1/currencies/"


class QuotesResponse(BaseModel):
    currency: str
    exchange_rates: dict[str, float] | None = None
    success: bool
    error: str | None = None
    status_code: int


class QuotesService:
    @staticmethod
    def get_quotes(currency: str) -> QuotesResponse:
        url = f'{QUOTES_API_URL}{currency}.json'
        print(url)
        response = requests.get(url)

        if not response.ok:
            return QuotesResponse(
                currency=currency,
                success=False,
                error=QuotesService._extract_error_message(response),
                status_code=response.status_code,
            )

        data = response.json()
        return QuotesResponse(
            currency=currency,
            exchange_rates=data[currency],
            success=True,
            status_code=response.status_code,
        )

    @staticmethod
    def _extract_error_message(response: requests.Response) -> str:
        if response.headers.get('Content-Type') == 'application/json':
            return response.json().get('error', response.text)
        return response.text
