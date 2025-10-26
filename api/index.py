from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def instant():
    return {"message": "Hello, World!"}

@app.get("/api/{path:path}")
async def api_handler(path: str):
    return {"path": path}

# Vercel requires this handler
handler = Mangum(app)
