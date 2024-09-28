import data
import random
import re

menu_list=[]

def convertItems():
    global menu_list

    for i in data.menu_items:
        item_code, item_name, price=i.split()
        #print(item_code)
        # print(item_name)
        # print(quantity)
        menu_dic={'id':item_code, 'dish':item_name,'price':int(price)}
        menu_list.append(menu_dic)
        for item in menu_list:
            item['dish']=item['dish'].replace('\u200b','')

   # print(menu_list)
    
   

def stock():
    for item in menu_list:
    # Check if the item ID starts with 'A', 'S', 'E', or 'T' (indicating it's a non-drink item)
        if item['id'][0] not in ['D']:
            item['stock'] = random.randint(25, 50)

# Print the updated menu list with stock values assigned
    #print(menu_list)


def managerAccess():
    a=input('Are you a Manager (Y/N)?')
    while True:
        if not a:
           print('Invalid input. Please enter valid input.')
        elif a in 'yY':
            print('A for Add an item')
            print('R for Remove an item')
            print('C for change price')
            choice=input('Enter A or R or C:')
            if not choice:
                print('Invalid input. Please enter valid input.')
            elif choice in 'Aa':
                id_pattern=r"^[A-Za-z][0-9]+$"
                dish_pattern=r"^[A-Za-z]"
                price_pattern=r"^[0-9]+"
                id=valid_input('Enter Item id:',id_pattern).upper()
                if any(item['id'] == id for item in menu_list):
                    print('This Item ID is already exists.')
                else:
                    dish=valid_input('Enter a dish name:', dish_pattern)
                    price=valid_input('Enter price of an item:', price_pattern)
                    new_item = {'id': id, 'dish': dish, 'price': price}
                    menu_list.append(new_item)
                    print(new_item,'is added to menu.')
                    stock()

            elif choice in 'Rr':
                id=input('Enter id to remove:')
                for items in menu_list:
                    if id==items['id']:
                        menu_list.remove(items)
                        print(f'{id} is removed from menu.')
                    

            elif choice in 'cC':
                item_id = input('Enter id to change price:')
                if any(item['id'] == item_id for item in menu_list):
                    item_price = input('Enter price:')
                    for item in menu_list:
                        if item['id'] == item_id:
                            item['price'] = item_price
                            break
                    print(f'Price updated for {item_id}.')
                else:
                    print(f'{item_id} Item ID is not in the menu list.')
    
            else:
                print('Invalid input. Please enter valid input.')
            
            continue_action = input("Do you want to perform another action as a manager (Y/N)? ")
            if continue_action not in 'yY':
                print("Exiting Manager Access.")
                break

        elif a in 'nN':
            break
        else:
            print('Invalid input. Please enter valid input.')
            break

                
#print(menu_list)

def valid_input(prompt,pattern=None):
    value=input(prompt).strip()
    while not value or (pattern and not re.match(pattern,value)):
        if not value:
            print('Input cannot be empty. Please enter valid input.')
        else:
            print('Invalid format.')
        value=input(prompt).strip()
    return value



def customerAccess():
    while True:
        order=input('Enter your quantity and dish name:')
        print(menu_list)


convertItems()
stock()
while True:
    print('Menu is converted into list of dictionary and stock added to non-drink items.')
    print('-----------------------------------------------------------------------------')
    print(menu_list)
    print('__________________________')
    print('C for coustmer access.')
    print('M for manager access.')
    print('Q for quit.')
    access=input('Enter your choice (C/M/Q):')
    if access in 'qQ':
        break
    elif access in 'Mm':
        managerAccess()
    elif access in 'cC':
        customerAccess()
    else:
        print('-----------------------------------------')
        print('Invalid input. Please enter valid input.')
        print('-----------------------------------------')