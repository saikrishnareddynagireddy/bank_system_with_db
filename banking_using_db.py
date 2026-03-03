import sqlite3
import hashlib

conn = sqlite3.connect('bank.db')
cursor= conn.cursor()
#create table
cursor.execute("""
               create table if not exists accounts(
                   account_number integer primary key,
                   name text not null,
                   password text not null,
                   balance real not null
                     
               )
               """)   
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Banksystem:
    def create_account(self,):
        name=input("enter your name:")
        password=input("enter your password:")
        balance=float(input("enter initial deposit amount:"))
        hashed_password=hash_password(password)
        cursor.execute("insert into accounts(name,password,balance) values(?,?,?)",(name,hashed_password,balance))
        conn.commit()
        print("account created successfully!!")
        print(f"your account number is: {cursor.lastrowid}")
        
    def authenticate(self,account_number,password):
        hashed_password=hash_password(password)
        cursor.execute("select * from accounts where account_number=? and password=?",(account_number,hashed_password))
        return cursor.fetchone()
    
    def deposit(self):
        acc_num=int(input("enter your account number:"))
        password=input("enter your password:") 
        if self.authenticate(acc_num,password):
            amount=float(input("enter amount to deposit:"))
            cursor.execute("select balance from accounts where account_number=?",(acc_num,))
            balance=cursor.fetchone()[0]
            new_balance=balance+amount
            cursor.execute("update accounts set balance=? where account_number=?",(new_balance,acc_num))
            conn.commit()
            print("deposit successful!!")
        else:
            print("authentication failed!!")
        
    def withdraw(self):
            acc_num=int(input("enter your account number:"))
            password=input("enter your password:") 
            if self.authenticate(acc_num,password):
                amount=float(input("enter amount to withdraw:"))
                cursor.execute("select balance from accounts where account_number=?",(acc_num,))
                balance=cursor.fetchone()[0]
                if amount>balance:
                    print("insufficient funds!!")
                else:
                    new_balance=balance-amount
                    cursor.execute("update accounts set balance=? where account_number=?",(new_balance,acc_num))
                    conn.commit()
                    print("withdrawal successful!!")
            else:
                print("authentication failed!!")
        
    def check_balance(self):
            acc_num=int(input("enter your account number:"))
            password=input("enter your password:") 
            if self.authenticate(acc_num,password):
                cursor.execute("select name,balance from accounts where account_number=?",(acc_num,))
                result=cursor.fetchone()
                print(f"name:{result[0]}")
                print(f"your current balance is: {result[1]}")
            else:
                print("authentication failed!!")
                
def main():
    bank= Banksystem()
    while True:
        print("\n=====welcome to the banking system=====")
        print("1. create account")
        print("2. deposit")
        print("3. withdraw")
        print("4. check balance")
        print("5. exit")
        choice=input("enter your choice(1-5):").strip()
        if choice=="1":
            bank.create_account()
        elif choice=="2":
            bank.deposit()
        elif choice=="3":
            bank.withdraw()
        elif choice=="4":
            bank.check_balance()
        elif choice=="5":
            print("thanks for using our banking system!!")
            break
        else:
            print("invalid choice!!")

if __name__=="__main__":
    main()
    conn.close()
