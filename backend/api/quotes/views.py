from flask import Blueprint, request
from services.quotes import QuotesService

from .operations import compute_adjusted_exchange_rate, compute_quote_value
from .schemas import QuoteQueryParams

quotes = Blueprint('quotes', __name__)


@quotes.route('/quote', methods=['GET'])
def get_quote():
    query_dict = request.args.to_dict()
    try:
        query_params = QuoteQueryParams(**query_dict)
    except ValueError as e:
        return {
            "message": "Invalid query parameters provided",
            "error": e.errors(),
        }, 400
    quotes_response = QuotesService.get_quotes(currency=query_params.origin_currency)
    if not quotes_response.success:
        return {
            "message": "Failed to fetch quotes",
            "error": quotes_response.error,
        }, quotes_response.status_code

    exchange_rate = quotes_response.exchange_rates[query_params.destination_currency]
    adjusted_exchange_rate = compute_adjusted_exchange_rate(exchange_rate)
    value = compute_quote_value(
        amount=query_params.amount,
        adjusted_exchange_rate=adjusted_exchange_rate,
    )

    return {
        "value": value,
        "exchange_rate": adjusted_exchange_rate,
    }, 200
