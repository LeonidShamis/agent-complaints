from pathlib import Path

from fastapi import FastAPI, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from models import Complaint, complaints

app = FastAPI(title="AgentClinic")
templates = Jinja2Templates(directory=Path(__file__).parent / "templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/complaints")
async def complaints_page(request: Request):
    return templates.TemplateResponse("complaints.html", {"request": request, "complaints": complaints})


@app.post("/complaints")
async def add_complaint(agent_name: str = Form(...), text: str = Form(...)):
    complaints.append(Complaint(agent_name=agent_name, text=text))
    return RedirectResponse(url="/complaints", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, reload=True)
