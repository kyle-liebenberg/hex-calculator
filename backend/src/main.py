from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from src.calculator import add_hex, sub_hex, mul_hex, div_hex

app = FastAPI()

# Allow CORS so our local index.html can fetch data without security errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected JSON payload 
class CalcRequest(BaseModel):
    val1: str
    val2: str
    operation: str

@app.post("/calculate")
def calculate(req: CalcRequest):
    try:
        if req.operation == "+":
            return {"result": add_hex(req.val1, req.val2)}
        elif req.operation == "-":
            return {"result": sub_hex(req.val1, req.val2)}
        elif req.operation == "*":
            return {"result": mul_hex(req.val1, req.val2)}
        elif req.operation == "/":
            return {"result": div_hex(req.val1, req.val2)}
        else:
            raise HTTPException(status_code=400, detail="Invalid operation")
    except ValueError as e:
        # If our strict TDD constraints are violated, send the error back 
        raise HTTPException(status_code=400, detail=str(e))
