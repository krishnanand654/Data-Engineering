import time

print(f"\n{'-'*5}Welcome to the demo Marketplace{'-'*5}\n")

#login db
user_db={'username':'user','password':'user@pass123'}
admin_db={'username':'admin','password':'root'}

#global session storage
current_session_id = None
user = None

#user login
def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == user_db['username'] and password == user_db['password']:
        print(f"\n{'*'*5}Login successful as user{'*'*5}\n")
        global current_session_id 
        current_session_id = generate_session_id()
        global user
        user = 'user'
        return True
    else:
        print("\n--login failed--\n")

#admin login
def admin_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == admin_db['username'] and password == admin_db['password']:
        print(f"\n{'*'*5}Login successful as admin{'*'*5}\n")
        global current_session_id 
        current_session_id = generate_session_id()
        global user
        user = 'admin'
        return True
    else:
        print("\n--login failed--\n")

def generate_session_id():
    return "12345"

#login menu
def login():
    while True:
        print(f"\n{'-'*5}Login{'-'*5}\n")
        print("1. User Login\n2. Admin Login\n3. Exit application\n")
        ch = input("Enter your choice: ")
        if ch == '1':
            status = user_login()
            if status == True:
                break
        elif ch == '2':
            status = admin_login()
            if status == True:
                user="admin"
                break
        elif ch == '3':
            print("\nExiting application...\n")
            break
        else:
            print("Invalid choice!")

#Catelogs
catalog = [
    {'id':'101', 'name':'Puma', 'category':'Boots', 'price':10000},
    {'id':'102', 'name':'Reymond', 'category':'Coats', 'price':15000},
    {'id':'103', 'name':'H&M', 'category':'Jackets', 'price':6000},
    {'id':'104', 'name':'Urban Monkey', 'category':'Caps', 'price':5000},
    ]

def display_catalog():
    print(f"\n{'Item id':<10}|\t{'Name':<14}|\t{'Category':<10}|\tPrice")
    print('-'*50)
    for item in catalog:
        print(f"{item['id']:<10}|\t{item['name']:<14}|\t{item['category']:<10}|\t{item['price']}")

#Cart Functionality
cart=[]

def display_cart():
    print(f"\n{'Item id':<10}|\t{'Name':<14}|\t{'Category':<10}|\t{'Price':<10}|\t{'Quantity':<10}|\tTotal Price")
    print('-'*90)
    if len(cart)>0:
        for item in cart:
            print(f"{item['id']:<10}|\t{item['name']:<14}|\t{item['category']:<10}|\t{item['price']:<10}|\t{item['quantity']:<10}|\t{item['price']*item['quantity']}")
    else:
        print("No items in cart")
    pass

def add_to_cart(session_id, product_id, quantity):
    if current_session_id == session_id:
       
        #if item already in cart
        for item in cart:
            if item['id'] == product_id:
                item['quantity'] += quantity    
                return
            
       #if item not already in cart
        for item in catalog:
            if item['id'] == product_id:
                user_item = item
                user_item['quantity'] = quantity
                cart.append(user_item)
        print(f"\n{'-'*5}Item added to cart successfully{'-'*5}\n")
    else:
        print("Session expired Login Again")

def delete_from_cart(session_id, product_id):
    if current_session_id == session_id:
        for item in cart:
            if item['id'] == product_id:
                cart.remove(item)
        print(f"\n{'-'*5}Item removed from cart successfully{'-'*5}\n")
    else:
        print("Session expired Login Again")
    


def get_total():
    total = 0
    for item in cart:
        total += (item['price'] * item['quantity'])
    return total

#Payment Gateway service
def checkout():
    if len(cart)<=0:
        print("\nYour cart is empty!\n")
        return
    while True:
        print(f"\n{'*'*5}CHECKOUT{'*'*5}\n")
        print("\n1. UPI\n2. Net Banking\n3. COD\n4. Cancel")
        ch = int(input("Select payment method: "))

        if ch == 1:
            print("\nTotal Amount: ",get_total())
            upi_id = input("\nEnter UPI Id: ")
            print("\nUPI payment process initiated\n")
            print("Processing",end=" ")
            for i in range(10):
                time.sleep(0.5)
                print('.', end=" ", flush=True)
            print(f"\n\n{'*'*5}UPI payment is successfully{'*'*5}\n")
            break
        elif ch == 2:
            while True:
                #handling if user type string instead of integer
                try:
                    card_no = int(input("Enter card number: "))
                    cvv = int(input("Enter the CVV number: "))
                    fullName = input("Enter Card owners name: ")
                    print("\nNetbanking payment process initiated\n")
                    print("Processing",end=" ")
                    for i in range(10):
                        time.sleep(0.5)
                        print('.', end=" ", flush=True)
                    print(f"\n\n{'*'*5}Payment is successfully{'*'*5}\n")
                    break
                except ValueError as e:
                    print("Only number are allowed!")
            break
        elif ch == 3:
            print("\nOrder Placed successfully!\nPayment will be done by cash on hand\n")
            break
        elif ch == 4:
            print(f"\n{'-'*5}Exiting payment gateway{'-'*5}\n")
            break
        else:
            print("Invalid option")


#ADMIN functionalities
#add product
def add_products_to_catalog():
    id = input("Enter id: ")
    for item in catalog:
        if item['id'] == id:
            print(f"\n{'-'*4}Item with id {id} Already exist{'-'*4}\n")
            return
        else:
            name = input("Enter name: ")
            category = input("Enter category: ")
            while True:
                try:
                    price = int(input("Enter price: "))
                    catalog.append({"id":id, "name": name, "category":category, "price":price})
                    print(f"\n{'*'*5}Item added successsfully{'*'*5}\n")
                    return True
                except ValueError as e:
                    print(f"\n{'-'*5}Invalid price format{'-'*5}\n")
#update product
def update_product():
    product_id = input("Enter product id: ")
    found= False
    for item in catalog:
        if item['id'] == product_id:
            found = True
    if found:
        for item in catalog:
            if item['id'] == product_id:
                name=input("Enter Item name: ")
                category = input("Enter item category: ")
                while True:
                    try:
                        price = int(input("Enter item price: "))
                        item['name'] = name
                        item['category'] = category
                        item['price'] = price
                        print(f"\n{'-'*5}Product updated successfully{'-'*5}\n")
                        return
                    except ValueError as e:
                        print("invalid format")

if __name__ == "__main__":
    login()

#User menu
if user == 'user':
    while True:
        print(f"\n{'*'*5}Menu{'*'*5}\n")
        print("1. Add to cart\n2. View Cart\n3. Delete the Cart\n4. Checkout\n5. Log out")
        ch = input("Enter your choice: ")
        if ch == '1':
            product_id = input("Enter product_id: ")
             #if item already in cart
            found = False
            for item in catalog:
                if item['id'] == product_id:
                    found = True
            if found == False:
                print(f"\n{'-'*5}Product not found{'-'*5}\n")
            else:
                quantity = int(input("Enter the quantity: "))
                if add_to_cart(current_session_id, product_id,  quantity):
                    break
        elif ch == '2':
            display_cart()
        elif ch == '3':
            product_id = input("Enter product_id: ")
            delete_from_cart(current_session_id, product_id)
        elif ch == '4':
            checkout()
        elif ch == '5':
            print("\nLogging out...\n")
            current_session_id = None
            login()
        else:
            print("Invalid Choice")

#Admin menu
if user == 'admin':
    while True:
        print(f"{'-'*5}MENU{'-'*5}")
        print("\n1. Add new product\n2. View Catalog\n3. Update a product\n4. Log out\n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            add_products_to_catalog()
        elif ch == 2:
            display_catalog()
        elif ch == 3:
            update_product()
        elif ch == 4:
            print("\nLogging out...\n")
            login()
        else:
            print("Invalid choice")
        
        




