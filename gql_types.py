from datetime import datetime
from typing import List, Optional

import strawberry
from strawberry import ID


@strawberry.interface
class Node:
    id: ID


@strawberry.input
class StrFilterLookup:
    exact: Optional[str] = None
    contains: Optional[str] = None
    in_list: Optional[List[str]] = None
    starts_with: Optional[str] = None
    ends_with: Optional[str] = None


@strawberry.input
class ItemFilter:
    name: Optional[StrFilterLookup] = None
    sku: Optional[StrFilterLookup] = None


@strawberry.type
class ItemType(Node):
    id: ID
    name: str
    barcode: str
    cost: float
    markup: float
    creationDate: datetime
    is_active: bool
    current_stock: float
    is_service: bool
    sku: str
    price: float
