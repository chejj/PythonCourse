# List Comprehensions

One of the main ways to create a new list from an existing one is to use `for` loops. This allows us to [iterate](https://en.wikipedia.org/wiki/Iteration) through each item and apply conditional logic at every step.

For example, say I want to create a new list containing only Pokémon whose names contain "chu".

```python
pokemon = ["Pikachu", "Charizard", "Blastoise", "Venusaur", "Raichu"]
new_list = []

for x in pokemon:
    if "chu" in x:
        new_list.append(x)

print(new_list)
# ["Pikachu", "Raichu"]
```

While this works perfectly well, Python provides a more concise syntax called a `list comprehension` for creating lists. The same code can be written as:

```python
pokemon = ["Pikachu", "Charizard", "Blastoise", "Venusaur", "Raichu"]
new_list = [x for x in pokemon if "chu" in x]

print(new_list)
# ["Pikachu", "Raichu"]
```

## Why use a List Comprehension?
`List comprehensions` are generally considered easier and cleaner to read, and are often faster than manually building a list with a traditional for loop.

## Assignment
Fantasy Quest logs every attack made during combat, but we only want to review successful attacks (__attacks with values greater than 0__). Complete the `check_attacks` function using a list comprehension. It takes a list of integers, `attacks`, and returns a new list.