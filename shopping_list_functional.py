import os
import re
from enum import Enum

class Exit_Command(Enum):
    exit = "exit"
    ex = "ex"
    q = "q"
    quit = "quit"
    

shopping_list : list = list()
shopping_list_item_counter = list()
stock = dict()

veg = open("vegetables.txt", "r") 
fruits = open("fruit's.txt", "r")
supermarket = open("supermarket.txt","r")

list_of_vegetables = veg.readlines()
list_of_fruits = fruits.readlines()
list_of_supermarket_ware = supermarket.readlines()


def show_help():
    """ """
    print(">> enter quit to exit the program and see your list << \n")
    print(">> You can use edit, show, find and remove keyword's << \n")


def purify_names(shopping_list):
    regex_of_numbers = r'[0-9]'
    just_name : list = list()
    for items_of_list in shopping_list:
        items_of_list = re.sub(regex_of_numbers,'',items_of_list)
        items_of_list = items_of_list.replace("by","")
        items_of_list = items_of_list.replace("kg","")
        items_of_list = items_of_list.replace("each","")
        just_name.append(items_of_list.strip())
    return just_name    


def purify_prices(shopping_list):
    regex_of_numbers = r'[a-z]'
    just_num : list = list()
    for items_of_list in shopping_list:
        items_of_list = re.sub(regex_of_numbers,'',items_of_list)
        items_of_list = items_of_list.replace("by","")
        items_of_list = items_of_list.replace("kg","")
        items_of_list = items_of_list.replace("each","")
        just_num.append(items_of_list.strip())
    return just_num       


def categorize():
        category_choice = input("which category ? vegetables/fruits/supermarket").casefold().strip()
        if category_choice == "vegetables" :
            purify_names(list_of_vegetables)
        elif category_choice == "fruits" :
            purify_names(list_of_fruits)
        elif category_choice == "supermarket":
            purify_names(list_of_supermarket_ware)     
        else:
            print("Your category has not been found ‼❗‼❗‼❗‼")


def generate_products_dict():
    counter : int = 0
    for num in range(len(list_of_vegetables)):
        stock[purify_names(list_of_vegetables)[counter]] = purify_prices(list_of_vegetables)[counter]
        counter += 1
    counter = 0

    for num in range(len(list_of_fruits)):
        stock[purify_names(list_of_fruits)[counter]] = purify_prices(list_of_fruits)[counter]
        counter += 1 

    counter = 0
    for num in range(len(list_of_supermarket_ware)):
        stock[purify_names(list_of_supermarket_ware)[counter]] = purify_prices(list_of_supermarket_ware)[counter]
        counter += 1
    return stock
generate_products_dict()


def sales_invoice(shopping_list,shopping_list_item_counter):
    total_price :int = 0
    for item in shopping_list:
        count_of_item = shopping_list_item_counter.count(item)
        print(f"| {item} | price : {stock.get(item)} | count : {count_of_item} |")
        total_price +=  count_of_item*int(stock[item])
    print(f"total price is : {total_price}")


def beautify_item(shopping_list):
    """

    Parameters
    ----------
     item : fetch an item to make it more pretty and show it


    Returns
    -------


    """
    
    number = 1
    print("item's :")
    print("\n")
    for itemFinder in shopping_list:
        print(f"> {number}. {itemFinder}")
        number += 1
    print("\n")


def count(shopping_list):
    print(f"length of your list: {len(shopping_list)}")


def add_item(shopping_list, item_to_add):
    """

    Parameters
    ----------
    list :  considered list you want to add something to it

    item :  considered item you want to add it to list


    Returns
    -------

    """
    shopping_list.append(item_to_add)


def drop_item(shopping_list, item_to_drop):
    """

    Parameters
    ----------
    list : considered list you want to remove something from it

    item : considered item you want to add it to list


    Returns
    -------

    """
    if item_to_drop not in shopping_list:
        print("Item doesn't exit")

    shopping_list.remove(item_to_drop)


def clear_screen():
    """ clear the screen by cls command"""
    return os.system('cls')


def find_element(shopping_list, item_to_find):
    """

    Parameters
    ----------
    list : shopping list 

    item : the item user want to find 


    Returns
    -------

    """
    if item_to_find in shopping_list:
        print("\n \/ item has been found \/")
        print(f"number of element is > {shopping_list.index(item_to_find) + 1} <")
    else:
        print("item doesn't exist")

# this is for any item in the list to change
def edit_item(shopping_list, item_to_edit):
    if item_to_edit in shopping_list:
        index_of_item = shopping_list.index(item_to_edit)
        item_to_change = input("enter the new value :")
        shopping_list[index_of_item] = item_to_change
    else:
        print("item doesn't exist")


def change_priority(shopping_list, item_to_change_its_place,index_of_item):
    if item_to_change_its_place in shopping_list:
        shopping_list.remove(item_to_change_its_place)
        index_of_item -= 1
        shopping_list.insert(index_of_item, item_to_change_its_place)

    else:
        print("item doesn't exist")        


def show_menu():
    print("Menu :")
    print("0] show your list and exit the program")
    print("1] see your shopping cart ")
    print("2] see  your count of item in shopping list ")
    print("3] remove an item from your list ")
    print("4] search for your item and show it's place ")
    print("5] edit your item ")
    print("6] prioritize your item's ")
    print("7] show product's by category ")
    print("8] add item to your shopping list ")
    print("9]show menu")
    print("10]sales invoice")
show_menu()


while True:
    # fetching the value from user
    user_choice = input(" \n enter your choice from menu: ").lower().strip()
    clear_screen()
    if user_choice == "0":
        # showing the final list
        beautify_item(shopping_list)
        print('^ This is your final list ^')
        break
    # show for showing user list
    elif user_choice == '1':
        beautify_item(shopping_list)
    # count for length of user list
    elif user_choice == '2':
        count(shopping_list)
        # help for helpful command's
    elif user_choice == 'help':
        show_help()
    # remove for removing any element
    elif user_choice == '3':
        item_to_remove = input('please enter the item you want to remove')
        drop_item(shopping_list, item_to_remove)
        beautify_item(shopping_list)
        print("item removed")
    # find for finding element's in list
    elif user_choice == '4':
        item_to_find = input('enter your element to start searching: ')
        find_element(shopping_list, item_to_find)
    # edit for editing element's in the list
    elif user_choice == '5':
        beautify_item(shopping_list)
        item_to_edit = input("which item do you wanna edit :").strip().lower()
        edit_item(shopping_list, item_to_edit)

    elif user_choice == '6':
        beautify_item(shopping_list)
        print("> change your item's place's <")
        item_to_change_place = input("enter your item : ")
        where_to_place = int(input("where ?"))
        change_priority(shopping_list, item_to_change_place, where_to_place)
    elif user_choice == "7":
        category_choice = input("which category ? vegetables/fruits/supermarket : ").casefold().strip()
        if category_choice == "vegetables" :
            print(*purify_names(list_of_vegetables))
        elif category_choice == "fruits" :
            print(*purify_names(list_of_fruits))
        elif category_choice == "supermarket":
            print(*purify_names(list_of_supermarket_ware))
        else:
            print("Your category has not been found ‼❗‼❗‼❗‼")
    elif user_choice == '8':
            esc = False
            print("\n you can press exit,ex to exit the adding section ")
            while True:
                item_existence = False
                item_to_add = input("write your item to add : ").strip().casefold()
                for command in Exit_Command:
                    if item_to_add == command.value:
                        esc = True
                if esc == True:
                    break
                for item in stock:
                    if item.strip() == item_to_add:
                        if item_to_add in shopping_list:
                            add_item(shopping_list_item_counter,item_to_add)
                            item_existence = True
                        else:
                            add_item(shopping_list, item_to_add)
                            add_item(shopping_list_item_counter,item_to_add)
                            print(f"> {item_to_add} < added to list")
                            print(f"You have {len(shopping_list)} item's in list")
                            item_existence = True
                if item_existence == False:
                    print("item doesn't exist in the stock !")
    elif user_choice == '9':
        show_menu()
    elif user_choice == '10':
        sales_invoice(shopping_list,shopping_list_item_counter)
    else:
        print("Your choice should be something between 0 and 10")
