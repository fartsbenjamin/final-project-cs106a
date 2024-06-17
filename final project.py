from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

def main():
    make_main()

def make_main():
    choice=[0,0,0]
    root = tk.Tk()
    root.geometry('600x600')
    root.resizable(False, False)
    root.title("project")
    #makes add fish button
    fish_button = tk.Button(root, text="add fish", command=lambda: when_fish_clicked(choice, pot_label, text))
    fish_button.pack()
    fish_button.place(x=300, y=80)
    #makes fish image
    fish_img = PhotoImage(file="fish.gif")
    fish_label = tk.Label(root, text="click here", image=fish_img)
    fish_label.pack()
    fish_label.place(x=400, y=0)
    #makes add meat button
    meat_button = tk.Button(root, text="add meat", command=lambda: when_meat_clicked(choice, pot_label, text))
    meat_button.pack()
    meat_button.place(x=300, y=270)
    #makes meat image
    meat_img = PhotoImage(file="meat.gif")
    meat_label = tk.Label(root, text="click here", image=meat_img)
    meat_label.pack()
    meat_label.place(x=400, y=250)
    #makes carrot button
    carrot_button = tk.Button(root, text="add veggie", command=lambda: when_veggie_clicked(choice, pot_label, text))
    carrot_button.pack()
    carrot_button.place(x=300, y=450)
    #makes carrot img
    carrot_img = PhotoImage(file="veggie.gif")
    carrot_label = tk.Label(root, text="click here", image=carrot_img)
    carrot_label.pack()
    carrot_label.place(x=400, y=400)
    #makes cook button
    cook_button = tk.Button(root, text="cook", command=lambda: cook_now(root,choice))
    cook_button.pack()
    cook_button.place(x=50, y=100)
    #makes pot img
    #pot_img = Image.open("pot.gif")
    #resize_pot = pot_img.resize((50,50))
    resize_pot = ImageTk.PhotoImage(file="pot.gif")
    pot_label = tk.Label(root, text="click here", image=resize_pot)
    pot_label.pack()
    pot_label.place(x=0, y=200)
    button_close = tk.Button(
        root,
        text="close window",
        command=root.destroy).pack()
    text = Label(root, text="Fish added: No\n Meat added: No\n Veggie added: No")
    text.pack()
    text.place(x=0, y=400)
    #makes remove fish button
    remove_fish_button = tk.Button(root, text="remove fish", command=lambda: remove_fish(choice, pot_label, text))
    remove_fish_button.pack()
    remove_fish_button.place(x=300, y=150)
    #makes remove meat button
    remove_meat_button = tk.Button(root, text="remove meat", command=lambda: remove_meat(choice, pot_label, text))
    remove_meat_button.pack()
    remove_meat_button.place(x=300, y=350)
    #makes remove veggie button
    remove_veggie_button = tk.Button(root, text="remove veggie", command=lambda: remove_veggie(choice, pot_label, text))
    remove_veggie_button.pack()
    remove_veggie_button.place(x=300, y=520)
    root.mainloop()

def when_fish_clicked(choice, pot_label, fish_text):
    choice[0] = 1
    fish_img = PhotoImage(file="fish.gif")
    pot_label.configure(image=fish_img)
    pot_label.image = fish_img
    shown_text = "Fish added: Yes\n"
    if choice[1] == 1:
        shown_text = shown_text + "Meat added: Yes"
    else: 
        shown_text = shown_text + "Meat added: No"
    if choice[2] == 1:
        shown_text = shown_text + "\nVeggie added: Yes"
    else:
        shown_text = shown_text + "\nVeggie added: No"
    fish_text.configure(text=shown_text)


def when_meat_clicked(choice, pot_label, text):
    choice[1] = 1
    meat_img = PhotoImage(file="meat.gif")
    pot_label.configure(image=meat_img)
    pot_label.image = meat_img
    if choice[0] == 1:
        shown_text = "Fish added: Yes"
    else: 
        shown_text = "Fish added: No"
    shown_text = shown_text + "\nMeat added: Yes"
    if choice[2] == 1:
        shown_text = shown_text + "\nVeggie added: Yes"
    else:
        shown_text = shown_text + "\nVeggie added: No"
    text.configure(text=shown_text)

def when_veggie_clicked(choice, pot_label, text):
    choice[2] = 1
    veggie_img = PhotoImage(file="veggie.gif")
    pot_label.configure(image=veggie_img)
    pot_label.image = veggie_img
    if choice[0] == 1:
        shown_text = "Fish added: Yes"
    else: 
        shown_text = "Fish added: No"
    if choice[1] == 1:
        shown_text = shown_text + "\nMeat added: Yes"
    else:
        shown_text = shown_text + "\nMeat added: No"
    shown_text = shown_text + "\nVeggie added: Yes"
    text.configure(text=shown_text)

def remove_fish(choice, pot_label, text):
    choice[0] = 0
    fish_img = PhotoImage(file="fish.gif")
    pot_label.configure(image=fish_img)
    pot_label.image = fish_img
    shown_text = "Fish added: No\n"
    if choice[1] == 1:
        shown_text = shown_text + "Meat added: Yes"
    else: 
        shown_text = shown_text + "Meat added: No"
    if choice[2] == 1:
        shown_text = shown_text + "\nVeggie added: Yes"
    else:
        shown_text = shown_text + "\nVeggie added: No"
    text.configure(text=shown_text)

def remove_meat(choice, pot_label, text):
    choice[1] = 0
    meat_img = PhotoImage(file="meat.gif")
    pot_label.configure(image=meat_img)
    pot_label.image = meat_img
    if choice[0] == 1:
        shown_text = "Fish added: Yes"
    else: 
        shown_text = "Fish added: No"
    shown_text = shown_text + "\nMeat added: No"
    if choice[2] == 1:
        shown_text = shown_text + "\nVeggie added: Yes"
    else:
        shown_text = shown_text + "\nVeggie added: No"
    text.configure(text=shown_text)

def remove_veggie(choice, pot_label, text):
    choice[2] = 0
    veggie_img = PhotoImage(file="veggie.gif")
    pot_label.configure(image=veggie_img)
    pot_label.image = veggie_img
    if choice[0] == 1:
        shown_text = "Fish added: Yes"
    else: 
        shown_text = "Fish added: No"
    if choice[1] == 1:
        shown_text = shown_text + "\nMeat added: Yes"
    else:
        shown_text = shown_text + "\nMeat added: No"
    shown_text = shown_text + "\nVeggie added: No"
    text.configure(text=shown_text)

def cook_now(root, choice):
    root.destroy()
    cooked_window = tk.Tk()
    cooked_window.title("cooked")
    cooked_window.config(width=600, height=600)
    button_close = tk.Button(
        cooked_window,
        text="close now",
        command=cooked_window.destroy
    )
    button_go_back = tk.Button(
        cooked_window,
        text="go back",
        command=lambda: go_back_to_main(cooked_window, root)
    )
    button_close.place(x=75, y=75)
    button_go_back.place(x=150, y=0)
    if choice == [1, 1, 1]:
        cooked = PhotoImage(file="all cooked.gif")
    elif choice == [1, 1, 0]:
        cooked = PhotoImage(file="fish and meat dish.gif")
    elif choice == [0, 1, 1]:
        cooked = PhotoImage(file="meat and veggie dish.gif")
    elif choice == [1, 0, 0]:
        cooked = PhotoImage(file="cooked fish dish.gif")
    elif choice == [0, 1, 0]:
        cooked = Image.open("steak.png")
        cooked = ImageTk.PhotoImage(cooked)
    elif choice == [0, 0, 1]:
        cooked = Image.open("carrot.jpg")
        cooked = cooked.resize((400, 400))
        cooked = ImageTk.PhotoImage(cooked)
    elif choice == [0, 0, 0]:
        error_text = Label(cooked_window, text="please choose at least one or more ingredients")
        error_text.pack()
        error_text.place(x=250, y=300)
    #image = tk.Label(cooked_window, text="click here", image=cooked)
    #image.pack()
    #image.place(x=150, y=50)    

    cooked_window.mainloop()

def go_back_to_main(current, main):
    current.destroy()
    make_main()

if __name__ == '__main__':
    main()