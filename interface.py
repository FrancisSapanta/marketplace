from combat import combat_acc
from lifeskill import lifeskill_acc
import math
print("BDO Marketplace\n")



acc_group = int(input("1. Combat Accessories \n2. Lifeskill Accessories\n3. Custom Price\n"))

if acc_group not in [1,2,3]: print("Invalid Request")

acc_type = int(input("\n1. Rings\n2. Earring\n3. Necklace\n4. Belt\n"))

if acc_group == 1:
    print(combat_acc(acc_type))  

elif acc_group == 2:
    print(lifeskill_acc(acc_type))

elif acc_group == 3:
    base_price = int(input("Price of base accessory in millions"))
    goal_level = int(input("Enchantment level for goal accessory"))
    goal_cost = int(input("Marketplace price for goal accessory"))
    total_cost = (base_price + base_price*goal_level)

    success_rates = {
        1 : .7,
        2 : .5,
        3 : .45,
        4 : .3,
        5 : .1
    }
    rates_list = []
    for level, rates in success_rates.items():
        print(rates)
        rates_list.append(rates)
        if level == goal_level:
            break
    print(rates_list)
        
    
    print("Success rate is {}% with a {} million silver investment".format(math.prod(rates_list), total_cost))
    print("Estimated profit of {} million".format((goal_cost*(0.8))-total_cost))



78