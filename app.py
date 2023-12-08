from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from function import createForm

app = FastAPI(debug=True)
app.mount("/static/", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def temp(request: Request):
    return templates.TemplateResponse("temp.html", {"request": request})


@app.get("/z", response_class=HTMLResponse)
async def z(request: Request):
    return templates.TemplateResponse("z.html", {"request": request})


@app.post("/grace")
async def grace(
    year: int = Form(...),
    month: int = Form(...),
    day: int = Form(...),
    hour: int = Form(...),
):
    result = createForm(year, month, day, hour)
    return result
