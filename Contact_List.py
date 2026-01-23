contacts =[]

def add_contact():
  phone = int(input("Enter phone number : "))

  if phone <= 0:
    print("Invalid phone number.")
    return
  for c in contacts:
    if c["phone"] == phone:
      print("Contact already exist.")
      return
    
  name = input("Enter name : ")
  email = input("Enter email : ")
  address = input("Enter adderss : ")

  contact = {
    "name":name,
    "phone":phone,
    "email":email,
    "address":address
  }
  contacts.append(contact)
  print("Contact added successfully.")


def view_contact():
  if not contacts:
    print("Contact record not found.")
    return
  for c in contacts:
    print("----------")
    print("Name :",c["name"])
    print("Phone :",c["phone"])
    print("Email :",c["email"])
    print("Address :",c["address"])
    print("----------")


def search_contact():
  phone = int(input("Enter phone number : "))
  for c in contacts:
    if c["phone"] == phone:
      print("Contact found:")
      print(c)
      return
  print("Contact not found.")

def update_contact():
  phone = int(input("Enter phone number :"))
  for c in contacts:
    if c["phone"] == phone:
      c["name"] =  input("enter new name :")
      c["email"] = input("enter new email :")
      c["address"] = input("enter new address :")
      print("Contact updated successfully.")
      return
  print("Contact not found.")

def delete_contact():
  phone = int(input("enter phone number :"))
  for c in contacts:
    if c["phone"] == phone:
      contacts.remove(c)
      print("Contact deleted successfully.")
      return
  print("Contact not found.")

while True:
  print("\n--- Contact List Application ---")
  print("1.Add Contract")
  print("2.View All Contacts")
  print("3.Search Contact")
  print("4.Update Contact ")
  print("5.delete contact")
  print("6.Exit")
  
  choice = input("Enter your choice: ")

  if choice == "1":
    add_contact()
  elif choice == "2":
     view_contact()
  elif choice == "3":
        search_contact()
  elif choice == "4":
        update_contact()
  elif choice == "5":
        delete_contact()
  elif choice == "6":
        print("Exiting program. Thank you.")
        break
  else:
        print("Invalid choice. Try again.")