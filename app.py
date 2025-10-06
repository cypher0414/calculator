import tkinter as tk
root=tk.Tk()
root.title("Calculator")
e=tk.Entry(root,width=20,font=('Arial',20),borderwidth=5)
e.grid(row=0,column=0,columnspan=4)
def click(num):
    e.insert(tk.END,str(num))
def clear():
    e.delete(0,tk.END)
def equal():
    try:
        result=eval(e.get())
        e.delete(0,tk.END)
        e.insert(0,result)
    except:
        e.delete(0,tk.END)
buttons=[
'7','8','9','/','4','5','6','*','1','2','3','-','.','0','=','+'
]
r,c=1,0
for b in buttons:
    tk.Button(root,text=b,width=5,height=2,font=('Arial',18),
    command=(lambda x=b:equal() if x=='=' else click(x))).grid(row=r,column=c)
    c+=1
    if c>3:
        c=0
        r+=1
tk.Button(root,text='C',width=16,height=2,font=('Arial',18),command=clear).grid(row=r,column=0,columnspan=3)
root.mainloop()
