##project
chocolate=50
chips=30
colddrink=25
icecream=40
#menu
print("-----------MINI STORE----------")
print("welcome to stire menu")
print("1. CHOCOLATE",chocolate)
print("2. CHIPS",chips)
print("3. COLDDRINK",colddrink)
print("4. ICECREAM",icecream)

choice=int(input("enter your choice (1-5):")) 
qty=0
subtotal=0
match choice:
    case 1:
        print("chocolate - 50rs.")
        qty=int(input("how much qty you wants"))
        subtotal=chocolate*qty
    case 2:
        print("chips - 30 rs.")   
        qty=int(input("how much qty you wants")) 
        suntotal=chips*qty
    case 3:
        print("colddrink - 25rs")    
        qty=int(input("how much qty you wants to buy"))
        subtotal=colddrink*qty
    case 4:
        print("icecream- 40 rs.")
        qty=int(input("how much qty you wants"))
        subtotal=icecream*qty
print("subtotal will be:",subtotal)    

#discount
discount=0

if subtotal>200:
    discount=0.1*subtotal
else :
    print("no discount available")

#  qty
if qty>5:
    discount=5*choice
    print("discount applies")
else:
    print("no discount applies")    


#totalafterdiscount
totalafterdiscount=subtotal-discount
print("totalafterdiscount",totalafterdiscount)

#delievery
delievery=0
if totalafterdiscount>300:
    delievery=0
else:
    delievery=30

print("delivery will be",delievery)

#finalamount
finalamount=0
finalamount=totalafterdiscount+delievery
print("finalamount",finalamount)

#BIlling FEatures
print("-----BILLING FEATURES--------")
print("your choice",choice)
print(" your qty of your choice",qty)
print("discount applies",discount)
print("totalafterdiscount",totalafterdiscount)
print(" delievery eill br",delievery)
print("your final amount will be",finalamount)


