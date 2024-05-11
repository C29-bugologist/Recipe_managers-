class RecipeManager:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, name, ingredients, instructions):
        self.recipes[name] = {"Ingredients": ingredients, "Instructions": instructions}
        print(f"Recipe for {name} added successfully!")

    def delete_recipe(self, name):
        if name in self.recipes:
            del self.recipes[name]
            print(f"Recipe for {name} deleted successfully!")
        else:
            print(f"No recipe found with the name {name}.")

    def view_recipe(self, name):
        if name in self.recipes:
            recipe = self.recipes[name]
            print(f"Recipe: {name}")
            print("Ingredients:")
            for ingredient in recipe["Ingredients"]:
                print(f"- {ingredient}")
            print("Instructions:")
            for step, instruction in enumerate(recipe["Instructions"], 1):
                print(f"{step}. {instruction}")
        else:
            print(f"No recipe found with the name {name}.")


def main():
    manager = RecipeManager()

    while True:
        print("\nRecipe Manager Menu:")
        print("1. Add Recipe")
        print("2. Delete Recipe")
        print("3. View Recipe")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(",")
            instructions = input("Enter instructions (one step per line, end with 'done'): ").splitlines()
            manager.add_recipe(name, ingredients, instructions)
        elif choice == "2":
            name = input("Enter recipe name to delete: ")
            manager.delete_recipe(name)
        elif choice == "3":
            name = input("Enter recipe name to view: ")
            manager.view_recipe(name)
        elif choice == "4":
            print("Exiting Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
