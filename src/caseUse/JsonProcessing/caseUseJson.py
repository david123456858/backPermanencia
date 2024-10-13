from fastapi import UploadFile, HTTPException
import pandas as pd

from src.model.JsonModel import columns

class caseUseJson:

    def separar_nombres_apellidos(self, nombre_completo):
        partes = nombre_completo.split()

        nombre_1 = ""
        nombre_2 = ""
        apellido_1 = ""
        apellido_2 = ""

        preposiciones = ["DE", "DEL", "LAS", "LOS", "LA"]

        if len(partes) == 1:
            nombre_1 = partes[0]
        elif len(partes) == 3:
            nombre_1 = partes[0]
            apellido_1 = partes[1]
            apellido_2 = partes[2]
        else:
            nombre_1 = partes[0]
            i = 1
            while i < len(partes) - 2:  
                if partes[i].upper() in preposiciones:
                    nombre_2 = partes[i] + " " + partes[i + 1]  
                    i += 2
                    break
                else:
                    nombre_2 = partes[i]
                    i += 1

            apellido_1 = " ".join(partes[i:len(partes) - 1])  
            apellido_2 = partes[-1] 

        return nombre_1, nombre_2, apellido_1, apellido_2

    async def post_file_json(self, file: UploadFile):
        try:
            if not file.filename.endswith('.xlsx'):
                raise HTTPException(status_code=400, detail="El archivo no tiene formato Excel (.xlsx)")
            content_excel = pd.read_excel(file.file,sheet_name="BD")

            if content_excel.empty:
                raise HTTPException(status_code=400, detail="El archivo Excel está vacío")

            nombres_apellidos = content_excel['NOMBRE Y APELLIDO'].apply(self.separar_nombres_apellidos)
            content_excel[['NOMBRE1', 'NOMBRE2', 'APELLIDO1', 'APELLIDO2']] = pd.DataFrame(nombres_apellidos.tolist(), index=content_excel.index)


            content_excel.drop(columns=['NOMBRE Y APELLIDO'], inplace=True)

            for column in content_excel.select_dtypes(include=['datetime64', 'datetime']):
                content_excel[column] = content_excel[column].astype(str)

            content_excel.fillna("", inplace=True)

            json_result = content_excel[columns]
            json_result = json_result.to_dict(orient="records")
            return json_result
        
        except Exception as error:
            print(f"Error al procesar el archivo: {error}")
            raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(error)}")
