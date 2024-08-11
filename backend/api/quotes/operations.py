def compute_adjusted_exchange_rate(exchange_rate: float) -> float:
    return exchange_rate * 0.95


def compute_quote_value(amount: float, adjusted_exchange_rate: float) -> float:
    return amount * adjusted_exchange_rate
