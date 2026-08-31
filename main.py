from fastapi import FastAPI
app = FastAPI()

taxas = {
    "USD-BRL": 5.40,
    "BRL-USD": 0.185,
    "EUR-BRL": 5.85
}

@app.get("/converter")
def converter(valor: float, de: str, para: str):
    chave = f"{de}-{para}"
    resultado = taxas[chave] * valor
    return {"resultado": resultado}

