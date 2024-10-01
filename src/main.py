from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/")
def readRoot():
    return{"data":"YA ESTA"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("/src/main:app",host='0.0.0.0',port=8000, reload=True)