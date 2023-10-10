import tkinter as tk


def btnpress(char):
    global equ
    equ = equ + str(char)
    eq.set(equ)
root=tk.Tk()

def back():
    try:
        global equ
        a=eq.get()
        a=int(a)
        a=a//10
        a=str(a)
        equ=a
        eq.set(equ)
    except:
        pass


def evaluate(eq):
    try:
        global equ
        data=eq.get()
        equ=''
        a=data.replace('x','*')
        a=a.replace('^','**')
        eq.set('Answer: '+str(eval(a)))   
    except:
        eq.set('Invalid entry')


def clear():
    global equ
    equ = ''
    eq.set('0')


h,w,fgclr,fgclr2,bgclr,bgclr2,fnt=4,8,'black','Red','white','white',('Calibri' 'bold',20)
equ=''
eq = tk.StringVar()
calculation = tk.Label(root,font=('Calibri',16),textvariable = eq)
eq.set('0')
calculation.config(text='')
calculation.grid(columnspan = 5)

B0=tk.Button(root,text='0',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(0))
B1=tk.Button(root,text='1',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(1))
B2=tk.Button(root,text='2',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(2))
B3=tk.Button(root,text='3',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(3))
B4=tk.Button(root,text='4',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(4))
B5=tk.Button(root,text='5',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(5))
B6=tk.Button(root,text='6',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(6))
B7=tk.Button(root,text='7',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(7))
B8=tk.Button(root,text='8',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(8))
B9=tk.Button(root,text='9',height=h,width=w,font=(fnt),fg=fgclr,bg=bgclr,command =lambda: btnpress(9))
Beq=tk.Button(root,text='=',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: evaluate(eq))
Bplus=tk.Button(root,text='+',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('+'))
Bminus=tk.Button(root,text='-',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('-'))
Bmul=tk.Button(root,text='x',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('x'))
Bdiv=tk.Button(root,text='/',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('/'))
Bclr=tk.Button(root,text='C',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: clear())
Bbrs=tk.Button(root,text='(',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('('))
Bbre=tk.Button(root,text=')',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress(')'))
Bback=tk.Button(root,text='~',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: back())
Bpow=tk.Button(root,text='^',height=h,width=w,font=(fnt),fg=fgclr2,bg=bgclr2,command =lambda: btnpress('^'))

B1.grid(row=1,column=0)
B2.grid(row=1,column=1)
B3.grid(row=1,column=2)
B4.grid(row=2,column=0)
B5.grid(row=2,column=1)
B6.grid(row=2,column=2)
B7.grid(row=3,column=0)
B8.grid(row=3,column=1)
B9.grid(row=3,column=2)
B0.grid(row=4,column=1,)
Bclr.grid(row=4,column=0)
Beq.grid(row=4,column=2)
Bplus.grid(row=1,column=3)
Bminus.grid(row=2,column=3)
Bmul.grid(row=3,column=3)
Bdiv.grid(row=4,column=3)
Bback.grid(row=1,column=4)
Bbrs.grid(row=2,column=4)
Bbre.grid(row=3,column=4)
Bpow.grid(row=4,column=4)

root.mainloop()