fn = "input.txt"
fn = "test.txt"

# parse the data
data = []
for line in open(fn):
    ingredients, allergens = line.split(' (contains ')
    ingredients = set(ingredients.split(' '))
    allergens= [x.strip() for x in allergens.replace(')','').split(', ')]
    data.append((ingredients, allergens))

# populate the pantry with all ingredients and
# create initial food allergen associations 
pantry   = set()
possible = dict()
for ingredients, allergens in data:
    pantry.update(ingredients)
    for allergen in allergens:
        if allergen not in possible:
            possible[allergen] = ingredients
        else:
            possible[allergen] = possible[allergen].intersection(ingredients)

# iteratively isolate the unique allergen/food pairs
mapping = dict()
while True:
    isolated = len(mapping)
    allergens = list(possible.keys())
    for allergen in allergens:
        if len(possible[allergen]) == 1:
            ingredient = possible[allergen].pop()
            mapping[ingredient] = allergen
            pantry.remove(ingredient)

    # remove identified
    for key in possible:
        possible[key] = possible[key].difference(mapping)

    if isolated == len(mapping):  
        break  # because there were no changes

# extract the answers
count = 0
for ingredients, _ in data:
    for ingredient in ingredients:
        count += ingredient in pantry
print('Part 1:', count)

mapping = dict(sorted(mapping.items(), key=lambda item: item[1]))
print('Part 2:', ','.join(mapping))