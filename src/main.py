from fastapi import FastAPI

app = FastAPI(title="Project template")


@app.get("/")
def root() -> str:
    return "Hello World"
