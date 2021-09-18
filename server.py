from functools import lru_cache
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import aiofiles

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


#@lru_cache
def read_html(filename):
    file_path = f"static/{filename}"
    with open(file_path, mode="r") as file:
        content = file.read()
    return content


@app.get("/", response_class=HTMLResponse)
async def index():
    content = read_html("index.html")
    return content
