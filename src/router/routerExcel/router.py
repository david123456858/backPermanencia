from src.config.router.routerConfig import getRouteBase
from fastapi import APIRouter

BASE_URL = getRouteBase()

router = APIRouter()

def create_route_everything_excel():
    @router.get(BASE_URL,tags=['excel_router'])  #tags para la documentacion 
    async def getExcelRead():
        return {'data':'Enrutado en funcionamiento'}
    
    return router
    
    

