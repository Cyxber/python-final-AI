def menu_options(menu_items: dict[str, str], category: str) -> list[str]:
    return [
        item.strip()
        for item in menu_items.get(category, "").split(",")
        if item.strip()
    ]
