from __future__ import print_function
from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from twilio.rest import Client
import time
import sys, os


root = Tk()

root.title("1337 Checkin checker")
#root.geometry("600x400")

codeedimg= ImageTk.PhotoImage(Image.open("Codeed_3_16.png"))
label = tk.Label(root, image=codeedimg)
label.pack()




frame = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame.pack()
tk.Label(master=frame, text="your account SID :   ").pack(side=LEFT)
SID=tk.Entry(frame)
SID.pack(side=RIGHT)

frame1 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame1.pack()
tk.Label(master=frame1, text="your auth Token:      ").pack(side=LEFT)
auth =tk.Entry(frame1)
auth.pack(side=RIGHT)

frame2 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame2.pack()
tk.Label(master=frame2, text="your phone number:  ").pack(side=LEFT)
my_Phone=tk.Entry(frame2)
my_Phone.pack(side=RIGHT)

frame3 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame3.pack()
tk.Label(master=frame3, text="your twilio number:  ").pack(side=LEFT)
twilio_Number=tk.Entry(frame3)
twilio_Number.pack(side=RIGHT)


frame4 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame4.pack()
tk.Label(master=frame4, text="your 1337 email:       ").pack(side=LEFT)
email=tk.Entry(frame4)
email.pack(side=RIGHT)

frame5 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame5.pack()
tk.Label(master=frame5, text="your 1337 password: ").pack(side=LEFT)
password=tk.Entry(frame5)
password.pack(side=RIGHT)

frame6 = tk.Frame(master=root, width=150, height=150, pady=10, padx=20)
frame6.pack()
tk.Label(master=frame6, text="your Message:           ").pack(side=LEFT)
message=tk.Entry(frame6)
message.pack(side=RIGHT)



def sendSMSbytwilio():
    account_sid = SID.get() # Found on Twilio Console Dashboard
    auth_token = auth.get() # Found on Twilio Console Dashboard

    myPhone = my_Phone.get() # Phone number you used to verify your Twilio account
    TwilioNumber = twilio_Number.get() # Phone number given to you by Twilio

    client = Client(account_sid, auth_token)

    client.messages.create(
      to=myPhone,
      from_=TwilioNumber,
      body= message.get())



def start():
    Email = email.get()
    Password = password.get()

    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get('https://candidature.1337.ma/')

    email_Box = driver.find_element_by_xpath("//input[@id='user_email']")
    password_Box = driver.find_element_by_xpath("//input[@id='user_password']")

    email_Box.send_keys(Email)
    password_Box.send_keys(Password)

    connectButton = driver.find_element_by_xpath("//input[@name='commit']")
    connectButton.click()

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    if check_exists_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]"):
    	driver.close()
    	print('please try again, your password or your email is incorrect')
    	exit()


    while True:
        driver.refresh()
        try:
        	driver.find_element_by_xpath("//p[contains(text(),'De nouveaux creneaux ouvriront prochainement. Pour')]")
        except NoSuchElementException:
            sendSMSbytwilio()
            print('SMS is sent')
            break
        time.sleep(10)

start_button = Button(root, text='Run', pady=20, padx=30, command=start)
start_button.pack()
root.mainloop()
