from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_helper import  PlayAudio
import threading

#some usefull variables
font=('Vedana',20,'bold')
ob = PlayAudio()


#important funtions

def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0, ex)


def all_clear():
    textField.delete(0,END)



def click_btn_funtion(event):
    print("btn clicked")
    b= event.widget
    text=b['text']
    print(text)
    t=threading.Thread(target=ob.speak,args=(text,))
    t.start()

    if text=='=':
        try:
               ex = textField.get()
               answer=eval(ex)
               textField.delete(0,END)
               textField.insert(0,answer)
        except Exception as e:
            print("Error..",e)
            showerror('Error.',e)
        return

    textField.insert(END, text)



#creating a window
window = Tk()
window.title('Calculator -By UGT')
window.geometry('420x480')
#picture label
pic=PhotoImage(file='Ugtcalci.png')
headingLabel =Label(window,image=pic,)
headingLabel.pack(side=TOP,pady=10)


#heading label
heading = Label(window,text='UGTs CALCI', font=font, )
heading.pack(side=TOP)

#text field
textField=Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)

#buttons


buttonFrame=Frame(window)
buttonFrame.pack(side=TOP, padx=10)

#adding_button
temp = 1
for i in range(0,3):      #by using matrix 3 rows * 3 colms
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp) ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i, column=j )
        temp= temp+1      #temp variable use karke +1 number kiya
        btn.bind('<Button-1>',click_btn_funtion)


zeroBtn=Button(buttonFrame,text='0' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
zeroBtn.grid(row=3, column=0 )

dotBtn=Button(buttonFrame,text='.' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
dotBtn.grid(row=3, column=1 )

equalBtn=Button(buttonFrame,text='=' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
equalBtn.grid(row=3, column=2 )

plusBtn=Button(buttonFrame,text='+' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
plusBtn.grid(row=0, column=3 )

subBtn=Button(buttonFrame,text='-' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
subBtn.grid(row=1, column=3 )

multBtn=Button(buttonFrame,text='*' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
multBtn.grid(row=2, column=3)

divdeBtn=Button(buttonFrame,text='/' ,font=font, width=5,relief='ridge',activebackground='orange',activeforeground='white')
divdeBtn.grid(row=3, column=3 )

clearBtn=Button(buttonFrame,text='<--' ,font=font, width=11,relief='ridge',activebackground='orange',activeforeground='white',command=clear)
clearBtn.grid(row=4, column=0 , columnspan=2 )

allClearBtn=Button(buttonFrame,text='AC' ,font=font, width=11,relief='ridge',activebackground='orange',activeforeground='white', command=all_clear)
allClearBtn.grid(row=4, column=2 , columnspan=2 )

#binding all btns
plusBtn.bind('<Button-1>',click_btn_funtion)
subBtn.bind('<Button-1>',click_btn_funtion)
multBtn.bind('<Button-1>',click_btn_funtion)
divdeBtn.bind('<Button-1>',click_btn_funtion)
zeroBtn.bind('<Button-1>',click_btn_funtion)
dotBtn.bind('<Button-1>',click_btn_funtion)
equalBtn.bind('<Button-1>',click_btn_funtion)


def enterClick(event):
    print('hii')
    e=Event()
    e.widget = equalBtn
    click_btn_funtion(e)

textField.bind('<Return>',enterClick)

########################################################################################################
#funtions for scientific
scFrame=Frame(window)
fontSc=('',18,'bold')

sqrtBtn=Button(scFrame,text='√' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
sqrtBtn.grid(row=0, column=0 )


powBtn=Button(scFrame,text='^' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
powBtn.grid(row=0, column=1 )

factBtn=Button(scFrame,text='X!' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
factBtn.grid(row=0, column=2 )

radBtn=Button(scFrame,text='toRad' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
radBtn.grid(row=0, column=3)

degBtn=Button(scFrame,text='toDeg' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
degBtn.grid(row=1, column=0 )

sinBtn=Button(scFrame,text='sinθ' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
sinBtn.grid(row=1, column=1 )

cosBtn=Button(scFrame,text='cosθ' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
cosBtn.grid(row=1, column=2 )

tanBtn=Button(scFrame,text='tanθ' ,font=fontSc, width=5,relief='ridge',activebackground='orange',activeforeground='white')
tanBtn.grid(row=1, column=3 )

noramalcalc = True



def calculate_sc(event):
    print('btn..')
    btn=event.widget
    text=btn['text']
    print(text)
    ex = textField.get()
    answer=' '
    if text == 'toDeg':
        print("cal degree")
        answer = str(m.degrees(float(ex)))

    elif text =='toRad':
        print('radian')
        answer=str(m.radians(float(ex)))
    elif text == 'X!':
        print("cal factorial")
        answer=str(m.factorial(int(ex)))
    elif text == 'sinθ'  :
        print("cal sin")
        answer=str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text== 'tanθ':
        print('cal tan')
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√' :
        print('sqrt')
        answer = m.sqrt(int(ex))
    elif text == '^' :
        print('pow')
        base, pow =ex.split(',')
        print(base)
        print(pow)
        answer = m.pow(int(base), int(pow))

    textField.delete(0, END)
    textField.insert(0, answer)



def sc_click():
    global noramalcalc
    if noramalcalc:
        # sc...
        buttonFrame.pack_forget()
        #add sc frame

        scFrame.pack(side=TOP,pady=15)
        buttonFrame.pack(side=TOP)
        window.geometry('420x600')
        print("Show sc")
        noramalcalc=False
    else:
        print("Show normal")
        scFrame.pack_forget()
        window.geometry('420x480')
        noramalcalc = True



#end funtions
#binding sc button
sqrtBtn.bind("<Button-1>",calculate_sc)
powBtn.bind("<Button-1>",calculate_sc)
factBtn.bind("<Button-1>",calculate_sc)
sinBtn.bind("<Button-1>",calculate_sc)
cosBtn.bind("<Button-1>",calculate_sc)
radBtn.bind("<Button-1>",calculate_sc)
degBtn.bind("<Button-1>",calculate_sc)
tanBtn.bind("<Button-1>",calculate_sc)

fontMenu=('',10)

menubar=Menu(window, font=fontMenu)

mode=Menu(menubar,font=fontMenu,tearoff=0)
mode.add_checkbutton(label="Scientific Calculator",command=sc_click)

menubar.add_cascade(label="Mode",menu=mode)

window.config(menu=menubar)



window.mainloop()