def lifeskill_acc(acc_type):
    lifeskill_value_dict = {
         1: "lifeskill rings",
         2: "lifeskill earrings",
         3: "lifeskill necklace",
         4: "lifeskill belt",
    }
    return lifeskill_value_dict.get(acc_type, "Invalid Request")