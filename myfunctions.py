import dateparser

"""
This is the module with extra functions
"""

#reference URL: https://stackoverflow.com/questions/14865961/iterate-through-a-namespace
def conversion(user_input):
    dict_1 = {}
    for key, value  in user_input.__dict__.items():
        if key == "add":
            dict_1[key] = value
        elif key == "due":
            if value == None:
                dict_1[key] = "-"
            else:
                dict_1[key] = dateparser.parse(value, date_formats = ['%m/%d/%y'])
        elif key == "priority":
            if value == None:
                dict_1[key] = 1
            else:
                dict_1[key] = int(value)
    return dict_1

#parsing the query so that we can search with lowercase letters at all times
def query_parse(user_input):
    list_1 = []
    for key,value in user_input.__dict__.items():
        if key == "query":
            list_1 += user_input.__dict__[key]
    list_2 = []
    for el in list_1:
        list_2.append(el.lower())
    
    return list_2

#getting id for the --done
def get_id_done(user_input):
    list_1 = []
    for key,value in user_input.__dict__.items():
        if key == "done":
            list_1.append(user_input.__dict__[key]) 
    return list_1

#getting id for the --delete (I made separate functions because the code kept on crashing for some reason :(   )
def get_id_delete(user_input):
    list_1 = []
    for key,value in user_input.__dict__.items():
        if key == "delete":
            list_1.append(user_input.__dict__[key])
    return list_1

