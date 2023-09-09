from tkinter import*
import os

caminho=os.path.dirname(__file__)
namefile=caminho+"\\Registration.txt"


def imprimirdados():
    arquivo=open(namefile,"a")
    arquivo.write("Name: %s" % gname.get())
    arquivo.write("\nTell: %s" % gfone.get())
    arquivo.write("\nEmail: %s" % gmail.get())
    arquivo.write("\nBio: %s" % gobs.get("1.0",END))
    arquivo.write("\n\n")
    arquivo.close()
      
    
R=Tk()
R.title("Rsgister Screen")
R.geometry("500x300")
R.configure(background="#dde")

Label(R,text="REGISTER",bg="#dde",fg="#009",anchor=W).place(x=200,y=10,width=100,height=20)


Label(R,text="Name", background="#dde",foreground="#009", anchor=W).place(x=10,y=20,width=100,height=20)
gname=Entry(R)
gname.place(x=10,y=40,width=100,height=20)

Label(R,text="Tell",bg="#dde",fg="#009",anchor=W).place(x=10,y=60,width=100,height=20)
gfone=Entry(R)
gfone.place(x=10,y=80,width=100,height=20)

Label(R,text="E-mail",bg="#dde",fg="#009",anchor=W).place(x=10, y=100,width=100,height=20)
gmail=Entry(R)
gmail.place(x=10,y=120,width=300,height=20)

Label(R,text="BIO",background="#dde",foreground="#009",anchor=W).place(x=10,y=140,width=100,height=20)
gobs=Text(R)
gobs.place(x=10,y=160,width=300,height=80)

Button(R,text="Save",command=imprimirdados).place(x=10,y=250,width=100,height=20)


R.mainloop()