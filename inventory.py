inventory = {"laptop": 10, "mouse": 25, "keyboard": 15}
inventory["monitor"] = 5
inventory["laptop"] = 2
if inventory.get("keyboard") > 0:
   # print("Mouse: {inventory["mouse"]}")
   # print(f"Mouse: {inventory["mouse"]}")
   print("keybord is in stock")

    
for item, stock in inventory.items():
    print(f"{item}: {stock}")