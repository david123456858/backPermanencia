from src.config.router.routerConfig import getRouteBase
from src.controller.ExcelProcessing.controller import Controller_Excel_Processing

from fastapi import APIRouter,UploadFile,File

BASE_URL = getRouteBase()

router = APIRouter()

def create_route_everything_excel(controller_excel):
    @router.get(BASE_URL,tags=['excel_router'])  #tags para la documentacion 
    async def getExcelRead():
        return {'data':'Enrutado en funcionamiento'}
    
    @router.post(f"{BASE_URL}/file",tags=['excel_router'])## ruta para convertir el excel
    async def postFileExcelConvert(file:UploadFile = File()):
            print('Pase por las rutas')
            return await controller_excel.post_file_excel(file)
            
    return router
    
    

