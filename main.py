from fastapi import FastAPI
from apis import router

app = FastAPI()

# 包含路由
app.include_router(
    router
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API service"}