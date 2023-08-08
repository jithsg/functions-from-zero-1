from fastapi import FastAPI
from mylib.calc import add, sub, mul, div, sqrt
import uvicorn

app = FastAPI()

@app.get("/add")
def add_endpoint(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/sub")
def sub_endpoint(a: float, b: float):
    return {"result": sub(a, b)}

@app.get("/mul")
def mul_endpoint(a: float, b: float):
    return {"result": mul(a, b)}

@app.get("/div")
def div_endpoint(a: float, b: float):
    return {"result": div(a, b)}

@app.get("/sqrt")
def sqrt_endpoint(a: float):
    return {"result": sqrt(a)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)