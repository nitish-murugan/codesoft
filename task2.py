import tkinter as tk
expression = ""

def press(num):
    global expression
    expression+=str(num)
    equation.set(expression)
    
def equalPress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        
        expression = ""
        equation.set(total)
        
def clear():
    global expression
    expression = ""
    equation.set(expression)

root = tk.Tk()
root.geometry("300x300")
root.title("Calculator")

equation = tk.StringVar()
displayScreen = tk.Entry(root,textvariable=equation,justify=tk.RIGHT,width=10,font=("Arial",20))
displayScreen.grid(columnspan=4, ipadx=70)

button16 = tk.Button(root, text=' AC ', fg='black', command= clear, height=1, width=7)
button16.grid(row=1, column=0, pady=(20,0)) 
button17 = tk.Button(root, text='+/-', fg='black', command=lambda: press('-'), height=1, width=7)
button17.grid(row=1, column=1, pady=(20,0)) 
button18 = tk.Button(root, text=' % ', fg='black', command=lambda: press('%'), height=1, width=7)
button18.grid(row=1, column=2, pady=(20,0))
button19 = tk.Button(root, text=' / ', fg='black', command=lambda: press('/'), height=1, width=7)
button19.grid(row=1, column=3, pady=(20,0))
button1 = tk.Button(root, text=' 7 ', fg='black', command=lambda: press(7), height=1, width=7)
button1.grid(row=2, column=0, pady=(20,0)) 
button2 = tk.Button(root, text=' 8 ', fg='black', command=lambda: press(8), height=1, width=7)
button2.grid(row=2, column=1, pady=(20,0)) 
button3 = tk.Button(root, text=' 9 ', fg='black', command=lambda: press(9), height=1, width=7)
button3.grid(row=2, column=2, pady=(20,0))
button4 = tk.Button(root, text=' X ', fg='black', command=lambda: press('*'), height=1, width=7)
button4.grid(row=2, column=3, pady=(20,0))
button5 = tk.Button(root, text=' 4 ', fg='black', command=lambda: press(4), height=1, width=7)
button5.grid(row=3, column=0, pady=(10,0))
button6 = tk.Button(root, text=' 5 ', fg='black', command=lambda: press(5), height=1, width=7)
button6.grid(row=3, column=1, pady=(20,0))
button7 = tk.Button(root, text=' 6 ', fg='black', command=lambda: press(6), height=1, width=7)
button7.grid(row=3, column=2, pady=(20,0))
button8 = tk.Button(root, text=' - ', fg='black', command=lambda: press('-'), height=1, width=7)
button8.grid(row=3, column=3, pady=(20,0))
button9 = tk.Button(root, text=' 1 ', fg='black', command=lambda: press(1), height=1, width=7)
button9.grid(row=4, column=0, pady=(20,0))
button10 = tk.Button(root, text=' 2 ', fg='black', command=lambda: press(2), height=1, width=7)
button10.grid(row=4, column=1, pady=(20,0))
button11 = tk.Button(root, text=' 3 ', fg='black', command=lambda: press(3), height=1, width=7)
button11.grid(row=4, column=2, pady=(20,0))
button12 = tk.Button(root, text=' + ', fg='black', command=lambda: press('+'), height=1, width=7)
button12.grid(row=4, column=3, pady=(20,0))
button13 = tk.Button(root, text=' 0 ', fg='black', command=lambda: press(0), height=1, width=17)
button13.grid(row=5, column=0, pady=(20,0), columnspan=2)
button14 = tk.Button(root, text=' . ', fg='black', command=lambda: press('.'), height=1, width=7)
button14.grid(row=5, column=2, pady=(20,0))
button15 = tk.Button(root, text=' = ', fg='black', command=equalPress, height=1, width=7)
button15.grid(row=5, column=3, pady=(20,0))





root.mainloop()