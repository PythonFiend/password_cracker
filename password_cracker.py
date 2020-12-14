import string
import re
import getpass
from random import randint
import time
import PySimpleGUI as sg 
import sys

col1 = [[sg.Image('lock2.png', pad=(30,0))]]
col2 = [[sg.Image('key2.png', pad=(20,0))]]

sg.theme('SystemDefault')
layout = [[sg.Text("Password Cracker", pad=(70,0), size=(15,1), font='Arial 16')],
          [sg.Column(col1), sg.Column(col2)],
          [sg.InputText( pad=(20,0), size=(10,2), password_char='*', key='INPUT', font='Arial 16'), sg.Text(size=(10,1), background_color='white',key='OUTPUT', font='Arial 16')],
          [sg.Button("Crack!", font='Arial 14', pad=(20,0)), sg.Button("Exit", font='Arial 14')]]

window = sg.Window("Password Cracker", layout)

alphabet = list(string.ascii_letters)
numbers = [n for n in range(0,10)]
special = list(string.punctuation)
joint = alphabet + numbers + special

guess_pwd = ''
while True:
    event,values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        exit()
    elif event == "Crack!":

        user_pwd = (values['INPUT'])
        fail = 'Not found!'
        wait = "Wait..."
        sg.popup_auto_close("Wait...", font="Arial 18")
        window['OUTPUT'].update(wait)

        try:
            while (guess_pwd != user_pwd):
                for chars in range(len(user_pwd)):
                    guess_char = joint[randint(0,93)]
                    guess_pwd = str(guess_char) + str(guess_pwd)
                print('\r', guess_pwd, end='')
            print("Your password is", guess_pwd)
        except KeyboardInterrupt:
            print('\n\n[-] Detected CTRL + C...Quitting...')
            
            if guess_pwd == user_pwd:
                print('\n',r)
                window['OUTPUT'].update(r, text_color='green')
                break
            if guess_pwd != user_pwd:
                window['OUTPUT'].update(fail, text_color='red')




# alphabet = list(string.ascii_letters)
# numbers = [n for n in range(0,10)]
# special = list(string.punctuation)
# joint = alphabet + numbers + special

# user_pwd = getpass.getpass(prompt="Enter password: ")
# guess_pwd = ''

# try:
#     while (guess_pwd != user_pwd):
#         for chars in range(len(user_pwd)):
#             guess_char = alphabet[randint(0,12)]
#             guess_pwd = str(guess_char) + str(guess_pwd)
#         print('\r', guess_pwd, end='')
#     print("Your password is", guess_pwd)
# except KeyboardInterrupt:
#     print('\n\n[-] Detected CTRL + C...Quitting...')



# guess = ""
# while (guess != user_pass):
#     guess = ""

#     for letter in range(len(user_pass)):
#         guess_letter = password[randint(0, 25)]
#         guess = str(guess_letter) + str(guess)
  
#     print('\r',guess,end='')
    

# print("Your password is",guess)