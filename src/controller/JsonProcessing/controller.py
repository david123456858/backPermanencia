import os
from fastapi import UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from datetime import datetime

class Controller_Json_Processing:
    def __init__(self, caseUseJson) -> None:
        self.caseUseJson = caseUseJson

    async def post_file_json(self, file: UploadFile):
        try:
            result_json = await self.caseUseJson.post_file_json(file)
            
            nombre_archivo_json = f"archivo_convertido_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            return JSONResponse(content=result_json, headers={"Content-Disposition": f"inline; filename={nombre_archivo_json}"})
        
        except Exception as error:
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(error)}")

   