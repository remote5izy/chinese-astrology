from fastapi import FastAPI, Request, APIRouter, Form, Depends
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)
app.mount("/static/", StaticFiles(directory="static", html=True), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def temp(request: Request):
    return templates.TemplateResponse("temp.html", {"request": request})

@app.post("/grace")
async def grace(request: Request, year: int = Form(...), month: int = Form(...), day: int = Form(...), hour: int = Form(...)):
    context = {"request": request, "year": year, "month": month, "day": day, "hour": hour}
    print(context)
    return  {"message": "success"}
