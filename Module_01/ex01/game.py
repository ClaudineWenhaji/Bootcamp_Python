# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: clwenhaj <clwenhaj@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/17 16:43:22 by clwenhaj          #+#    #+#              #
#    Updated: 2026/07/17 17:55:52 by clwenhaj         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
    
    def __init__(self, first_name, is_alive=True):
        
        self.first_name = first_name
        self.is_alive = is_alive
        
class Stark(GotCharacter):
        
        family_name = "Stark"
        house_words = "Winter is coming"
        
        # super( appelle methodes ou constructeur de la classe mere)
        
        def __init__(self, first_name, is_alive=True):
              super().__init__(first_name, is_alive)
              self.family_name = self.family_name
              self.house_words = self.house_words
              
        def print_house_words(self):
              print(self.house_words)
              
        def die(self):
              self.is_alive = False

