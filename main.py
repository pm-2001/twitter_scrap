from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse 
from fastapi import Request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/twitterfetch/")
async def read_index(request: Request):
    return FileResponse('static/index.html')