from sheets import get_sheet
def combat_acc(acc_type):
    combat_value_dict = {
         1: "combat rings",
         2: show_combat_earrings(),
         3: "combat necklace",
         4: "combat belt",
    }
    return combat_value_dict.get(acc_type, "Invalid Request")

def show_combat_earrings():
     combat_earrings_dict = {
          1: "Black Distortion Earring",
          2: "Tungrad Earring",
          3: "Narc Earring Accessory",
          4: "Vaha's Dawn",
          5: "Dawn Earring",
          6: "Ethereal Earring"
     }

     for key, value in combat_earrings_dict.items():
          print(key, "-", value)