import uvicorn
from scripts.config import service_data

if __name__ == "__main__":
    uvicorn.run("course:app", reload=True,host=service_data.host, port = service_data.port)
