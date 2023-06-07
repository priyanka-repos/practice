import uvicorn
from fastapi import FastAPI
from scripts.config import service_data
from course import data_router
from scripts.constants.app_constants import CommonConstants
app = FastAPI()
app.include_router(data_router)
if __name__ == "__main__":
    uvicorn.run(app=CommonConstants.APP_KEY,host=service_data.host, port = service_data.port,reload=True)
