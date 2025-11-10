from typing import Union
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from agent.agent import agent
from starlette.responses import JSONResponse
from utils import ingest_articulation_pdf  # your ingestion pipeline function

app = FastAPI()

class Query(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/query")
async def run_agent(query: Query):
    try:
        result = agent.run(query.query)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ingest")
async def ingest_pdf(file: UploadFile = File(...)):
    try:
        # Save the uploaded PDF to a temporary location (or a configured directory)
        contents = await file.read()
        temp_path = f"/tmp/{file.filename}"
        with open(temp_path, "wb") as f:
            f.write(contents)

        # Call your ingestion pipeline on the saved file
        vectordb = ingest_articulation_pdf(temp_path)

        return JSONResponse(content={"message": f"Successfully ingested {file.filename}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")
