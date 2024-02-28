spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
       names.append(food["name"])
    return names

print(get_names(spicy_foods))
pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [spicy for spicy in spicy_foods if spicy["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return (food)
        
pass

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
pass


def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
pass
