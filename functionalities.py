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
    print('----------------------------------')
    a=input('Are you a Manager (Y/N)?')
    while True:
        if not a:
           print('----------------------------------------')
           print('Invalid input. Please enter valid input.')
           break
        elif a in 'yY':
            print('----------------------------------------')
            print('A for Add an item')
            print('R for Remove an item')
            print('C for change price')
            print('D for decription change')
            choice=input('Enter A or R or C or D:')
            if not choice:
                print('----------------------------------------')
                print('Invalid input. Please enter valid input.')
            elif choice in 'Aa':
                id_pattern=r"^[A-Za-z][0-9]+$"
                dish_pattern=r"^[A-Za-z]"
                price_pattern=r"^[0-9]+"
                print('----------------------------------------')
                id=valid_input('Enter Item id:',id_pattern).upper()
                if any(item['id'] == id for item in menu_list):
                    print('----------------------------------------')
                    print(f'{id} Item ID is already exists.')
                else:
                    print('----------------------------------------')
                    dish=valid_input('Enter a dish name:', dish_pattern)
                    print('----------------------------------------')
                    price=valid_input('Enter price of an item:', price_pattern)
                    new_item = {'id': id, 'dish': dish, 'price': price}
                    menu_list.append(new_item)
                    print('----------------------------------------')
                    print(new_item,'is added to menu.')
                    stock()

            elif choice in 'Rr':

                print('-----------------------------')
                item_id = input('Enter id to remove:')
                item_id=item_id.upper()
                if any(item['id'] == item_id for item in menu_list):
                    for item in menu_list:
                        if item['id'] == item_id:
                            menu_list.remove(item)
                            break
                    print('--------------------------------')
                    print(f'{item_id} is removed from menu.')
                else:
                    print('-------------------------------------------')
                    print(f'{item_id} Item ID is not in the menu list.')

            elif choice in 'dD':
                print('----------------------------------------')
                item_id = input('Enter id for dish name change:')
                item_id=item_id.upper()
                if any(item['id'] == item_id for item in menu_list):
                    dish_pattern=r"^[A-Za-z]"
                    print('----------------------')
                    dish=valid_input('Enter the dish name:',dish_pattern)
                    for item in menu_list:
                        if item['id'] == item_id:
                            item['dish']=dish
                            break
                    print('----------------------------------------')
                    print(f'{dish} is updated to {item_id} menu.')
                else:
                    print('----------------------------------------')
                    print(f'{item_id} Item ID is not in the menu list.')
       

            elif choice in 'cC':
                print('----------------------------------------')
                item_id = input('Enter id to change price:')
                item_id=item_id.upper()
                if any(item['id'] == item_id for item in menu_list):
                    price_pattern=r"^[0-9]+"
                    print('----------------')
                    item_price = valid_input('Enter price:',price_pattern)
                    for item in menu_list:
                        if item['id'] == item_id:
                            item['price'] = item_price
                            break
                    print('----------------------------------------')
                    print(f'Price updated for {item_id}.')
                else:
                    print('----------------------------------------')
                    print(f'{item_id} Item ID is not in the menu list.')
    
            else:
                print('----------------------------------------')
                print('Invalid input. Please enter valid input.')
            
            print('-------------------------------------------------------------')
            continue_action = input("Do you want to perform another action as a manager (Y/N)? ")
            if continue_action not in 'yY':
                print('-----------------------')
                print("Exiting Manager Access.")
                break

        elif a in 'nN':
            print('--------------')
            print('Thank you....!')
            break
        else:
            print('----------------------------------------')
            print('Invalid input. Please enter valid input.')
            break

                
#print(menu_list)

def valid_input(prompt,pattern=None):
    value=input(prompt).strip()
    while not value or (pattern and not re.match(pattern,value)):
        if not value:
            print('------------------------------------------------')
            print('Input cannot be empty. Please enter valid input.')
        else:
            print('---------------')
            print('Invalid format.')
        value=input(prompt).strip()
    return value



def customerAccess():
    while True:
        print('---------------------')
        print(menu_list)
        print('-------------------------------------------------------------------------------')
        order=input('Enter your quantity and dish name (eg: 30 burger) or Give B to back main menu:')

        if order.lower()=='b':
            print('-----------------------------')
            print("Returning to the main menu...")
            break
        
        
        if not re.match(r'^[0-9]+\s[A-Za-z]+$', order):
            print('-------------------------------------------------------------------------------')
            print("Invalid format! Please enter the order in the format 'Quantity Dish name' (e.g., 30 burger).")
            continue
        quantity, dish_name=order.split()
        quantity=int(quantity)
        item_found=False
        for item in menu_list:
            if dish_name.upper() in item['dish'].upper():
                item_found=True
                if quantity<=item['stock']:
                    print('-----------------------------------------------')
                    print(f'Your order {quantity}  {dish_name} is Success.')
                    item['stock']= item['stock']-quantity
                else:
                    print('----------------------------')
                    print(f'{dish_name} is out of stock')
                break
        
        if not item_found:
            print('---------------------------------')
            print(f'{dish_name} is not in menu list.')
            


convertItems()
stock()
while True:
    print('-----------------------------------------------------------------------------')
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