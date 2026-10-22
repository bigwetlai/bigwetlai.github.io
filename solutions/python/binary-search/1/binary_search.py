def find(search_list, value):
    index = 0
    while search_list:
        lenth = len(search_list)
        if value == search_list[lenth//2]:
            index += lenth//2
            return index
            
        if value < search_list[lenth//2]:
            search_list = search_list[:lenth//2]
            continue
            
        if value > search_list[lenth//2]:
            search_list = search_list[ lenth//2 + 1 : ]
            index += lenth//2 + 1

    raise ValueError("value not in array")
