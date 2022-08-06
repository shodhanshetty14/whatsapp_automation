from turtle import title
import pyautogui
from time import sleep
import webbrowser

flag = True
webbrowser.open('https://web.whatsapp.com')


def Spam(message):
    count = 0
    ask = pyautogui.confirm(text='Do you want to Spam the message?', title='Do you want to send multiple times?',buttons=['Yes', 'No'],)
    if ask == 'Yes':
        number = pyautogui.prompt(text='How many times would u like to repeat the message?', title='Number of repeats')
        while count!= int(number):
            write_msg(message)
            count = count + 1
    else:
        write_msg(message)

def search_name():
    # searching the search bar and searching   
    sleep(3)
    name = pyautogui.prompt(text='Whom would you like to send the message?', title='Reciever name')
    sleep(2)
    try:
        x, y =pyautogui.locateCenterOnScreen("search.png", confidence = 0.9)
    except:
        pyautogui.click(204,264,1,button="left")
    # x, y =pyautogui.locateCenterOnScreen("search.png")
    message = pyautogui.prompt(text=f"What Message would you like to send to {name}?", title='Message')
    sleep(2)
    try:
        pyautogui.click(x, y)
    except:
        pyautogui.click(204,264,1,button="left")
    pyautogui.write(name)
    pyautogui.press('enter')
    Spam(message)


def write_msg(message):    
    # writing the message and sending
    pyautogui.write(message)
    pyautogui.press('enter')




sleep(4)    
opt = pyautogui.alert(text="After Scanning the QR press ok, If already logged in then ignore this.", title="ALERT!!")
search_name()

while flag==True:
    nxt_msg = pyautogui.confirm(text='Would you like to send message to anyone else?',title='New Reciever', buttons=['Yes', 'No'])
    if nxt_msg == 'Yes':
        search_name()
    else:
        flag = False
        # quit()