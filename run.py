import uvicorn
from balikobot_connector.conf.settings import PORT

if __name__ == "__main__":
    uvicorn.run("balikobot_connector.main:app", host='0.0.0.0', port=int(PORT), reload=True, debug=True, workers=1)
