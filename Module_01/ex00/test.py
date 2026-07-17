# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: clwenhaj <clwenhaj@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 11:23:24 by clwenhaj          #+#    #+#              #
#    Updated: 2026/07/17 14:53:58 by clwenhaj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

book = Book("My cookbook")

pizza = Recipe(
    "Pizza",
    4,
    30,
    ["Dough", "Tomato", "Mozzarella"],
    "Italian pizza",
    "lunch"
)

cake = Recipe(
    "Chocolate cake",
    2,
    45,
    ["Flour", "Eggs", "Chocolate"],
    "",
    "dessert"
)

book.add_recipe(pizza)
book.add_recipe(cake)

book.get_recipes_by_types("lunch")

book.get_recipe_by_name("Chocolate cake")