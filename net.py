# MTN Network Transaction
#Welcome To MTN Network Transaction
class Code:
    def __init__(self):
        print("Welcome to MTN...")
        self.first()
    def first(self):
#Here you have to input your mtn transaction code....
        inp = input(" Enter your MTN Transaction code:   ")
        if inp == "*131#":
#To perform any of the below transactions
            print('''
                    (1). Data Plans
                    (2). Social Bundles
                    (3). Balance Check    
                    (4). Roaming/Int'l
                    (5). Borrow Credit/Recharge
                    (6). Gift Data
                    (7). Video Packs
                    (8). Hot Deals
            ''')
        value = input("Enter your choice:   ")
        if value == '1':       
            print('''
                Buy Data Plans
                1.  Daily
                2.  Weekly
                3.  Monthly
                4.  2-3Month
                5.  Always ON Plans
                6. Broadband Plans
                7. Family Packs
                8. Hot Deals
                9. 5G Plans
            ''')
        elif value == '2':
            print('''
                    1. Whatsapp
                    2. Facebook
                    3. Instagram
                    4. TikTok
                    5. Ayoba
                    6. All Social Bundles
                    7. YouTube, Instagram and TikTok
                    8. Opera Mini & News
                    9. Social Mega Bundles
                    99.Next    
            ''')
        elif value == '3':
            print('''
                    Your data balance:
                    Daily: 1034mb expires 28/08/2022
                    Monthly: 2346mb expires 28/09/2022
                    Youtube Night: 342mb expires 20/08/2022
            ''')
        elif value == '4':
            print('''
                        1. TravelPass Plans
                        2. Data Hybrid
                        3. Infligth Roaming Data
                        4. Free incoming roaming call
                        5. Int'l calling Bundle
                        6. Roaming Balance Check
            ''')
        elif value == '5':
            print('''
                    1. Borrow Airtime
                    2. Borrow Data
                    3. Recharge
                    0. Back
            ''')
        elif value == '6':
            print('''
                    1. Transfer From Data Recharge
                    2. Buy for a friend
                    3. Request from a friend
                    4. View Pending request
                    0. Back
                    00. Main Menu
            ''')
        elif value == '7':
            print('''
                   Video Streaming Packs
                    1. Youtube Video Packs
                    2. StarTimes Video Packs
                    3. 1GB(YouTube Only) + 500MB (Data Access)
                    4. Showmax Mobile
            ''')
        elif value == '8':
            print('''
                    1. TopDeal4ME
                    2. Data4ME
                    3. Recharge4ME
                    4. VAS4ME
            ''')
        else:
            print("Invalid Input") 


c = Code()