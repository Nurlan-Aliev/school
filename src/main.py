from fastapi import FastAPI
from .auth.view import router as auth_router
from .user.view import router as user_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(user_router)
