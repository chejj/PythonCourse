# Enumerate


The built-in <mark>enumerate()</mark> function takes an iterable and pairs each item with a number. By default, this number starts at `0` and increases by ==1== for each item.

This is useful when you need both the position of an item and the item itself while iterating.
```
inventory = ["Sword", "Shield", "Bow", "Boomerang"]

for index, item in enumerate(inventory):
    print(f"{index}: {item}")

# prints:
# 0: Potion
# 1: Sword
# 2: Shield
# 3: Bow
```

While indices in Python start at 0, we can use the optional <mark>start</mark> parameter to choose a new starting value. Note that this means if we use <mark>start=1</mark>, we will still start at index 0, but the first value paired with the item at index 0 will be 1.

