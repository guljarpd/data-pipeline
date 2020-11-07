from fastapi import FastAPI
from app.api.routes.read_file import read_and_save
from app.api.routes.apis import router
from app.models.db import database

# 
app = FastAPI()

# 
@app.on_event("startup")
async def startup():
  # db connection
  await database.connect()
  # read file
  await read_and_save()


@app.on_event("shutdown")
async def shutdown():
  # close connection here.
  await database.disconnect()


@app.get('/')
def root():
  return '{"status": "Ok"}'


app.include_router(router, prefix="/api/v1")


def _main():
  from uvicorn import run
  run(app)

if __name__ == "__main__":
    _main()