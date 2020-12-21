#!/usr/local/bin/python3.9

# Advent of Code 2020
# Day 21

f = open('input.txt', 'r')
lines = [line.strip() for line in f]

courses = []

allIngredients = set()
allAllergerns = set()
for line in lines:
    part = line.split(' (contains ')

    ingredients = part[0].split(' ')
    allergens = part[1][:-1].split(', ')

    courses.append([ingredients, allergens])

    allIngredients |= set(ingredients)
    allAllergerns |= set(allergens)

ingredientsWithAllergen = {}
for allergen in allAllergerns:
    ingredientsWithAllergen[allergen] = set(allIngredients)
for ingredients, allergens in courses:
    for allergen in allergens:
        ingredientsWithAllergen[allergen] &= set(ingredients)


# Part One:
# How many times do any of those ingredients appear?
ingredientsWithoutAllergen = set(allIngredients)
for _, ingredients in ingredientsWithAllergen.items():
    ingredientsWithoutAllergen -= ingredients

count = 0
for ingredients, allergens in courses:
    for ingredient in ingredients:
        if ingredient in ingredientsWithoutAllergen:
            count += 1

print("Part One:", count)


# Part Two:
# What is your canonical dangerous ingredient list?

ingredientForAllergen = {}
while ingredientsWithAllergen:
    for allergen, ingredients in ingredientsWithAllergen.items():
        if len(ingredients) == 1:
            ingredient = list(ingredients)[0]
            break

    ingredientForAllergen[allergen] = ingredient
    del ingredientsWithAllergen[allergen]

    for ingredients in ingredientsWithAllergen.values():
        ingredients -= set([ingredient])

result = list(ingredientForAllergen.items())
result.sort()
result = [ingredient for (_, ingredient) in result]

print('Part Two:', ','.join(result))

