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

# We have a list of dictionaries above, we want to get each item it it and from each item we have to get each name 
# Start by iterating over our list so we can get each item in the dictionary(which is the item )


def get_names(spicy_foods):

    foods = []

    for food in spicy_foods: 
        foods.append(food["name"])

    # return foods 

    return[food["name"] for food in spicy_foods]

    
# print(get_names(spicy_foods))



#Will be returning list of dictionaries and keep track of heat level
def get_spiciest_foods(spicy_foods):
    foods= []
    
    for food in spicy_foods:
        if food["heat_level"] > 5:
            foods.append(food)

    return [food for food in spicy_foods if food["heat_level"] > 5]




#print(): Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
# HINT: you can use times (*) with a string to produce the correct number of "🌶" emojis.

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        country = food["cuisine"]
        heat = food["heat_level"] * "🌶"

        print(f"{name} ({country}) | Heat Level: {heat}")    



# Returns a single item 
# Match cuisine key to whatever this is 
# Iterate over spicy_foods

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

#Not returning a list, just returning a single item 
# We have spicy_foods and taking the ones greater than 5, since it has return value itll return list of dicitionaries so take that list and put it in print spicy_foods and itll print out every food that has spicy level greater than 5 
#Buffalo Wings (American) | Heat Level: 🌶🌶🌶.
def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))


# Take in list, and get all the heat levels, add them up and divide by number of heat levels.
def get_average_heat_level(spicy_foods):
    #create a sum locally 
    #sum  = sum + 1
    sum = 0

    for food in spicy_foods:
        heat  = food["heat_level"]
        sum += heat

    average = sum / len(spicy_foods)

    return average


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    
    return spicy_foods




def sort_spicy_foods(spicy_foods):
    heat_levels = [food["heat_level"] for food in spicy_foods]

    heat_levels.sort()

    return heat_levels

# a lambda expression can be used within the `sort` function here
# in order to get the "heat_level" key:value pair when creating
# a list of each dictionary rather than each integer