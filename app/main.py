from fastapi import FastAPI, APIRouter
from routers.user import router as user_router
from typing import Union
from pydantic import BaseModel

router = APIRouter()
router.include_router(
    user_router,
    prefix='/users',
    tags=['users']
)

app = FastAPI()
app.include_router(router)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
