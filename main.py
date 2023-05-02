from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
import os
app = FastAPI()

url=os.environ.get('MONGO_URL')
client = AsyncIOMotorClient(url)
db = client["task_management"]
tasks_collection = db["tasks"]

# Task model
class Task(BaseModel):
    id: str = None
    title: str
    description: str
    assignee: str = None
    priority: int = 1
    due_date: str = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/check")
def check():
    return {"Hello": "World"}

# Create a task
@app.post("/tasks")
async def create_task(task: Task):
    task_data = task.dict()
    task_data["_id"] = ObjectId()
    await tasks_collection.insert_one(task_data)
    return {"id": str(task_data["_id"])}

# Get all tasks
@app.get("/tasks")
async def get_all_tasks():
    tasks = []
    async for task in tasks_collection.find():
        task["id"] = str(task["_id"])
        del task["_id"]
        tasks.append(task)
    return tasks

# Get a task by ID
@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = await tasks_collection.find_one({"_id": ObjectId(task_id)})
    if task:
        task["id"] = str(task["_id"])
        del task["_id"]
        return task
    else:
        return {"error": "Task not found"}

# Update a task
@app.put("/tasks/{task_id}")
async def update_task(task_id: str, updated_task: Task):
    await tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": updated_task.dict()})
    return {"status": "Task updated"}

# Delete a task
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    await tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return {"status": "Task deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
