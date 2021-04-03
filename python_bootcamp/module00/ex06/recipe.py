cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def add_recipe(recipe):
    ingredients = input("please enter ingredients separated by only a comma: ")
    ingredients = ingredients.split(',')
    meal = input("please enter type of meal (e.g. breakfast): ")
    prep_time = input("please enter prep time with unit measure: ")
    cookbook[recipe] = {"ingredients": (ingredients), "meal": meal, "prep_time": prep_time}
    print(f"\nYou have successfully added the recipe {recipe} to the cookbook")


def delete_recipe(recipe):
    try:
        cookbook.pop(recipe)
        print(f"\nYou have successfully deleted the recipe {recipe}")
    except:
        print(f"\nThe recipe {recipe} does not exist in the cookbook")


def print_recipe(recipe):
    try:
        cookbook[recipe]
        print(f"\n{recipe}:")
        print(f"Ingredients: {cookbook[recipe]['ingredients']}.")
        print(f"To be eaten for {cookbook[recipe]['meal']}.")
        print(f"Takes {cookbook[recipe]['prep_time']} of cooking.")
    except:
        print(f"\nThe recipe {recipe} does not exist in the cookbook")


def print_cookbook():
    print(f"\nThis cookbook contains {len(cookbook.keys())} recipes")
    for i in cookbook.keys():
        print_recipe(i)


if __name__ == "__main__":
    option = ''
    print("Please select an option by typing the corresponding number:")
    while option != '5':
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        option = input()
        if option == '1':
            recipe = input("\nPlease type the recipe name: ")
            add_recipe(recipe)
        elif option == '2':
            recipe = input("\nPlease type the name of the recipe you want to delete: ")
            delete_recipe(recipe)
        elif option == '3':
            recipe = input("\nPlease type the name of the recipe you want to print: ")
            print_recipe(recipe)
        elif option == '4':
            print_cookbook()
        elif option == '5':
            break
        else:
            print("\nThis option does not exist.", end='')
        print("\nPlease select another option.")
    print("Cookbook closed.")