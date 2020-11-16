def stringfy(list_items, separator):
    list_stringfied = ''

    for index in range(len(list_items)):
        if index == (len(list_items) -1):
            list_stringfied += f'{list_items[index]}'
            return list_stringfied
        list_stringfied += f'{list_items[index]} {separator} '

    return list_stringfied