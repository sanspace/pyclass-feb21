from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

class Developer(BaseModel):
    id: int
    name: str
    pythonista: Optional[bool]
    skills: List[str]

app = FastAPI()

data = {}

@app.get('/')
def read_root():
    return {'message': 'hi'}

@app.get('/developers')
def get_developers():
    return data

@app.get('/developers/{developer_id}')
def get_developer(developer_id: int):
    # return data[developer_id]
    try:
        dev = data[developer_id]
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Dev with ID {developer_id} not found")
    return dev

@app.post('/developers')
def add_developer(developer: Developer):
    developer_id = developer.id
    data[developer_id] = developer
    return developer

@app.delete('/developers/{developer_id}')
def delete_developer(developer_id: int):
    dev = data[developer_id]
    del data[developer_id]
    return dev




