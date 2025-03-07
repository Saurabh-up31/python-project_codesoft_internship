contacts = {}

while True:
    print("\nContact Book project by Saurabh kumar ")
    print("1. Add contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search Contact")
    print("6. Count Contact")
    print("7. Exit")
    
    choice = input("Enter the choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        if name in contacts:
            print(f'Contect name {name} already exists!')
        else:
            age = input('Enter the age: ')
            email = input('Enter the email: ')
            mobile = input('Enter the mobile: ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print('Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contect name to view= ')
        if name in contacts:    
            contact = contacts[name]
            print(f'Name: {name}, Age:{age}, Mobile number:{mobile}, Email:{email}')
        else:
            print('Contact not found')

    elif choice == '3':
        name  = input('Enter name to update contact: ')
        if name in contacts:
            age = input('Enter updated age: ')
            email = input('Enter updated email: ')
            mobile = input('Enter updated mobile number : ')
            contacts[name] = {'age':int(age), 'email':email, 'mobil':mobile}
        else :
            print("contact not found")

    elif choice == '4':
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contect name {name} has been deleted successfully')
        else :
            print('Contect not found')

    elif choice =='5':
        search_name = input('Enter contact name to search!')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found-Name {name}, Age:{age},Mobile number:{mobile}, Email:{email}')
                found = True
            if not found:
                print('No contact found with that name')

    elif choice == '6':
        print(f'Total contacts in your book : {len(contacts)}')

    elif choice == '7':
        print('Thank You Far Using Contact Book')
        break
    
    else:
        print('Enter the valid number 1 to 7 ')
