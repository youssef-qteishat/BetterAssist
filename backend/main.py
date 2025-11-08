from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

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
def login():
    print("Login successful")
    return {"message": "Login successful"}

class RegisterRequest(BaseModel):
    email: str
    password: str

@app.post("/api/auth/register")
async def register_user(request: RegisterRequest):
    if request.email == "test@example.com":
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "Register successful"}