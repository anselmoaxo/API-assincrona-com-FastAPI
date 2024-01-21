from fastapi import FastAPI
import uvicorn

app = FastAPI(title='WorkKoutApi')

@app.get('/')  
def read_root():  
    return {'message': 'Olá Mundo!'} 

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, log_level='info', reload=True)
