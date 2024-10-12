from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from src.router.routerExcel.router import create_route_everything_excel
from src.caseUse.ExcelProcessing.caseUseExcel import caseUseExcel
from src.controller.ExcelProcessing.controller import Controller_Excel_Processing


from src.router.routerJson.router import create_route_everything_json
from src.caseUse.JsonProcessing.caseUseJson import caseUseJson
from src.controller.JsonProcessing.controller import Controller_Json_Processing

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

# Excel
caseUseExcelInstance = caseUseExcel()
controllerExcel = Controller_Excel_Processing(caseUseExcelInstance)
app.include_router(create_route_everything_excel(controllerExcel))

# JSON
caseUseJsonInstance = caseUseJson()
controllerJson = Controller_Json_Processing(caseUseJsonInstance)
app.include_router(create_route_everything_json(controllerJson))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app",host='0.0.0.0',port=8000, reload=True)
