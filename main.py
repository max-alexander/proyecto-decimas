from functions import *
import os, sys, time
os.system("cls")

menu1 = menu()
if menu1 == "1":
    name,number,email = add_contacts()