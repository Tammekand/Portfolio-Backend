from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/items/{item}", responses={200: {"description": "Item found"}, 451: {"description": "Unavailable for Legal Reasons"}})
async def read_root(item: str):
    if item == "teapot":
        raise HTTPException(status_code=451, detail="You are a Teapot", headers={"X-Error": "Who is a Teapot?"})
    return {"msg": f"Hello {item}!"}