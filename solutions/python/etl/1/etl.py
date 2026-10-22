def transform(legacy_data):
    injective = {}
    for points, character_list in legacy_data.items():
        for char in character_list:
            injective[char.casefold()] = points

    return injective
