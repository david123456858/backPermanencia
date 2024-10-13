from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from datetime import datetime


## El self es para utilizar los atributos globales de la clas
class Controller_Excel_Processing:
    def __init__(self,caseUseExcel)->None:
        self.caseUseExcel = caseUseExcel
        
    async def post_file_excel(self,file:UploadFile):
        try:
            if not file:
                return HTTPException(status_code=400,detail=" Faltan argumentos ")
            print('Estoy en el controllador')
            result = await self.caseUseExcel.post_file_excel(file)
            
            nombre_archivo_csv = f"archivo_convertido_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            return StreamingResponse(result, media_type="text/csv", headers={"Content-Disposition": f"attachment; filename={nombre_archivo_csv}"})
        
        except Exception as error:
            raise HTTPException(status_code=500,detail=f"internal error server {str(error)}")
          
        