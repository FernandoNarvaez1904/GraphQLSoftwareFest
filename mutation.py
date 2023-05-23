from typing import Optional, List

import strawberry
from strawberry import ID

from gql_types import ItemFilter, ItemType
from models import Item, populate_items
from utils import get_filter_arg_from_filter_input


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def populate_items_with_count(self, count: int) -> List[ItemType]:
        await populate_items(count)
        items = await Item.all().values()
        return [ItemType(**item) for item in items]

    @strawberry.mutation
    async def item_delete(self, id: ID) -> ItemType:
        item = await Item.get(id=id).values()
        item_type = ItemType(**item)
        temp = await Item.get(id=id)
        await temp.delete()
        return item_type
