import models
import views
from urls import get_url
from models import load_data
from colorama import Fore, Style, Back


def welcome():
    user = str(input("Please enter your name : "))
    print(Fore.LIGHTMAGENTA_EX + f"""
                Welcome to our website, {user}!

    Our entire program is divided into 2 sections :

        -> Section 1 : It is the mandatory section of the project.
                       and is related to data-preprocessing.
        -> Section 2 : It is other section of the project in which analysis is performed.
                       It shows the trends and patterns present in your data.""")
    print(Style.RESET_ALL, end='')


def stages():
    print(Fore.LIGHTBLUE_EX + f"""
          
    There are 3 mandatory steps in the program that you have to perform.
    Then there are other optional steps to proceed further.""")

    print(f"""
    The 3 mandatory stages of the program are : 
        1 -> Handling null or missing values.
        2 -> Dealing with outliers.
        3 -> Data formatting.
    """)

    print("    If you miss any of the mandatory steps project might not work properly.")
    print(Style.RESET_ALL, end='')


def mandatory_steps():
    print(Fore.RED + f"""
    Run step 1 of Handling missing values.
    Run step 2 of Dealing with outliers
          """)
    print(Style.RESET_ALL, end='')


def optional_steps():
    print(Fore.GREEN + f"""
            Analysis of Relationship between different inputs columns are - 
          
    Press 3 to show relationship between speed and price
    Press 4 to show relationship between Touch and price
    Press 5 to show relationship between Battery and price
    Press 6 to show relationship between Backlit and price
    Press 7 to show relationship between Graphic and price
    Press 0 to exit 
    
    
    """)
    print(Style.RESET_ALL, end='')


def main():
    print('Home URL : ', get_url('home'))
    welcome()
    stages()
    df = models.load_data()
    mandatory_steps()
    choice = int(input("Enter 1 to Handling missing values : "))
    if choice == 1:
        print('Home URL : ', get_url('handling_missing_values'))
        df = views.handling_missing_values(df)
    else:
        print("Invalid Input!")

    choice = int(input("Enter 2 to Handle Outlier values : "))
    if choice == 2:
        print('Home URL : ', get_url('set_outliers'))
        df = views.set_outliers(df)
    else:
        print("Invalid Input!")

    df.to_csv("filtered.csv")
    check = True
    while check:
        optional_steps()
        choice = int(input("Enter Your choice : "))
        if choice == 3:
            print('Home URL : ', get_url('speed_v_price'))
            views.speed_v_price(df)
        elif choice == 4:
            print('Home URL : ', get_url('touch_v_price'))
            views.touch_v_price(df)
        elif choice == 5:
            print('Home URL : ', get_url('battery_v_price'))
            views.battery_v_price(df)
        elif choice == 6:
            print('Home URL : ', get_url('backlit_v_price'))
            views.backlit_v_price(df)
        elif choice == 7:
            print('Home URL : ', get_url('graphic_v_price'))
            views.graphic_v_price(df)
        elif choice == 0:
            print("Thank you !")
            check = False
        else:
            print("Invalid Input !")
    
main()