# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: clwenhaj <clwenhaj@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 13:13:10 by clwenhaj          #+#    #+#              #
#    Updated: 2026/07/17 14:58:48 by clwenhaj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from datetime import datetime

class Book:
    def __init__(
        self,
        name: str,
    ):
        
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        
        self.name = name
        self.creation_date = datetime.now
        self.last_update = self.creation_date
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print("Recipe not found")
        return None   

    def get_recipes_by_types(self, recipe_type):
        
        if recipe_type not in self.recipes_list:
            raise ValueError("Unknown recipe type")
        for recipe in self.recipes_list[recipe_type]:
            print(recipe.name) 
              
    def add_recipe(self, recipe):
        
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be a Recipe object")
        
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now
            