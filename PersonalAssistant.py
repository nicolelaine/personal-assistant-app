class PersonalAssistant:

  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays 

  def add_birthday(self, name, date):
    if name in self.birthdays:
      print("Birthday already in list!")
    else:
      self.birthdays[name] = date
      print(f"Added {name}'s birthday {date} to list!")

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      print(f"Removed {name}'s birthday!")

    else:
      print("Birthday not in list, can't remove!")

  def get_birthday(self, name):
    if name in self.birthdays:
      print(f"{name}'s birthday is {self.birthdays[name]}")
    else:
      print("Can't find a birthday for this person...")

  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"

  def get_contacts(self):
    return self.contacts

 
#assistant.add_todo("Pick up groceries")
#assistant.add_todo("Buy food for the doggo")
#print(assistant.get_contact("Chelsea"))
#print(assistant.get_todos())
#print(assistant.get_birthday("Jenn"))
