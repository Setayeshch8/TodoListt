todo_list = []



def  add_task():
   task = input("Enter a task: ")
   todo_list.append({"Task": task, "status": "pending"})
   print("New Task added Successfully!\n")


def view_task():
   print("Your Todo List: ")
   if len(todo_list) == 0:
      print("no pending taks.")
   else:
      for index, task in enumerate(todo_list, 1):
         print(f"{index}: {task['Task']} - {task['status']}")
         print("\n")


def remove_task():
   if len(todo_list) == 0:
      print("List is empty!")
   else:
     try: 
        search_index = int(input("enter the task nnumber u want to remove")) - 1
        if 0  <= search_index < len(todo_list):
          removed_task = todo_list.pop(search_index)
          print(f"Task Removed: {removed_task['Task']}")
        else:
         print("Invalid Task Number")
     except ValueError:
      print("please enter a valid task nmber")

def mark_done():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("enter the task number that you want to mark as complete ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked done.")
            else:
                print("Invalid Task Number")
        except ValueError:
            print("please enter a valid task number")




def menu():
    while(True):
      print("*** main menu***")
      print("1.add new task")
      print("2. view all tasks")
      print("3.remove a task")
      print("4. mark a task as completed")
      print("5. exit")

      choice  = input("enter your choice: ")
      if choice == "1":
         add_task()
      elif choice == "2":
         view_task()
      elif choice == "3":
         remove_task()
      elif choice == "4":
         mark_done()
      elif choice == "5":
         print("exiting the application...")
         exit()
      else:
          print("Invalid choice! Try again")
         
menu()