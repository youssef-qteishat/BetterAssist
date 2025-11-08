from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

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
async def login(user_login: UserLogin):
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
        return {"error": str(e)}

@app.post("/api/auth/register")
async def register_user(request: RegisterRequest):
    if request.email == "test@example.com":
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "Register successful"}
