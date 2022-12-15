import argparse
import pickle
from tabulate import tabulate
from datetime import datetime
import uuid
from os import path
import sys
from operator import itemgetter
from myfunctions import *
from myclasses import *
"""
This is the main module
"""

def main():

    """All the real work that drives the program!"""
    parser = argparse.ArgumentParser(description = "Update your ToDo list.")

    group = parser.add_mutually_exclusive_group(required = True) ##mutually_exclusive is added because user can only pass
    #one of the following inputs at once.
    group.add_argument("--add", type = str, help = "a task string to add to your list")
    group.add_argument("--delete", type = str, help = "the id of the task you want to delete")
    group.add_argument("--report", action = "store_true", required = False, help = "List all tasks including both completed and incomplete tasks")
    group.add_argument("--list", action = "store_true", required=False, help = "list all tasks that have not been completed")
    group.add_argument("--query", type = str, required=False, nargs = "+", help = "priority of task; default value is 1")
    group.add_argument("--done", type = str, help = "marking the task that matches the input id as completed")

    #the 2 below should be allowed for mutual use for -add
    parser.add_argument("--due", type = str, required = False, help = "due date in dd/MM/YYYY format")
    parser.add_argument("--priority", type = int, required = False, default = 1, help = "priority of task; default value is 1")

    #Parse the argument
    args = parser.parse_args()

    #create instances of Tasks
    task_list = Tasks()

    #Read out arguments (note the types)

    if args.add:
        print("We need to add {} to our todo list with a priority of {}.".format(args.add, args.priority))
        x = conversion(args)
        task_list.add(x) #pass the right things

    elif args.delete:
        print("Delete task with unique ID")
        x = get_id_delete(args)
        task_list.delete(x)

    elif args.report:
        print("These are all the tasks including complete and incomplete ones.")
        task_list.report()

    elif args.list:
        print("These are all the tasks in my Tasks() object! Except for the task that are done.")
        task_list.list()
    
    elif args.query:
        print("These are all the tasks with the search-words.")
        
        x = query_parse(args)
        task_list.query(x)

    elif args.done:
        x = get_id_done(args)
        task_list.done(x)


    task_list.pickle_tasks() #save it back to disk
    exit()

if __name__ == "__main__":
    main()
