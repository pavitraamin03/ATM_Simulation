import mysql.connector as m
from deep_translator import GoogleTranslator
try:
    db=m.connect(host="localhost",user="root",passwd="root")
    cur=db.cursor()
    
    cur.execute("create database if not exists adv_python")
    cur.execute("use adv_python")
    #cur.execute("drop table if exists users")
    cur.execute("create table if not exists users(cname text,mob text,email text,uid varchar(20),pwd text,opbal float)")
    text="table created"
    ans=GoogleTranslator(source="en",target="gu").translate(text)
    print(ans)

    
    while True:
        txt="-----MENU------"
        a=GoogleTranslator(source="en",target="gu").translate(txt)
        print(a)
        t="1.SignUp"
        b=GoogleTranslator(source="en",target="gu").translate(t)
        print(b)
        c="2.SignIn"
        d=GoogleTranslator(source="en",target="gu").translate(c)
        print(d)
        e="0.Exit"
        f=GoogleTranslator(source="en",target="gu").translate(e)
        print(f)
        ch=int(input("Enter Your Choice = "))
        if ch==1:
            cname=input("Enter Customer Name = ")
            g=GoogleTranslator(source="en",target="gu").translate(cname)
            print(g)
            mob=input("Enter Mobile Number = ")
            h=GoogleTranslator(source="en",target="gu").translate(mob)
            print(h)
            if len(mob)!=10 or not mob.isdigit():
                print("Please Enter a Valid Mobile Number")
                continue
            email=input("Enter Email ID = ")
            opbal=input("Enter Opening Balance = ")
            uid=input("Enter User ID = ")
            pwd=input("Enter Password = ")
            cpwd=input("Please Confirm Your Password = ")
            if pwd!=cpwd:
                print("Your Password Must Match Your Confirmed Password")
                continue
            
            cur.execute("insert into users values('"+cname+"','"+mob+"','"+email+"','"+uid+"','"+pwd+"','"+opbal+"')")
            db.commit()
            print("Registration Done Successfully")
            
        elif ch==2:
            #check uid and pwd and confirm
            cur.execute("select * from users")
            for i in cur:
                print(i)
            uid=input("Enter User Id = ")
            pwd=input("Enter Password = ")
            cur.execute("select * from users where uid='"+uid+"' and pwd='"+pwd+"' ")
            ans=cur.fetchone()
            if ans:
                while True:
                    print("Welcome User ",ans[0])
                    print("1.Deposit\n2.Withdraw\n3.Display\n4.Back")
                    choice=int(input("Enter Your Choice = "))
                    if choice==1:
                        amt=int(input("Enter Deposite Amount = "))
                        cur.execute("update users set opbal=opbal+'"+str(amt)+"' where uid='"+uid+"' ")
                        db.commit()
                        print("Amount deposited ")
                    elif choice==2:
                        amt=int(input("Enter Withdraw Amount = "))
                        cur.execute("update users set opbal=opbal-'"+str(amt)+"' where uid='"+uid+"' ")
                        db.commit()
                        print("Amount withdrawn ")
                    elif choice==3:
                        cur.execute("select * from users where uid='"+uid+"' ")
                        for i in cur:
                            print(i)
                    elif choice==4:
                        break
            else:
                print("Invalid Credentials")
        elif ch==0:
            break

except Exception as e:
    print(e)
