def number_inventory(inventory):
    for number, (item, quantity) in enumerate(inventory.items(), start=1):
        print(f"{number}. {item} x {quantity}")