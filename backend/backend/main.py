from fastapi import FastAPI, UploadFile
from credit_model import calculate_credit_score
from cam_generator import generate_cam
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Intelli Credit AI Running"}

@app.post("/analyze")
async def analyze_company(file: UploadFile):

    data = json.load(file.file)

    score = calculate_credit_score(data)

    if score > 70:
        decision = "APPROVED"
        loan = "₹15 Crore"
        rate = "11%"
    else:
        decision = "REJECTED"
        loan = "0"
        rate = "N/A"

    generate_cam(data["company"], score, loan)

    return {
        "company": data["company"],
        "score": score,
        "decision": decision,
        "loan": loan,
        "interest": rate
    }
