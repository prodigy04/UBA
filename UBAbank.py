# ASSIGNMENT 
# Mobile Banking USSD Code
class UBA:
    def __init__(self):
#To either Register Or Login
        print('''
                Welcome To UBA....
                Enter:
                    1. To Register
                    2. To Login
        ''')
        value = input("Enter your choice:  ")
        if value == '1':
            self.Register()
        elif value == '2':
            self.login()
#your login details so as to access your ussd Code, for a registered user
    def login(self):
        username = input("Enter your username:  ")
        password = input("Enter your password:  ")
        print("Kindly Proceed to perform any transactions!!!...")
        self.Transaction()
# if you are yet to register, then you have to register so as to be able to make transactions using your USSD code
    def Register(self):
        Name = input("Enter your full name:  ")
        Email = input("Enter your email address:  ")
        Password = input("Enter your password:  ")
        Confirm_Password = input("Confirm your password:  ")
        if Password == Confirm_Password:
            print("Registration Successful!")
        else:
            print("Input your Password again")
            Confirm_Password = input("Enter your Password again:   ")
        user = {"Name":Name,"Email":Email, "Password":Password, "Confirm_Password":Confirm_Password}
        print(user)
        print('''
                Enter: 
                    Yes To Log In
                      No To Exit
        ''')
        name = input("Do you want to log in?   ")
        if name == 'Yes':
            self.login()
        elif name == 'No':
            print("Thank you for choosing us!!!")
            quit()
            pass
#To perform more transactions, after Buying airtime or buying data or any other transactions...
    def More(self):
        Text = ("Would you like to perform more Transactions?  ")
        print(Text)
        print('''
                1. Yes
                2. No
        ''')
        text = input("Enter your choice:   ")
        if text == '1':
            self.Transaction()
        elif text == '2':
            quit
            pass
        else:
            print("Thank you for choosing us!")
# To buy Airtime,you need to provide your security pin
    def Airtime(self):
        Pin = input("Enter your Pin:  ")
        Number = input("Enter Destination Phone Number or the last four digits:   ")
        Amount = input("Enter Amount(50-1000):      ")
        con = ("Kindly Confirm...")
        print(''' 
                    1. Yes
                    2. No
        ''')
#Transfering airtime to a beneficiary's Number
        trans = input(f"Transfer airtime of NGN {Amount} to {Number}:   ")
        if trans == '1':
#If you will like to save beneficiary, 
            Benefit = ("Would you like to save this beneficiary?")
            print(Benefit) 
            print('''
                    1. Yes
                    2. No
            ''') 
            inter = input("  ")
            if inter == '1':
                print("Your Tranasaction is being Processed..")
                print(f"You have successfully sent {Amount} to {Number}")
            elif inter == '2':
                print(f"You have successfully sent {Amount} to {Number}")
            else:
                print("Thanks...")
# To confirm the phone number and amount incase of wrong details
        elif trans == '2':
            Number = input("Enter Destination Phone Number or the last four digits:   ")
            Amount = input("Enter Amount(50-1000):    ")
        else:
            print("Invalid Input")
        self.More()
#To buy data, you need to provide your security Pin
    def Data(self):
        Pin = input("Enter your Pin:  ")
        Number = input("Enter Destination Phone Number or the last four digits:   ")
        Dat = input("How much data will you to send?   ")
        con = ("Kindly Confirm...")
        print(''' 
                    1. Yes
                    2. No
        ''')
        trans = input(f"Transfer airtime of NGN {Dat} to {Number}:   ")
        if trans == '1':
            Benefit = ("Would you like to save this beneficiary?")
            print(Benefit) 
            print('''
                    1. Yes
                    2. No
            ''') 
            inter = input("  ")
#For Successful transactions,
            if inter == '1':
                print("Your Tranasaction is being Processed..")
                print(f"You have successfully sent {Dat} to {Number}")
            elif inter == '2':
                print(f"You have successfully sent {Dat} to {Number}")
            else:
                print("Thanks...")
#Incase of wrong phone number, and data amount,proper confirmation
        elif trans == '2':
            Number = input("Enter Destination Phone Number or the last four digits:   ")
            Dat = input("How much data will you to send?   ")
        else:
            print("Invalid Input")
        self.More()
#to make transfer to beneficiaries, 
    def Transfer(self):
        Pin = input("Enter your Pin:   ")
#You have to input the beneficiary's bank name, to know if the transfer will be done to same bank, other banks, or microfinance banks
        Bank = input("Enter the Beneficiary's Bank:   ")
#You have to input the beneficiary's account Number
        Account_Number = input("Enter the Beneficiary's Account Number:   ")
        Amount = input("Please Enter Amount(amount greater than NGN 20,000 will require Secure Pass):   ")
#Proper Confirmation
        print(f"Send Money to {Account_Number}?  ")
        print('''
                    1. Yes
                    2. No
        ''')
        Option = input("Do you wish to continue?   ")
        if Option == '1':
            Benefit = ("Would you like to save this beneficiary?")
            print(Benefit) 
            print('''
                    1. Yes
                    2. No
            ''') 
            inter = input("  ")
            if inter == '1':
                print("Your Tranasaction is being Processed..")
                print(f"You have successfully sent {Amount} to {Account_Number} {Bank}")
            elif inter == '2':
                print(f"You have successfully sent {Amount} to {Account_Number} {Bank}")
            else:
                print("Thank you for choosing us!!!...")
        else:
            print("Kindly Confirm Again")
        self.More()
#Here you have your hidden Balance
    def Balance(self):
        Bal = ("Your Balance is ******")
        print(Bal)
#Here you have lists of transactions to make, like buying airtime, buying data, and making transfers to same bank, other banks, or microfinance banks, and checking balance
    def Transaction(self):
        self.inp = input("Enter your code:  ")
#Here you have to supply your UBA banking USSD code to perform any transactions
        if self.inp == "*919#":
            print('''
                    1. Buy Airtime 
                    2. Buy Data
                    3. Transfer - UBA
                    4. Transfer - Other Banks
                    5. Transfer - Microfinance Banks
                    6.  Check Balance
                    7. Next
            ''')
            option = input("Enter your choice:  ")
        else:
            print("Invalid Code")
#Making transactions,,
        if option == '1':
            self.Airtime()
        elif option == '2':
            self.Data()
        elif option == '3':
            self.Transfer()
        elif option == '4':
            self.Transfer()
        elif option == '5':
            self.Transfer()
        elif option == '6':
            self.Balance()
        elif option == '7':
            Exit()
####Enjoy!!!
m = UBA()
# m.cod1()



