# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: clwenhaj <clwenhaj@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 11:24:16 by clwenhaj          #+#    #+#              #
#    Updated: 2026/07/17 13:12:05 by clwenhaj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:

    def __init__(
        self,  
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients = list[str],
        description = str,
        recipe_type = str
    ):
      
        # name
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        
        #cooking level
        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl must be an integer")
        if not 1 <= cooking_lvl <= 5:
            raise ValueError("cooking_lvl must be between 1 and 5")
        
        #cooking time
        if not isinstance(cooking_time, int):
            raise TypeError("cooking_time must be an integer")
        if cooking_time < 0:
            raise ValueError("cooking_time cannot be negative")
        
        #ingredients
        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list")
        if len(ingredients) == 0:
            raise ValueError("ingredients cannot be empty")
        if not all(isinstance(i, str) for i in ingredients):
            raise TypeError("all ingredients must be strings")
        
        #description
        if not isinstance(description, str):
            raise TypeError("description must be a string")
        
        #recipe type
        if recipe_type not in ("starter", "lunch", "dessert"):
            raise ValueError('recipe_type must be "starter", "lunch" or "dessert"')
        
        # Assign attributes
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type


# The built-in method __str__ helps define the 
# readable representation of an object

    def __str__(self):
    
        """Returns the string to print with the recipe’s info"""
        ingredients = ", ".join(self.ingredients)
        """Your code here"""
        return (
            f"Recipe: {self.name}\n"
            f"Type: {self.recipe_type}\n"
            f"Difficulty: {self.cooking_lvl}/5\n"
            f"Cooking time: {self.cooking_time}\n"
            f"Ingredients: {ingredients}\n"
            f"Description: {self.description}\n"
            )

recipe = Recipe(
    name="pizza",
    cooking_lvl=5,
    cooking_time=30,
    ingredients=["mozza", "tomato", "cheese"],
    description="Recipe for a delicious pizza",
    recipe_type="lunch",
)
print()
print(recipe.name)
print(recipe.description)
print(recipe.ingredients)
print()

tourte = Recipe(
    "Tourte aux pommes",
    2,
    60,
    ["pommes", "farine", "beurre", "sucre"],
    "Une délicieuse tourte.",
    "dessert",)

to_print = str(tourte)
print(tourte)