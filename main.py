from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from data import elements

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "elements": elements}
    )


@app.get("/element/{element_id}", response_class=HTMLResponse)
async def element_page(request: Request, element_id: int):
    element = next((e for e in elements if e["id"] == element_id), None)
    return templates.TemplateResponse(
        "element.html",
        {"request": request, "element": element}
    )
@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    query = q.lower()

    results = [
        el for el in elements
        if query in el["name"].lower() or query in el["symbol"].lower()
    ]

    return templates.TemplateResponse(
        "search_results.html",
        {"request": request, "results": results, "q": q}
    )
