from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def root():
  return '{"status": "Ok"}'


def _main():
  from uvicorn import run
  run(app)

if __name__ == "__main__":
    _main()