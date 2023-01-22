from combat import combat_acc
from lifeskill import lifeskill_acc
print("BDO Marketplace\nChoose .")

acc_group = int(input("1. Combat Accessories \n2. Lifeskill Accessories\n"))

if acc_group not in [1,2]: print("Invalid Request")

acc_type = int(input("\n1. Rings\n2. Earring\n3. Necklace\n4. Belt\n"))

if acc_group == 1:
    print(combat_acc(acc_type))  

elif acc_group == 2:
    print(lifeskill_acc(acc_type))




