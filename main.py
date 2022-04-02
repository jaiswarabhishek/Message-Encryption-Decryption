from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)
    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")
def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password!="1234":
        messagebox.showerror("encryption","Invalid Password")

        


#The Main Screen Function

def main_screen():
    global screen
    global code
    global text1
    screen=Tk()
    screen.geometry("400x400")
    #icon
    image_icon=PhotoImage(file="encrypted.png")
    screen.iconphoto(False,image_icon)
    screen.title("App")

    #function for reset the text
    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    #input Text msg
    Label(text="Type a message",fg="black",font=("Ariel",10)).place(x=10,y=10)
    text1=Text(font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=40,width=365,height=100)

    # input secrete key
    Label(text="Enter secrete key",fg="black",font=("Ariel",10)).place(x=10,y=150)

    code=StringVar()
    Entry(textvariable=code,width=52,bd=0,font=("arial",10),show="*").place(x=10,y=180)

    # encrypt Decrypt Button

    Button(text="Encrypt",height="2",width=20,bg="#ed3833",fg="white",font=("Ariel",10),command=encrypt,bd=0).place(x=10,y=210)
    Button(text="Decrypt",height="2",width=20,bg="#00bd56",fg="white",font=("Ariel",10),command=decrypt,bd=0).place(x=210,y=210)
    Button(text="RESET",height="2",width=45,bg="#1089ff",fg="white",command=reset,font=("Ariel",10),bd=0).place(x=10,y=260)
   



    
    screen.mainloop()
main_screen()
