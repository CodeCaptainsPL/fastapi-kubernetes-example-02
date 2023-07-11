from fastapi import FastAPI

from employee.api import router

app = FastAPI()
app.include_router(router=router)
