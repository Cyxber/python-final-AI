def menu_options(menu_items: dict[str, str], category: str) -> list[str]:
    return [
        item.strip()
        for item in menu_items.get(category, "").split(",")
        if item.strip()
    ]


def recommend_outfit(
    menu_items: dict[str, str], preferred_color: str, preferred_size: str
) -> dict[str, str] | None:
    tops = menu_options(menu_items, "TOPS")
    colors = menu_options(menu_items, "COLORS")
    graphics = menu_options(menu_items, "GRAPHICS")
    sizes = menu_options(menu_items, "SIZES")

    color = next(
        (item for item in colors if item.casefold() == preferred_color.casefold()),
        None,
    )
    size = next(
        (item for item in sizes if item.casefold() == preferred_size.casefold()),
        None,
    )
    if not tops or not graphics or color is None or size is None:
        return None

    return {
        "top": tops[0],
        "color": color,
        "graphic": graphics[0],
        "size": size,
    }
