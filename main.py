import requests
from fastapi import FastAPI
app = FastAPI()


@app.get("/converter")
def converter(valor: float, de: str, para: str):
    url = f"https://economia.awesomeapi.com.br/last/{de}-{para}"
    if valor <=0:
        return {"erro": "Voce colocou um valor errado, digite novamente!"}
    try:
        resp = requests.get(url)
        respostalimpra = resp.json()
        chave = f"{de}{para}"
        x = float(respostalimpra[chave]["bid"])
        resultado = x * valor
        resultadof = round(resultado, 2)
    except Exception as e:
        return {"erro": "Voce colocou algo errado, confira e atualize novamente"}
    return {"resultado": resultadof}



