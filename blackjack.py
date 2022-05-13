from tkinter import *
import random
root = Tk()
root.title("BlacJack")
root.geometry("300x250")
 
def  igra():
    ruka = 0
    dealer = 0
    rating = 0
    while True:
        while ruka <= 17:
            ruka += random.randrange(1, 7, 1)
            dealer += random.randrange(1, 7, 1)
        if ruka < 22 and dealer > 21 or dealer < ruka:
            print("Вы победили!")
            rating += 1
        elif ruka == dealer:
            print("Ничья!")
        else:
            print("Вы проиграли!")
            rating -= 1
        print("Ваши очки", ruka, "Очки диллера", dealer, "Ваш рейтинг", rating)
        break

btn = Button(text="Играть", command=igra)
btn.pack()
root.mainloop()
