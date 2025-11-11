from typing import Union
from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent.agent import agent
from starlette.responses import JSONResponse
from supabase_init import supabase
from utils import ingest_articulation_pdf  # your ingestion pipeline function

app = FastAPI()

class Query(BaseModel):
    query: str

class UserLoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    firstName: str
    lastName: str
    email: str
    password: str

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Handle user authentication
@app.post("/api/auth/login")
async def login(user_login: UserLoginRequest):
    try:
        print("Logging with email:", user_login.email)
        response = supabase.auth.sign_in_with_password(
            {
                "email": user_login.email,
                "password": user_login.password,
            }
        )
        return {"user": response.user.dict(), "session": response.session.dict()}
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@app.post("/query")
async def run_agent(query: Query):
    try:
        result = agent.run(query.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):
    try:
        # Save the uploaded PDF to a temporary location (or a configured directory)
        contents = await file.read()
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)

        # Call your ingestion pipeline on the saved file
        vectordb = ingest_articulation_pdf(temp_path)

        return JSONResponse(content={"message": f"Successfully ingested {file.filename}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")

@app.post("/api/auth/register")
async def register_user(register_request: RegisterRequest):
    try:
        response = supabase.auth.sign_up(
            {
                "email": register_request.email,
                "password": register_request.password,
                "options": {
                    "email_redirect_to": "http://localhost:8080/",
                    "data": {
                        "first_name": register_request.firstName,
                        "last_name": register_request.lastName,
                    }
                },
            }
        )
        print("Response:", response)
        return {"user": response.user.dict()}
    except Exception as e:
        print("Exception:", e)
        raise HTTPException(status_code=401, detail=str(e))
