import os
os.system ('clear')


class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    




        #deposit start
    def deposit(self,dep_amt):
        self.balance = dep_amt + self.balance
        print('Deposit Accepted of amt : {}' .format(dep_amt))
        print('Current amt : {}' .format(self.balance))
        


        #withdraw start 
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance =  self.balance - wd_amt
            print('Withdrawal Accepted of amt : {}' .format(wd_amt))
            print('Current amt : {}' .format(self.balance))

        #funds not avail start
        else:    
            print('Funds not Unavailable!')
            Loan = wd_amt - self.balance
            print("\nYou are taking loan of {}" .format(Loan) )
       	
            answer = input('Are u sure? ')
            y = 'yes'
            n = 'no'
            if answer == y :
             print(" \n Now you are in dedt of {}" .format(Loan))
             ans = input("\n Interst rate is 10% \n Do you want to continue?")
                
            if ans == y:
                years = int(input(" \n In how many years you will return money to the bank?"))
                simple_compound = input("\nPress one to pay monthly installment and get 4 month free installment \n or \n Press two to pay annually \n\n 1 = monthly = compound interest \n 2= annually = simple interest \n :")
                one = '1'
                two = '2'
    
                if simple_compound == one:
                 compound_interest = Loan * (1 + 10/12)**(years/12) - 4
                 total_compound = compound_interest + Loan
                 print("\n You chose compound interest method so,\n You have to pay Rs.{} icluding your interst of {} " .format(round (total_compound ,2) , round(compound_interest , 2)))

                elif simple_compound == two:
                 interst_r = 10/100* Loan * years
                 round(interst_r, 2)
                 total_amount = interst_r + Loan
                 print("\n You chose simple interest method so , \n You have to pay Rs.{} including your interst of {} " .format (round(total_amount , 2), round(interst_r , 2)))
                
                else:
                 print("You have to choose 1 or 2")
            elif answer == n :
              print("\n As you say, loan not granted")

            else:
             print("\n As you say, loan not granted")

        
              
       



acc_1 = Account("Sanat" , 10000)
acc_2 = Account("Aditya" , 1000000)
acc_3 = Account("Aditi" , 100000)


















