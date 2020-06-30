meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]


# the list "meals" is already defined
# your code here

out = 0
for _count, value in enumerate(meals):
    out += value["kcal"]

print(out)
print(sum(x['kcal'] for x in meals))
