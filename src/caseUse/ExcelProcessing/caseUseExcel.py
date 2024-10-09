from fastapi import UploadFile
import io
import pandas as pd

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
        except  Exception as error:
            print(error)
            raise Exception('Error the reading file Excel')  

        