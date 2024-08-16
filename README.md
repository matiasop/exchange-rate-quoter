# Cotizador

## Frontend

Escrito en: Vue3 + typescript

Correr los siguientes comandos:

```bash
cd frontend
npm install
npm run dev
```

## Backend

Escrito en: Flask

Correr los siguientes comandos:

```bash
cd backend
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## Documentación - Endpoints

### GET /quote

**Descripción**: obtiene el valor cotizado y la tasa de cambio para una moneda específica. Es necesario que la `origin_currency` o la `destination_currency` sea `clp` (peso chileno).

#### Query params

`origin_currency (string)`: moneda desde la cual se calcula la cotización.

`destination_currency (string)`: la moneda a la cual se aplica la tasa de cambio.

`amount (number)`: la cantidad de `origin_currency` que se va a convertir.

**Ejemplo**: GET /quote?origin_currency=CLP&destination_currency=USD&amount=100

#### Respusta Exitosa

Código 200 OK

`value (number)`: el valor calculado (en `destination_currency`).

`exchange_rate`: la tasa de cambio de `origin_currency` a `destination_currency`.

Ejemplo:

```json
{
  "value": 85.5,
  "exchange_rate": 0.855
}
```

#### Respuesta de Error por parámetros inválidos

Código 400 Bad Request

`message`: el mensaje de error

`error`: detalles del error

Ejemplo:

```json
{
  "message": "Parámetros de consulta inválidos proporcionados",
  "error": [
    // Errores de validación
  ]
}
```
