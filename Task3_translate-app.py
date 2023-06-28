from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

def trans(text="abc",src="English",dest="Hindi"):
    textt=text
    srcc=src
    dess=dest
    translat=Translator()
    translatt=translat.translate(textt,src=srcc,dest=dess,transliteration=True)
    transliteration_output = translatt.pronunciation
    return translatt.text,transliteration_output

def data():
    s=drpbox1.get()
    d=drpbox2.get()
    masg=text1.get(1.0,'end')
    txtget,txtpron= trans(text=masg,src=s,dest=d) 
    text2.delete(1.0,END)
    text2.insert(END,txtget)
    text3.delete(1.0,END)
    text3.insert(END,txtpron)


root =Tk()
root.title("Translator App")
root.geometry("500x700")
root.config(bg='Cyan')

label1=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="Turquoise")
label1.place(x=120,y=50,height=60,width=270)

frame1=Frame(root).pack(side='bottom')

label2=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),bg="Cyan")
label2.place(x=10,y=130,height=25,width=160)

text1=Text(frame1,font=("Time New Roman",21,"bold"),wrap='word')
text1.place(x=10,y=160,height=100,width=480)

list1=list(LANGUAGES.values())

drpbox1=ttk.Combobox(frame1,values=list1)
drpbox1.place(x=25,y=280,height=30,width=115)
drpbox1.set(value="English")

bttn1=Button(frame1,text="Translate",relief="raised",command=data)
bttn1.place(x=210,y=280,height=30,width=100)

drpbox2=ttk.Combobox(frame1,values=list1)
drpbox2.place(x=380,y=280,height=30,width=100)
drpbox2.set(value="Translate To")

label3=Label(root,text="Translated Text",font=("Time New Roman",20,"bold"),bg="Cyan")
label3.place(x=10,y=340,height=25,width=207)

text2=Text(frame1,font=("Time New Roman",21,"bold"),wrap='word')
text2.place(x=10,y=370,height=100,width=480)

text3=Text(frame1,font=("Time New Roman",21,"bold"),wrap='word')
text3.place(x=10,y=480,height=100,width=480)

root.mainloop()

