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
    names =[key["name"] for key in spicy_foods]
    return names
print(get_names)




def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
         heat_emoji = "🌶"* food["heat_level"]
         print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
   return next(food for food in spicy_foods if food["cuisine"] == cuisine)


def print_spiciest_foods(spicy_foods):
     for food in get_spiciest_foods(spicy_foods):  # reuse the filtering function
        heat_emoji = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_emoji}")
    

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    count = len(spicy_foods)
    return total_heat // count  # Return the average heat level as an integer

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods