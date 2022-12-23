from tkinter import *
import time
import random

root = Tk()
root.title("Finance Fun")
root.geometry("800x800")
ipadding = {'ipadx': 10, 'ipady': 10}

price = 50
money = 1000
shares = 0

def startGame(event):
    c.config(width = 1, height = 1)
    updatePrice()

def updatePrice():
    global price
    price = price + int((random.randint(price * -1, 100 - price)) / 4)
    p.config(text = "Current share price: $" + str(price))
    p.after(1000, updatePrice)

def buy():
    global shares
    global money
    if money >= price:
        shares += 1
        money = money - price
        m.config(text = "Money: $" + str(money))
        sh.config(text = "Shares: " + str(shares))
        if money >= 1500:
            win()

def sell():
    global shares
    global money
    if shares >= 1:
        shares -= 1
        money = money + price
        m.config(text = "Money: $" + str(money))
        sh.config(text = "Shares: " + str(shares))
        if money >= 1500:
            win()

def win():
    c.delete("all")
    c.config(width = 800, height = 800)
    c.create_text(400, 400, text = "Congrats you win!", font = ('Helvetica', 25))
    c.pack()


c = Canvas(root, width = 800, height = 800, bg = "grey")
c.create_text(400, 350, text = "The goal is to get to $1500", font = ('Helvetica', 25))
c.create_text(400, 400, text = "Press enter to start!", font = ('Helvetica', 25))
c.create_text(400, 700, text = "Game created by tater tot the bot", font = ('Helvetica', 25))
c.pack()

m = Label(root, text = "Money: $" + str(money), font = ('Helvetica', 20))
m.pack(ipady = 15, side = TOP, anchor = 'w')

sh = Label(root, text = "Shares: " + str(shares), font = ('Helvetica', 20))
sh.pack(ipady = 15, side = TOP, anchor = 'w')

sh = Label(root, text = "Try to get to $1500", font = ('Helvetica', 20))
sh.pack(ipady = 15, side = TOP, anchor = 'w')

p = Label(root, text = "Current stock price: $" + str(price), font = ('Helvetica', 20))
p.pack(ipady = 15, fill = Y, anchor = 'center')

b = Button(root, bg = "green", text = "Buy", width = 5, height = 2, font = ('Helvetica', 20), command = buy)
b.pack(side = LEFT, padx = 10, pady = 10, fill = X, expand = True, anchor = 's')

s = Button(root, bg = "red", text = "Sell", width = 5, height = 2, font = ('Helvetica', 20), command = sell)
s.pack(side = RIGHT, padx = 10, pady = 10, fill = X, expand = True, anchor = 's')

root.bind('<Return>', startGame)
root.mainloop()
