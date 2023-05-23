import strawberry

from fastapi import FastAPI, HTTPException, status
from starlette.responses import RedirectResponse
from strawberry.fastapi import GraphQLRouter
from tortoise.contrib.fastapi import register_tortoise

from mutation import Mutation
from query import Query

schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI()


@app.get("/status/200")
async def status_200():
    return {"message": "Correct Page", "code": 200}


@app.get("/status/300")
async def status_300():
    return RedirectResponse(url="/status/200", status_code=300)


@app.get("/status/500")
async def status_500():
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Status 500")


register_tortoise(
    app,
    db_url="sqlite://:memory:",  # SQLite file name/location
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

app.include_router(graphql_app, prefix="/graphql")
