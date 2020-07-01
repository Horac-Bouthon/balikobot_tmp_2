import uvicorn
from conf.settings import HOST, PORT

if __name__ == "__main__":
    uvicorn.run("main:app", host=HOST, port=int(PORT), reload=True, debug=True, workers=1)
