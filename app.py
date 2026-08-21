from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import RedirectResponse

from models import Complaint, complaints

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/complaints")
def get_complaints(request: Request):
    return templates.TemplateResponse("complaints.html", {"request": request, "complaints": complaints})


@app.post("/complaints")
def post_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaint = Complaint(agent_name=agent_name, text=text)
    complaints.append(complaint)
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
