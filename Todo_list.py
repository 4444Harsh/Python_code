task=[]
print("To Do List Manager:")
def printlist():
  print()
  for item in task:
    print(item)
  print()
while True:
  menu=input("Do you want to view, add, edit, or remove an item from the to do list?")
  if menu=="view":
    printlist()
  elif menu=="add":
    item=input("What do you want to add?")
    task.append(item)
  elif menu=="remove":
    item=input("What do you want to remove?")
    if item in task:
      task.remove(item)
    else:
      print(f"{item} was not in the list")
  elif menu=="edit":
    item=input("What do you want to edit?")
    new=input("What do you want to change it to?")
    for i in range(0,len(task)):
      if task[i]==item:
        task[i]=new

  elif menu=="delete":
    task=[]
