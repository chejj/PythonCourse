# Enumerate

The built-in `enumerate()` function takes an iterable and pairs each item with a number creating an `enumerate object`. By default, this number starts at `0` and increases by `1` for each item.

This is useful when you need both the position of an item and the item itself while iterating.

```python
inventory = ["Sword", "Shield", "Bow", "Boomerang"]
enum_obj = enumerate(inventory)
print(enum_obj)
# <enumerate object at 0x0...>
```

By itself, an `enumerate` object doesn't display its contents. However, we can convert it into a list to see what it contains.

```python
print(list(enum_obj))
# [(0, 'Sword'), (1, 'Shield'), (2, 'Bow'), (3, 'Boomerang')]
```

Notice that each element is a tuple containing a number and an item from the original list.

The most common way to use `enumerate()` is to unpack each tuple inside a `for` loop.

```python
inventory = ["Sword", "Shield", "Bow", "Boomerang"]

for index, item in enumerate(inventory):
    print(f"{index}: {item}")

# 0: Sword
# 1: Shield
# 2: Bow
# 3: Boomerang
```

By default, the numbers produced by `enumerate()` begin at `0`. If you'd like to start from a different number, you can use the optional `start` parameter.

```python
inventory = ["Sword", "Shield", "Bow", "Boomerang"]

for number, item in enumerate(inventory, start=1):
    print(f"{number}: {item}")

# 1: Sword
# 2: Shield
# 3: Bow
# 4: Boomerang
```

Keep in mind that the `start` parameter **does not change the indices of the iterable**. It only changes the numbers that `enumerate()` pairs with each item. In this example, `"Sword"` is still stored at index `0` in the list, but `enumerate()` pairs it with the number `1`.

## Assignment (Hard) (this assignment only works after the dictionary section)

Fantasy Quest stores a player's inventory as a dictionary where the key is the item's name and the value is the quantity they own.

```python
inventory = {
    "Ice Arrow": 5,
    "Ocarina": 1,
    "Bomb": 2,
}
```

Complete the `number_inventory` function. It takes a dictionary, inventory, and prints the inventory in a numbered format.

1. Use `enumerate()` to number each item, starting at `1`.
2. Format each line as "<number>. <item> x<quantity>".
    For example, the key-value pair `"Ice Arrow": 5` should print `1. Ice Arrow x5.`
3. Print each item on its own line.

**Hint:** Iterate over the dictionary using `.items()`. Each item returned by `.items()` is a (key, value) tuple that can be unpacked while using enumerate().