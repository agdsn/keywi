import uvicorn

if __name__ == '__main__':
    uvicorn.run("api:app",
                host='0.0.0.0',
                port=6080,
                reload=True,
                workers=2)
