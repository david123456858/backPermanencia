from fastapi import UploadFile
import io
import pandas as pd
import numpy as np

class caseUseExcel:
    
   async def post_file_excel(self,file:UploadFile):
        try:
            if(file.filename.endswith('.xlsx')):
                content_excel = pd.read_excel(file.file)
                
                print(content_excel)
                
                buffer = io.StringIO()
                content_excel.to_csv(buffer,index=False)
                buffer.seek(0) ##
                
                return buffer
        except :
            raise Exception('Error the reading file Excel')
        
   async def post_excel_porcentage(self,file:UploadFile):
       try:
           if(file.filename.endswith('.xlsx')):
               
               content = pd.read_excel(file.file)
               print(content)
               for columna in content.columns:
                    content[columna] = pd.to_numeric(content[columna], errors='coerce')
               
               porcentage ={}
               
               for columns in content.columns:
                   total = content[columns].sum()
                   if(total > 0):
                       porcentage[columns] = (content[columns] / total * 100).tolist()
                   else:
                       porcentage[columns] = [0] * len(content[columns]) 
                         
               for key in porcentage:
                    porcentage[key] = [0 if np.isnan(x) else x for x in porcentage[key]]       
           return porcentage           
       except Exception as error:
           print(error)
           raise Exception('Error the read in the file excel')     