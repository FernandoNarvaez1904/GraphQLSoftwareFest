from gql_types import StrFilterLookup

lookup_name_conversion_map = {
    "i_exact": "iexact",
    "i_contains": "icontains",
    "in_list": "in",
    "starts_with": "startswith",
    "i_starts_with": "istartswith",
    "ends_with": "endswith",
    "i_ends_with": "iendswith",
    "is_null": "isnull",
    "i_regex": "iregex",
}


async def get_filter_arg_from_lookup(lookup: StrFilterLookup, prefix: str = "") -> dict:
    result = {}

    for name, val in lookup.__dict__.items():
        if val:
            if name == "exact":
                result.update({f"{prefix}": val})
                continue

            if prefix:
                if name in lookup_name_conversion_map.keys():
                    name = f"__{lookup_name_conversion_map[name]}"
                else:
                    name = f"__{name}"
            result.update({f"{prefix}{name}": val})

    return result


async def get_filter_arg_from_filter_input(filter, prefix: str = "") -> dict:
    filter_result = {}

    for name, value in filter.__dict__.items():

        if not value:
            continue

        if prefix:
            name = f"{prefix}__{name}"

        value_is_lookup = isinstance(value, StrFilterLookup)
        if value_is_lookup:
            result = await get_filter_arg_from_lookup(lookup=value, prefix=name)
            filter_result.update(result)
            continue

        # If value is a simple exact filter
        filter_result.update({f"{name}": value})

    return filter_result
