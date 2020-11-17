import flask.testing

def stringfy(items_list, separator):
    list_stringfied = ''

    for index in range(len(items_list)):
        if index == (len(items_list) -1):
            list_stringfied += f'{items_list[index].lower()}'
            return list_stringfied
        list_stringfied += f'{items_list[index].lower()} {separator} '

    return list_stringfied