from tkinter import *
root = Tk()
root.title("Lakksh's Calculator")
abheer = Entry(root, borderwidth=3)
abheer.grid(row=0, columnspan = 4)

def clicked_num(number):
    global hukka
    hukka = abheer.get() + str(number)
    abheer.delete(0, END)
    abheer.insert(0, hukka)
    

def clicked_clear():
    abheer.delete(0, END)
    
def clicked_add():
    global math
    global fir_num
    math = "add"
    fir_num = int(abheer.get())
    abheer.delete(0, END)
    
    
def clicked_sub():
    global math
    global fir_num
    math = "sub"
    fir_num = int(abheer.get())
    abheer.delete(0, END)
    
def clicked_mul():
    global math
    global fir_num
    math = "mul"
    fir_num = int(abheer.get())
    abheer.delete(0, END)
    
def clicked_div():
    global math
    global fir_num
    math = "div"
    fir_num = int(abheer.get())
    abheer.delete(0, END)

    
def clicked_equal():
    if math == "add":
        fin_num = fir_num + int(hukka)
        abheer.insert(0, fin_num)
    if math == "sub":
        fin_num = fir_num - int(hukka)
        abheer.insert(0, fin_num)
    if math == "mul":
        fin_num = fir_num * int(hukka)
        abheer.insert(0, fin_num)
    if math == "div":
        fin_num = fir_num / int(hukka)
    abheer.delete(0, END)
    abheer.insert(0, fin_num)
    



mylabel1 = Button(root, text="1", command=lambda: clicked_num(1), pady = 20, padx = 20)
mylabel2 = Button(root, text="2", command=lambda: clicked_num(2), pady = 20, padx = 20)
mylabel3 = Button(root, text="3", command=lambda: clicked_num(3), pady = 20, padx = 20)
mylabel4 = Button(root, text="4", command=lambda: clicked_num(4), pady = 20, padx = 20)
mylabel5 = Button(root, text="5", command=lambda: clicked_num(5), pady = 20, padx = 20)
mylabel6 = Button(root, text="6", command=lambda: clicked_num(6), pady = 20, padx = 20)
mylabel7 = Button(root, text="7", command=lambda: clicked_num(7), pady = 20, padx = 20)
mylabel8 = Button(root, text="8", command=lambda: clicked_num(8), pady = 20, padx = 20)
mylabel9 = Button(root, text="9", command=lambda: clicked_num(9), pady = 20, padx = 20)
mylabel0 = Button(root, text="0", command=lambda: clicked_num(0), pady = 20, padx = 20)
mylabelplus = Button(root, text="+", command=clicked_add, pady = 20, padx = 20)
mylabelminus = Button(root, text="-", command=clicked_sub, pady = 20, padx = 20)
mylabelmultiply = Button(root, text="x", command=clicked_mul, pady = 20, padx = 20)
mylabeldivide = Button(root, text="/", command=clicked_div, pady = 20, padx = 20)
mylabelclear = Button(root, text="AC", command=clicked_clear, pady = 20, padx = 17)
mylabelequal = Button(root, text="=", command=clicked_equal, pady = 20, padx = 20)

mylabel1.grid(row=4, column=2)
mylabel2.grid(row=4, column=1)
mylabel3.grid(row=4, column=0)
mylabel4.grid(row=3, column=2)
mylabel5.grid(row=3, column=1)
mylabel6.grid(row=3, column=0)
mylabel7.grid(row=2, column=2)
mylabel8.grid(row=2, column=1)
mylabel9.grid(row=2, column=0)
mylabel0.grid(row=5, column=1)
mylabelplus.grid(row=3, column=3)
mylabelminus.grid(row=4, column=3)
mylabelmultiply.grid(row=5, column=0)
mylabeldivide.grid(row=5, column=2)
mylabelclear.grid(row=2, column=3)
mylabelequal.grid(row=5, column=3)




root.mainloop()
