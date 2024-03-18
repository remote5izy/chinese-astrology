from fastapi import FastAPI, Form
from pydantic import BaseModel
from models import db


app = FastAPI(debug=True)


class EditData(BaseModel):
    id: str
    name: str
    content: str


class DeleteData(BaseModel):
    id: str


@app.post("/create")
async def create_a_new_data(data:EditData):
    item = {"id": data.id, "name": data.name, "content": data.content}
    db.table.insert_one(item)
    return {"message": "Data inserted successfully"}


@app.post("/edit")
async def edit_data(data: EditData):
    return {"message": "Data inserted successfully"}


@app.get("/getall")
async def get_all_data():
    data_list = [
        EditData(id="1", name="Name1", content="Content1"),
        EditData(id="2", name="Name2", content="Content2"),
        EditData(id="3", name="Name3", content="Content3"),
    ]
    return data_list


@app.post("/delete")
async def delete_data(a: DeleteData):
    print(a)
    return "u"
