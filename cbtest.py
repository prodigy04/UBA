import mysql.connector


Connect = mysql.connector.connect(host='127.0.0.1', user = 'root', passwd='', database='Cbt_Exam')
myCursor = Connect.cursor()
# myCursor.execute("CREATE DATABASE Cbt_Exam")
# myCursor.execute("SHOW DATABASES")


# for db in myCursor:
#     print(db)


# myCursor.execute("CREATE TABLE Test (Std_id INT(4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR(20), Address VARCHAR(50), Phone VARCHAR(11), Password VARCHAR(20), Confirm_Password VARCHAR(20) )")
# myCursor.execute("SHOW TABLES")
# for table in myCursor:
#     print(table)





class Exam():
    def __init__(self):
        pass
        self.x = 0
        self.text = ("""
        
                    1. Register
                    2. Log In
        """)
        print(self.text)
        self.Val()
    def Val(self):
        # print(" 1. Register\n 2.Log In")

        self.value = input("What will you like to do?  ")
        if self.value == "1":
            print("Fill in the form below...")
            self.tet()
        elif self.value == "2":
            print("Kindly log in below...")
            self.login()
        else:
            print("Invalid Number!!")
            # self.value()    

    
    def login(self):
            FullName = input("Enter your fullname:  ")
            Password = input("Enter your password:  ")
            query = "SELECT Full_Name FROM Test WHERE Full_Name=%s AND Password = %s"
            val = (FullName, Password)
            myCursor.execute(query, val)
            reg = myCursor.fetchall()
            print(reg)

            print('''
                        1. Start Exam
                        2. Check Result
            ''')
            word = input("What will you like to do??  ")
            # print(word)
            if word == '1':
                self.Test()
                print("Success!")
            elif word == '2':
                self.Result()
    # self.login()        
            # print("Your result below")
        # else:
        #     print("Invalid Input")
    def tet(self):
            Full_Name = input("Enter your Full Name:  ")
            Address = input("Enter your address:  ")
            Phone = input("Enter your phone number:  ")
            Password = input("Enter your password:  ")
            Confirm_Password = input("Enter your password again:  ")
            que = "INSERT INTO Test (Full_Name, Address, Phone, Password, Confirm_Password) VALUES(%s, %s, %s, %s, %s)"
            val = (Full_Name, Address, Phone, Password, Confirm_Password)
            if Password == Confirm_Password:
                print("Registration Successfully!")
            else:
                Confirm_Password = input("Enter your password again:  ")
            user = {"Full_Name":Full_Name,"Address":Address, "Phone": Phone, "Password":Password, "Confirm_Password":Confirm_Password}
            print(user)
            myCursor.execute(que, val)
            print(myCursor.rowcount, "record(s) entered successfully")
            Connect.commit()
            print('''
                    ***Kindly input your details to log in...***
            ''')
            self.login()
        # else:
        #     print("Error")

    def Test(self):
        name = "Welcome...  "
        name2 = "Each question carry 2 Point...  "
        print(name)
        print(name2)
        text = ("Question 1: The president of Nigeria is?")
        print(text)
        print("""
                (a) Muhamadu Buhari
                (b) Olusegun Obasanjo
                (c) Goodluck Jonathan
        """)
        self.txt = input("Answer:   ")
        if self.txt == 'a':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x == 0
            print(f"You have {self.x} points")

        text = ("Question 2: The Capital Of Lagos is?  ")
        print(text)
        print('''
                    (a) Ojota
                    (b) Ikeja
                    (c) Surulere
        ''')
        self.txt = input("Answer:  ")
        if self.txt == 'b':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x-=0
            # x-=0
            print(f"You have {self.x} points")

        text = ("Question 3: Who is the Governor of Oyo state?  ")
        print(text)
        print('''
                    (a) Jide Sanwolu
                    (b) Ambrose Ali
                    (c) Seyi Makinde
        ''')
        self.txt = input("Answer:   ")
        if self.txt == 'c':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x-=0
            print(f"You have {self.x} points")
        
        text = ("Question 4: How many states do we have in Nigeria?   ")
        print(text)
        print('''
                    (a) 45
                    (b) 36
                    (c) 65
        ''')
        self.txt = input("Answer:   ")
        if self.txt == 'b':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect answer")
            self.x-=0
            print(f"You have {self.x} points")

        text = ("Question 5: Calcium Oxide is also called?  ")
        print(text)
        print('''
                    (a) Lime
                    (b) Quicklime
                    (c) Baking Soda
        ''')
        self.txt = input("Answer:   ")
        if self.txt == 'b':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x-=0
            print(f"You have {self.x} points")

        text = ("Question 6: Slaked Lime is also called what?  ")
        print(text)
        print('''
                   (a) Calcium Carbonate
                   (b) TetraChloroMethane
                   (c) Calcium Hydroxide
        ''')
        self.txt = input("Answer:    ")
        if self.txt == 'c':
           print("Correct Answer")
           self.x+=2
           print(f"You have {self.x} points")
        else:
           print("Incorrect Answer")
           self.x-=0
           print(f"You have {self.x} points")

        text = ("Question 7: Bicarbonate of Soda is also Called?   ")
        print(text)
        print('''
                   (a) Sodium Oxide
                   (b) Baking Soda
                   (c) Sodium Fluoride
        ''')
        self.txt = input("Answer:     ")
        if self.txt == 'b':
           print("Correct Answer")
           self.x+=2
           print(f"You have {self.x} points")
        else:
           print("Incorrect Answer")
           self.x-=0
           print(f"You have {self.x} points")

        text = ("Question 8: CSS is?    ")
        print(text)
        print('''
                    (a) Cascading Style Sheet
                    (b) Central State Security
                    (c) Concentrated Saturated Solution
        ''')
        self.txt = input("Answer:     ")
        if self.txt == 'a':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x-=0
            print(f"You have {self.x} points")

        text = ("Question 9: Plaster of Paris is made of?   ")
        print(text)
        print('''
                   (a) Carcinogenic Material
                   (b) Gypsum
                   (c) Phosphate Oxide
        ''')
        self.txt = input("Answer:   ")
        if self.txt == 'b':
           print("Correct Answer")
           self.x+=2
           print(f"You have {self.x} points")
        else:
           print("Incorrect Answer")    
           self.x-=0
           print(f"You have {self.x} points")

        text = ("Question 10: Who is Aristotle?   ")
        print(text)
        print('''
                    (a) French Biologist
                    (b) Greek Philosopher
                    (c) Russian Scientist
        ''')
        self.txt = input("Answer:  ")
        if self.txt == 'b':
            print("Correct Answer")
            self.x+=2
            print(f"You have {self.x} points")
        else:
            print("Incorrect Answer")
            self.x-=0
            print(f"You have {self.x} points")
        mark = (f"Your Total score is {self.x}")
        print(mark + " points")
        result = [self.x]
        Confirm_Password = input("Password:   ")
        myquery = "UPDATE test SET Score = %s WHERE Confirm_Password = %s"
        # myquery = "INSERT INTO test (Score) WHERE Confirm_Password = %s"
        val = (result, Confirm_Password)
        # myCursor.executemany((myquery, val),())
        myCursor.execute((myquery, val), ())
        Connect.commit()
        print(myCursor.rowcount, "score inserted successfully")
    def Result(self):
        # mark = (f"Your Score is {self.x} points")
        # print(mark)
        Full_Name = input("Full_Name:    ")
        Confirm_Password = input("Password:   ")
        query = "SELECT Score FROM test WHERE Full_Name =%s AND Confirm_Password =%s"
        val = (Full_Name, Confirm_Password)
        myCursor.execute(query,val)
        Connect.commit()
        myreg = myCursor.fetchone() 
        print(myreg)





p = Exam()
# p.tet()
# p.Login()
# p.Test() 
# sql = 'DROP DATABASE Cbt_Exam'
# myCursor.execute(sql)