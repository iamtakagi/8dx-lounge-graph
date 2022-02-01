from graph import create_plotting
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/api/graph")
async def create_graph(baseMmr: int = Query(0), history: str = Query(None)):
    image = create_plotting(baseMmr, [int(mmr) for mmr in history.split(",")])
    return StreamingResponse(content=image, media_type="image/png")
