###############################################################################
#   Script Header
###############################################################################
__author__ = 'Eric Schrock'
__version__ = '3.0'
__email__ = 'eric.schrock@aptiv.com'
###############################################################################

###############################################################################
#   Libraries
###############################################################################
import sys
import random
import fileinput
from enum import Enum


###############################################################################
#   Enums
###############################################################################
class Team(Enum):
    Eric_Schrock = "Eric Schrock"
    Kin_Man_Lee = "Kin Man Lee"
    Sandeep_Borra = "Sandeep Borra"
    Kishore_Yenduri = "Kishore Yenduri"
    Devin_Jaenicke = "Devin Jaenicke"
    Ashesh_Goswami = "Ashesh Goshwami"
    Ravikumar_Vanjara = "Ravikumar Vanjara"


class Restaurant(Enum):
    Cracker_Barrel = "Cracker Barrel"
    Don_Panchos = "Don Pancho's"
    Grindstone_Charleys = "Grindstone Charley's"
    Hacienda = "Hacienda"
    Half_Moon = "Half Moon"
    Jays_Thai = "Jay's Thai"
    Lucky_Indian_Cuisine = "Lucky Indian Cuisine"
    Mancinos = "Mancino's"
    Mexican_Grill = "Mexican Grill"
    Mi_Familia = "Mi Familia"
    PASTArrific = "PASTArrific"
    Olive_Garden = "Olive Garden"
    Red_Lobster = "Red Lobster"
    Taku_Japanese_Steakhouse = "Taku Japanese Steakhouse"
    Tokyo_Cuisine = "Tokyo Cuisine"


class RestaurantType(Enum):
    American = "American"
    Asian = "Asian"
    Italian = "Italian"
    Mexican = "Mexican"


###############################################################################
#   Global Variables
###############################################################################
TEAM_FAVORITES = {Team.Eric_Schrock: Restaurant.Grindstone_Charleys,
                  Team.Kin_Man_Lee: Restaurant.Grindstone_Charleys,
                  Team.Sandeep_Borra: Restaurant.Mexican_Grill,
                  Team.Kishore_Yenduri: Restaurant.Jays_Thai,
                  Team.Devin_Jaenicke: Restaurant.PASTArrific,
                  Team.Ashesh_Goswami: Restaurant.Taku_Japanese_Steakhouse,
                  Team.Ravikumar_Vanjara: Restaurant.PASTArrific}

TEAM_BLACKLIST = {Team.Eric_Schrock: [],
                  Team.Kin_Man_Lee: [],
                  Team.Sandeep_Borra: [Restaurant.Cracker_Barrel, Restaurant.Red_Lobster],
                  Team.Kishore_Yenduri: [Restaurant.Cracker_Barrel, Restaurant.Red_Lobster],
                  Team.Devin_Jaenicke: [Restaurant.Jays_Thai],
                  Team.Ashesh_Goswami: [Restaurant.Cracker_Barrel, Restaurant.Red_Lobster],
                  Team.Ravikumar_Vanjara: [Restaurant.Cracker_Barrel, Restaurant.Red_Lobster]}

GUEST_BLACKLIST = []

LAST_RESTAURANT = Restaurant.Half_Moon

NOT_COMING = []

RESTAURANT_TYPES = {Restaurant.Cracker_Barrel: RestaurantType.American,
                    Restaurant.Don_Panchos: RestaurantType.Mexican,
                    Restaurant.Grindstone_Charleys: RestaurantType.American,
                    Restaurant.Hacienda: RestaurantType.Mexican,
                    Restaurant.Half_Moon: RestaurantType.American,
                    Restaurant.Jays_Thai: RestaurantType.Asian,
                    Restaurant.Lucky_Indian_Cuisine: RestaurantType.Asian,
                    Restaurant.Mancinos: RestaurantType.Italian,
                    Restaurant.Mexican_Grill: RestaurantType.Mexican,
                    Restaurant.Mi_Familia: RestaurantType.Mexican,
                    Restaurant.PASTArrific: RestaurantType.Italian,
                    Restaurant.Olive_Garden: RestaurantType.Italian,
                    Restaurant.Red_Lobster: RestaurantType.American,
                    Restaurant.Taku_Japanese_Steakhouse: RestaurantType.Asian,
                    Restaurant.Tokyo_Cuisine: RestaurantType.Asian}

###############################################################################
#   Classes
###############################################################################


###############################################################################
#   Main Function
###############################################################################
if __name__ == "__main__":
    # Create initial restaurants list
    restaurants = [restaurant for restaurant in Restaurant]  # Add list of area restaurants

    # Increase the chance of team favorites being selected (for everyone who is coming)
    restaurants += [TEAM_FAVORITES[key] for key in TEAM_FAVORITES.keys() if key not in NOT_COMING]

    # Increase the chance of going to restaurants blacklisted by people who are not coming
    restaurants += [restaurant for key in TEAM_BLACKLIST.keys() for restaurant in TEAM_BLACKLIST[key] if key in NOT_COMING]

    # Remove the last restaurant we went to
    restaurants = [restaurant for restaurant in restaurants if restaurant != LAST_RESTAURANT]

    # Remove restaurants similar to the last restaurant we went to
    restaurants = [restaurant for restaurant in restaurants if RESTAURANT_TYPES[restaurant] != RESTAURANT_TYPES[LAST_RESTAURANT]]

    # Remove restaurants from the guest black list
    restaurants = [restaurant for restaurant in restaurants if restaurant not in GUEST_BLACKLIST]

    # Remove blacklisted restaurants for everyone who is coming
    for key in TEAM_BLACKLIST.keys():
        if key not in NOT_COMING:
            restaurants = [restaurant for restaurant in restaurants if restaurant not in TEAM_BLACKLIST[key]]

    lunch = random.choice(restaurants)

    lunch_saved = False

    for line in fileinput.input("lunch.py", inplace=True):
       if "LAST_RESTAURANT" in line and not lunch_saved:
          sys.stdout.write('LAST_RESTAURANT = %s\n' % lunch)
          lunch_saved = True
       else:
          sys.stdout.write(line)

    print(lunch.value)

    exit(0)


###############################################################################
#   Exit Codes
###############################################################################
#
#  Code       Description
# ------  --------------------
#   0     Normal execution
#
###############################################################################

###############################################################################
#   Future Changes
###############################################################################
#
#  1. Move last restaurant to a config file
#  2. Move global variables to config files so others can use this more easily
#  3. Add team ratings for each restaurant to the probability of selecting each restaurant
#  4. Add unit tests
#  5. Move functionality out of main and into an object
#
###############################################################################

###############################################################################
#   Revision History
###############################################################################
#
#    Date        By                     Description
# MM/DD/YYYY    Name        JIRA AAA-#### Explanation of changes
# ----------  ---------     ------------------------------------
# 04/05/2019  Eric Schrock  v1.0 - Initial version
# 06/13/2019  Eric Schrock  v2.0 - Added blacklists
# 10/03/2019  Eric Schrock  v3.0 - Added restaurant types
###############################################################################
