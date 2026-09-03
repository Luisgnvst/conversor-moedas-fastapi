import requests
from fastapi import FastAPI
app = FastAPI()


@app.get("/converter")
def converter(valor: float, de: str, para: str):
    url = f"https://economia.awesomeapi.com.br/last/{de}-{para}"
    resp = requests.get(url)
    respostalimpra = resp.json()
    chave = f"{de}{para}"
    x = float(respostalimpra[chave]["bid"])
    resultado = x * valor

    return {"Resultadooo": resultado}



