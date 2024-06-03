Atm_card="card"
pin=1234
Money=1000
Temp=0
for outer in[1,2,3,4]:
    print("you are in front of atm machine")
    print("insert your card")
    print("enter your pin")
    if(Atm_card=="card")&(pin==1234):
        if outer<=3:
            while Temp<=Money:
                print("count",Temp,"Total Amount",Money)
                Temp=Temp+100
        else:
            print("only three atempt is possible")
            break
        print("take your money",Money,"rupee")
        Temp=0
    elif(Atm_card=="card")|(pin==1234):
        print("any one value is wrong")
    else:
        print("both values are wrong")
        print("thank you for use")