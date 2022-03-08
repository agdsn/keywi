import uvicorn

from lib.app_config import app_config

if __name__ == '__main__':
    uvicorn.run("api:root_app",
                host='0.0.0.0',
                forwarded_allow_ips='*',
                port=6080,
                reload=app_config.getboolean('general', 'debug'),
                workers=app_config.getint('general', 'workers'))
