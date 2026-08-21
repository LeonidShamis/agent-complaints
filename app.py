import uvicorn
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from models import Complaint, complaints

app = FastAPI(title="AgentClinic")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/complaints", response_class=HTMLResponse)
def list_complaints(request: Request):
    return templates.TemplateResponse("complaints.html", {"request": request, "complaints": complaints})


@app.post("/complaints", response_class=HTMLResponse)
def add_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
