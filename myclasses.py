import uuid
from datetime import datetime
import pickle
from os import path
from tabulate import tabulate

"""
This is the module with both classes
"""

class Task:
    """Representation of a task
  
  Attributes:
              - created - date
              - completed - date
              - name - string
              - unique id - number
              - priority - int value of 1, 2, or 3; 1 is default
              - due date - date, this is optional
  """
    
    def __init__(self, name, priority = 1, due_date = None, completed = None):
        self.name = name
        self.priority = priority
        self.completed = completed #optional. #boolean values maybe?? If it has a value => complete
        self.due_date = due_date #optional #premises look weird.. according to final walkthru => solved using dateparser
        #dateparser
        self.unique_id = uuid.uuid4() ##just try UUID
        self.created = datetime.now() #datetime.now-ish. change to strftime("%a %b %d %H: %M: %S %Z %Y") later on

    def id(self):
        return self.unique_id



class Tasks:

    """A list of `Task` objects."""
   
    def __init__(self):
        """Read pickled tasks file into a list"""
        # List of Task objects
        self.tasks = [] 
        if path.isfile('.todo.pickle') == True:
            f = open('.todo.pickle', 'rb')
            data = pickle.load(f)

            f.close()

            for item in data:
                self.tasks.append(item)

        else:
            f = open('.todo.pickle', 'wb')

            f.close()
        # your code here

    def pickle_tasks(self):
        """Pickle task list to a file"""
        # your code here

        with open('.todo.pickle', 'wb') as f:
            pickle.dump(self.tasks, f)


    # Complete the rest of the methods, change the method definitions as needed
    def list(self):
        new_list = []
        #append the things I want to new_list from self.tasks depending on the headers
        for el in self.tasks:
            if el.completed == None or el.completed == "-":
                input_list = [el.unique_id, datetime.now()-el.created, el.due_date, el.priority, el.name]
                new_list.append(input_list)

#below is procdure to sort by due date (if due date exists) and by priority if due date doesnt exist
#or due date is the same
        list_1 = []
        list_2 = []  
        for el in new_list:
            if el[2] == '-' or el[2] == None:
                list_1.append(el)
            else:
                list_2.append(el)

        sorted_list_1 = sorted(list_1, key = lambda element: (element[3]), reverse = True)
        sorted_list_2 = sorted(list_2, key = lambda element: (element[2],element[3]), reverse = True)

        sorted_list_2 += sorted_list_1

        for el in sorted_list_2:
            #print(type(el[1]))
            if type(el[1]) != str:
                el[1] = "{}d".format(el[1].days)

            if type(el[2]) != str:
                el[2] = el[2].strftime("%-m/%-d/%Y")

        print(tabulate(sorted_list_2, headers = ["ID","Age","Due Date", "Priority", "Task"]))

    def report(self):
        new_list = []
        #append the things I want to new_list from self.tasks depending on the headers
        for el in self.tasks:
            if el.completed == None:
                el.completed = "-"

        for el in self.tasks:        
            input_list = [el.unique_id, datetime.now()-el.created,el.due_date,el.priority, el.name, el.created.astimezone().strftime("%a %b %-d %H:%M:%S %Z %Y"), el.completed] #

            new_list.append(input_list)

        list_1 = []
        list_2 = []  
        for el in new_list:
            if el[2] == '-' or el[2] == None:
                list_1.append(el)
            else:
                list_2.append(el)

        sorted_list_1 = sorted(list_1, key = lambda element: (element[3]), reverse = True)
        sorted_list_2 = sorted(list_2, key = lambda element: (element[2],element[3]), reverse = True)

        sorted_list_2 += sorted_list_1

        for el in sorted_list_2:

            el[1] = "{}d".format(el[1].days)

            if type(el[2]) != str:
                el[2] = el[2].strftime("%-m/%-d/%Y")
            

        print(tabulate(sorted_list_2, headers = ["ID","Age","Due Date", "Priority", "Task", "Created", "Completed"]))


    def done(self, selected_id):
        for x in selected_id:

            for el in self.tasks:
                if el.completed == None or el.completed == "-":
                    if str(el.unique_id) == x:
                        el.completed = datetime.now().astimezone().strftime("%a %b %-d %H:%M:%S %Z %Y")
                        print("Completed task {}".format(x))
        
    def query(self, lowercase_query):

        new_list = []
        #append the things I want to new_list from self.tasks depending on the headers
        for el in self.tasks:
            if el.completed == None or el.completed == "-":
                for query in lowercase_query:
                    if query in el.name.lower():
                        input_list = [el.unique_id, datetime.now()-el.created, el.due_date,el.priority, el.name] #

                        new_list.append(input_list)

        print(tabulate(new_list, headers = ["ID", "Age", "Due Date", "Priority", "Task"])) #

          #age is ? = current open time (at the time of load pickle) - (created time)??

    def add(self,modified_dict):

        t = Task(modified_dict["add"], modified_dict["priority"], modified_dict["due"])

        self.tasks.append(t)
        print("Created task {}".format(t.unique_id))

    def delete(self, selected_id):
        for x in selected_id:

            for el in self.tasks:
                if str(el.unique_id) == x:
                    self.tasks.remove(el)
                    print("Deleted task {}".format(x))



