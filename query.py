from typing import Optional, List

import strawberry
from strawberry import ID

from gql_types import ItemFilter, ItemType
from models import Item
from utils import get_filter_arg_from_filter_input


@strawberry.type
class Query:

    @strawberry.field
    async def items(self, filter: Optional[ItemFilter] = None) -> List[ItemType]:
        filter_arg = {}
        if filter:
            filter_arg = await get_filter_arg_from_filter_input(filter)

        items = await Item.filter(**filter_arg).values()
        items_type = [ItemType(**item) for item in items]
        return items_type

    @strawberry.field
    async def item(self, id: ID) -> ItemType:
        item = await Item.get(id=id).values()
        item_type = ItemType(**item)
        return item_type

    @strawberry.field()
    async def my_id(self, all_caps: Optional[bool] = False) -> ID:
        my_id_s = "2ou45o3".upper() if all_caps else "2ou45o3"
        return ID(my_id_s)

    @strawberry.field
    async def company_name(self) -> str:
        return "UnleashTech Holdings"
