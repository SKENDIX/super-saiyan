import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import filedialog as fd
import sqlite3 as sqltor
import matplotlib.pyplot as plt
import ast

import os
import math
import random
import smtplib


conn=sqltor.connect('main.db') 
cursor=conn.cursor() 
cursor.execute("""CREATE TABLE IF NOT EXISTS poll
                    (name)""")

root=Tk()
root.geometry("900x530+300+190")
root.resizable(False,False)
root.title("Voting System")
root.configure(bg="#adacb1")


def login():
    pct=Toplevel()
    pct.geometry('270x530+1220+190')
    pct.title('login')
    pct.resizable(False,False)
    pct.configure(bg='#fff')


    def signin():
        username=user.get()
        password=code.get()

        file=open('Members.txt','r')
        d=file.read()
        r=ast.literal_eval(d)
        file.close()

        if username in r.keys() and password==r[username]:
            pct.destroy()
            create()

        else:
            messagebox.showerror('Invalid','invalid username or password')

            
    Label(pct,text='admin',font='Helvetica 16 bold',bg='#fff').place(x=5,y=10)


    frame1=Frame(pct,width=350,height=350,bg="white")
    frame1.place(x=10,y=70)

    heading=Label(frame1,text='Login to enter',fg='#57a1f8',bg='white',font='arial 15 ')
    heading.place(x=60,y=5)

    

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')

        
    user = Entry(frame1,width=20,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame1,width=180,height=2,bg='black').place(x=25,y=100)

    
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')



    code = Entry(frame1,width=20,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame1,width=180,height=2,bg='black').place(x=30,y=177)

    

    Button(frame1,width=25,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=signin).place(x=27,y=204)

    pct.mainloop()
    

def register():
    rkp=Toplevel(root)
    rkp.title("Become Member")
    rkp.geometry("900x530+300+190")
    rkp.configure(bg="#fff")
    rkp.resizable(False,False)

    def signup():
        username=user.get()
        password=code.get()
        conform_password=conform_code.get()

        if password==conform_password:
            try:
                file=open('Members.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('Members.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('Signup','Now you are member of this Election commission')
                rkp.destroy()
    
            except:
                file=open('Members.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()


        else:
            messagebox.showerror('Invalid',"Both Password should match")
    
    img = PhotoImage(file='Image/signup.png')
    Label(rkp,image=img,border=0,bg='white').place(x=50,y=90)

    frame=Frame(rkp,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)


    heading1=Label(frame,text='Register to Become Member',fg="black",bg='white',font=('arial',15,'bold'))
    heading1.place(x=30,y=5)

    
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0, 'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    
    def on_enter(e):
        conform_code.delete(0,'end')
    def on_leave(e):
        if conform_code.get()=='':
            conform_code.insert(0,'Confirm Password')

    conform_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    conform_code.place(x=30,y=220)
    conform_code.insert(0, 'Confirm Password')
    conform_code.bind("<FocusIn>",on_enter)
    conform_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    
    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=280)
    

    rkp.mainloop()



def resultsection(): 
    def results():
        sel=sele.get()  
        if sel=='-select-':
            return messagebox.showerror('Error','Select Poll')
        else:
            pl.destroy()
            def project():
                names=[]
                votes=[]
                for i in range(len(r)):
                    data=r[i]
                    names.append(data[0])
                    votes.append(data[1])
                    plt.title('Poll Result')
                plt.pie(votes,labels=names,autopct='%1.1f%%',shadow=True,startangle=140)
                plt.axis('equal')
                plt.show()

            res=Toplevel() 
            res.geometry("900x530+300+190")
            res.title('Results!')
            res.resizable(False, False)

            frame10=Frame(res,width=500,height=300)
            frame10.place(x=100,y=100)
            
            Label(res,text='Here is the Result!',font='Helvetica 12 bold').place(x=10,y=10)
            con=sqltor.connect(sel+'.db')
            pcursor=con.cursor()
            pcursor.execute('select * from polling')
            r=pcursor.fetchall()
            for i in range(len(r)):
                data=r[i]
                Label(frame10,text=data[0]+': '+str(data[1])+' votes',font='Helvetica 22 ').grid(row=2+i,column=1)
            Button(res,text='Project Results',width=50,height=2,bg='lightblue',font='20',command=project).place(x=40,y=400)


    cursor.execute('select name from poll')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    sele=StringVar()
    pl=Toplevel()
    pl.geometry('270x530+1220+190')
    pl.title('Voting result')
    pl.resizable(False,False)
    pl.configure(bg='#fff')
    Label(pl,text='Select Poll',font='Helvetica 12 bold',bg='#fff').pack(padx=10,pady=30)
    sel=ttk.Combobox(pl,values=pollnames,state='readonly',textvariable=sele,width=20,font='15')
    sel.pack()
    sel.current(0)
    Button(pl,text='Get Results',width=21,font='10',command=results).pack(pady=10)

    pl.mainloop()
    

def votingsystem():
    ppage=Toplevel()
    ppage.title("vote")
    ppage.geometry("900x530+300+190")
    ppage.configure(bg="lightblue")
    ppage.resizable(False,False)


    def proceed():
        chose=choose.get()
        print(chose)
        command='update polling set votes=votes+1 where name=?'
        pd.execute(command,(chose,))
        pd.commit()
        messagebox.showinfo('Success!','You have voted')
        votebutton["state"] = DISABLED

        

    def logout():
        ppage.destroy()
        user()


    
    Top=Frame(ppage,width=900,height=60,bg="#18224b")
    Top.place(x=0,y=0)

    MainFrame=Frame(ppage,width=600,height=300,bg="#f0f0f0")
    MainFrame.place(x=150,y=150)

    logo=PhotoImage(file="Image/national.png")
    mylogo=Label(Top,image=logo,background="#18224b")
    mylogo.place(x=30,y=-16)

    Label(Top,text='Voting System',font=('arial',14,'bold'),fg='#fff',bg='#18224b').place(x=130,y=15)
    
    choose=StringVar()
    choose.set(None)

    names=[]
    pd=sqltor.connect(plname+'.db') 
    pcursor=pd.cursor() 
    pcursor.execute('select name from polling')
    data=pcursor.fetchall()
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        names.append(ndata)
    print(names)



    Label(MainFrame,text='Select Any One candidate',bg='#f0f0f0',font='10').place(x=10,y=10)

    Frame(MainFrame,width=580,height=1,bg='grey').place(x=10,y=50)


    radioframe=Frame(MainFrame,width=580,height=230,bg='#f0f0f0')
    radioframe.place(x=10,y=60)
    for i in range(len(names)):
        Radiobutton(radioframe,width=10,height=2,font='30',text=names[i],value=names[i],variable=choose).grid(row=10+i,column=4)
    votebutton=Button(ppage,text='Vote',font='20',width=20,height=2,bg='#6dcff6',command=proceed)
    votebutton.place(x=550,y=230)
    Button(ppage,text='Logout',font='20',width=20,height=2,bg='black',fg="white",command=logout).place(x=550,y=330)






def user():
    rk=Toplevel()
    rk.title("Username")
    rk.geometry("900x530+300+190")
    rk.configure(bg="#fff")
    rk.resizable(False,False)
    

    
    image_icon=PhotoImage(file="Image/national.png")
    rk.iconphoto(False,image_icon)

    sidebar=Frame(rk,width=450,height=550,bg="#18224b")
    sidebar.place(x=0,y=0)

    img = PhotoImage(file='Image/national.png')
    Label(rk,image=img,border=0,bg='#18224b').place(x=20,y=10)

    Label(rk,text='Voter Portal',font='arial 20 bold',bg='#18224b',fg='#fff').place(x=110,y=26)
    Label(rk,text='Election Commission Of India',bg='#18224b',fg='#fff').place(x=110,y=55)

    def signup():
        username=user.get()
        emailid=email.get()

            



        
    
        if username=='Username' or emailid=='Email':
            messagebox.showerror('Invalid',"Type valid username and Email")


        else:
            sender="jsuyash149@gmail.com"
            password="pythonproject"

            digits = "0123456789"
            OTP = ""
            for i in range (6):
                OTP += digits[math.floor(random.random()*10)]
            otp = OTP + " is your OTP"

            message = f"Subject:Voting Registration\n{otp}"

            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()

            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()

            server.login(sender,password)
            server.sendmail(sender,emailid,message)

            Label(rk,text="Enter Your OTP",font=('Microsoft Yahei UI Light',10),bg="white",fg='black').place(x=470,y=330)


            code = Entry(rk,width=20,fg='black',border=1,bg='white',font=('Microsoft Yahei UI Light',20))
            code.place(x=470,y=360)
##            code.insert(0, 'OTP')

            def enterotp():
                a=code.get()
                username=user.get()
                emailid=email.get()

                if a==OTP:
                    print("Verified")

                    try:
                        file=open('datasheet.txt','r+')
                        d=file.read()
                        r=ast.literal_eval(d)

                        dict2={username:emailid}
                        r.update(dict2)
                        file.truncate(0)
                        file.close()
    
                        file=open('datasheet.txt','w')
                        w=file.write(str(r))

                        messagebox.showinfo('Congratulations','Sucessfully Login')

                        rk.destroy()
                
                        votingsystem()

                    except:
                        file=open('datasheet.txt','w')
                        pp=str({'Username':'Email'})
                        file.write(pp)
                        file.close()

                else:
                    messagebox.showerror('info','Invalid User name!!')
                    

            Button(rk,width=39,pady=7,text='Login',bg='blue',fg='white',border=0,command=enterotp).place(x=470,y=430)





    frame=Frame(rk,width=500,height=390,bg='#fff')
    frame.place(x=450,y=50)


    heading=Label(frame,text='Login',fg="#57a1f8",bg='white',font=('arial',30,'bold'))
    heading.place(x=20,y=5)

    
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Username')

    user = Entry(frame,width=45,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=375,height=2,bg='black').place(x=25,y=107)

    
    def on_enter(e):
        email.delete(0,'end')


    email = Entry(frame,width=45,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    email.place(x=30,y=150)
    email.insert(0, 'Email')
    email.bind("<FocusIn>",on_enter)
    

    Frame(frame,width=375,height=2,bg='black').place(x=25,y=177)



    Button(frame,width=39,pady=7,text='Send OTP',bg='orange',fg='white',border=0,command=signup).place(x=35,y=200)
    


    rk.mainloop()



def polls(): 
    def proceed():
        global plname
        plname=psel.get()
        if plname=='-select-':
            return messagebox.showerror('Error','select poll')
        else:
            mpolls.destroy()
            user()
    cursor.execute('select name from poll')
    data=cursor.fetchall()
    pollnames=['-select-']
    for i in range(len(data)):
        data1=data[i]
        ndata=data1[0]
        pollnames.append(ndata)
    psel=StringVar()
    
    mpolls=Toplevel()
    mpolls.geometry('270x530+1220+190')
    mpolls.title('Voting Selection')
    mpolls.configure(bg="#fff")
    mpolls.resizable(False,False)
    
    Label(mpolls,text='Select Voting',font='Helvetica 12 bold',bg='#fff').pack(padx=10,pady=30)
    select=ttk.Combobox(mpolls,values=pollnames,state='readonly',textvariable=psel,width=20,font='15')
    select.pack()
    select.current(0)
    Button(mpolls,text='Proceed',width=21,font='10',command=proceed).pack(pady=10)



def create():
    def proceed():
        global pcursor
        pname=name.get() 
        can=cname.get()   
        if pname=='':
            return messagebox.showerror('Error','Enter poll name')
        elif can=='':
            return messagebox.showerror('Error','Enter candidates')
        else:
            candidates=can.split(',') 
            command='insert into poll (name) values (?);'
            cursor.execute(command,(pname,))
            conn.commit()
            pd=sqltor.connect(pname+'.db') 
            pcursor=pd.cursor() 
            pcursor.execute("""CREATE TABLE IF NOT EXISTS polling
                 (name TEXT,votes INTEGER)""")
            for i in range(len(candidates)):
                command='insert into polling (name,votes) values (?, ?)'
                data=(candidates[i],0)
                pcursor.execute(command,data)
                pd.commit()
            pd.close()
            messagebox.showinfo('Success!','Poll Created')
            cr.destroy()

    cr=Toplevel(root)
    cr.title("Registration")
    cr.geometry("900x530+300+190")
    cr.configure(bg="#f26d7d")
    cr.resizable(False,False)
    

   
    image_icon=PhotoImage(file="Image/national.png")
    cr.iconphoto(False,image_icon)

    sidebar=Frame(cr,width=450,height=550,bg="#fff")
    sidebar.place(x=0,y=0)

    img = PhotoImage(file='Image/signup.png')
    Label(cr,image=img,border=0,bg='#fff').place(x=20,y=60)

    Label(cr,text='Registration',font=('arial',20,'bold'),bg='#fff').place(x=130,y=330)
    
  
    name=StringVar()
    cname=StringVar()
    
    Label(cr,text='Enter Details',font='Helvetica 22 bold',bg="#f26d7d",fg='#fff').place(x=450,y=20)
    Label(cr,text='Election Purpose: ',font=('arial',12,'bold'),bg="#f26d7d").place(x=450,y=100)
    Entry(cr,width=30,textvariable=name,font=('arial',12)).place(x=600,y=100)
    
    Label(cr,text='(eg: captain elections)',bg="#f26d7d").place(x=600,y=130)
    
    Label(cr,text='Enter Candidates: ',bg="#f26d7d",font=('arial',12,'bold')).place(x=450,y=200)
    Entry(cr,width=30,textvariable=cname,font=('arial',12)).place(x=600,y=200)
    Label(cr,text='Enter name with comma separated',bg='#f26d7d').place(x=600,y=230)
    
    Button(cr,text='Proceed', width=25,height=1,font=('arial',20),bg='#362f2d',fg='white',command=proceed).place(x=470,y=300)
    cr.mainloop()


image_icon=PhotoImage(file="Image/national.png")
root.iconphoto(False,image_icon)


frame=Frame(root,width=900,height=130,bg="#18224b")
frame.place(x=0,y=0)

logo=PhotoImage(file="Image/national.png")
mylogo=Label(frame,image=logo,background="#18224b")
mylogo.place(x=30,y=10)

Label(frame,text='Voting System',font=('arial',20,'bold'),fg='#fff',bg='#18224b').place(x=130,y=40)

vote=Button(frame,text='Vote',width=10,font=('arial', 20,'bold'),command=polls)
vote.place(x=700,y=30)



image1=PhotoImage(file='Image/image1.png')
registration=Button(root,image=image1,command=login)
registration.place(x=100,y=200)


image2=PhotoImage(file='Image/image2.png')
result=Button(root,image=image2,command=resultsection)
result.place(x=350,y=200)


image3=PhotoImage(file='Image/image3.png')
member=Button(root,image=image3,command=register)
member.place(x=600,y=200)







Bottom=Frame(root,width=900,height=100,bg="#fff")
Bottom.place(x=0,y=450)

root.mainloop()




