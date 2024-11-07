from src.config.router.routerConfig import getRouteBase
from src.controller.JsonProcessing.controller import Controller_Json_Processing

from fastapi import APIRouter, UploadFile, File

BASE_URL = getRouteBase()

router = APIRouter()

def create_route_everything_json(controller_json):
    @router.get(BASE_URL, tags=['json_router'])  # Ruta de prueba
    async def getJsonRead():
        return {'data': 'Enrutado JSON en funcionamiento'}
    
    @router.post(f"{BASE_URL}/json-file", tags=['json_router'])  # Ruta para convertir el Excel a JSON
    async def post_file_json(file: UploadFile = File()):
        
        return await controller_json.post_file_json(file)
    
    return router
