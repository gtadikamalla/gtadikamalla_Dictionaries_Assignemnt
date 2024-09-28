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
    
        if item['id'][0] not in ['D']:
            item['stock'] = random.randint(25, 50)


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
            print('D for decription change')
            choice=input('Enter A or R or C or D:')
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
                item_id = input('Enter id to remove:')
                if any(item['id'] == item_id for item in menu_list):
                    for item in menu_list:
                        if item['id'] == item_id:
                            menu_list.remove(item)
                            break
                    print(f'{item_id} is removed from menu.')
                else:
                    print(f'{item_id} Item ID is not in the menu list.')

            elif choice in 'dD':
                item_id = input('Enter id for dish name change:')
                if any(item['id'] == item_id for item in menu_list):
                    dish=input('Enter the dish name:')
                    for item in menu_list:
                        if item['id'] == item_id:
                            item['dish']=dish
                            break
                    print(f'{dish} is updated to {item_id} menu.')
                else:
                    print(f'{item_id} Item ID is not in the menu list.')
       

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
        print(menu_list)
        order=input('Enter your quantity and dish name (eg: 30 burger):')
        quantity, dish_name=order.split()
        quantity=int(quantity)
        for item in menu_list:
            if dish_name.upper() in item['dish'].upper():
                if quantity<=item['stock']:
                    print(f'Your order {quantity}{dish_name} is Success')
                else:
                    print(f'{dish_name} is Out of stock')
                break
            else:
                print(f'{dish_name} is not in menu list.')
            


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