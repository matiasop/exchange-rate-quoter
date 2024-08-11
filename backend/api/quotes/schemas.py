from pydantic import BaseModel, confloat, root_validator


class QuoteQueryParams(BaseModel):
    origin_currency: str
    destination_currency: str
    amount: confloat(gt=0.0)

    @root_validator(pre=True)
    @classmethod
    def check_currencies(cls, values):
        origin_currency = values.get("origin_currency")
        destination_currency = values.get("destination_currency")

        if origin_currency == destination_currency:
            raise ValueError(
                "origin_currency must be different from destination_currency"
            )

        if "clp" not in {origin_currency, destination_currency}:
            raise ValueError(
                "Either origin_currency or destination_currency must be 'clp'"
            )

        return values
