from fastapi import UploadFile
import io
import pandas as pd
import numpy as np

class caseUseExcel:
    
   async def post_file_excel(self,file:UploadFile):
        try:
            if(file.filename.endswith('.xlsx')):
                content_excel = pd.read_excel(file.file,sheet_name="BD")
                print(content_excel)
                
                if 'NOMBRE Y APELLIDO' in content_excel.columns:
                    nombres_apellidos = content_excel['NOMBRE Y APELLIDO'].str.split(' ', n=3, expand=True)
                    content_excel['NOMBRE1'] = nombres_apellidos[0] 
                    content_excel['NOMBRE2'] = nombres_apellidos[1]  
                    content_excel['APELLIDO1'] = nombres_apellidos[2]  
                    content_excel['APELLIDO2'] = nombres_apellidos[3]  
                    
                    content_excel['NOMBRE2'] = content_excel['NOMBRE2'].fillna('')
                    content_excel['APELLIDO2'] = content_excel['APELLIDO2'].fillna('')
                    
  
                    content_excel.drop(columns=['NOMBRE Y APELLIDO'], inplace=True)

                buffer = io.StringIO()
                content_excel.to_csv(buffer,index=False)
                buffer.seek(0)  

                return buffer
        except Exception as e:
            print(e)
            raise Exception('Error the read in the file excel')     

