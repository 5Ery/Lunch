###############################################################################
#   Script Header
###############################################################################
__author__ = 'Eric Schrock'
__version__ = '2.0.0'
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
    Satish_Vaishnav = "Satish Vaishnav"
    Kishore_Yenduri = "Kishore Yenduri"
    Devin_Jaenicke = "Devin Jaenicke"
    Ashesh_Goswami = "Ashesh Goshwami"

class Restaurant(Enum):
    Grindstone_Charleys = "Grindstone Charley's"
    PASTArrific = "PASTArrific"
    Don_Panchos = "Don Pancho's"
    Mexican_Grill = "Mexican Grill"
    Hacienda = "Hacienda"
    Jays_Thai = "Jay's Thai"
    Red_Lobster = "Red Lobster"
    Olive_Garden = "Olive Garden"
    Mancinos = "Mancino's"
    Half_Moon = "Half Moon"
    Mi_Familia = "Mi Familia"
    Taku_Japanese_Steakhouse = "Taku Japanese Steakhouse"
    Cracker_Barrel = "Cracker Barrel"
    Tokyo_Cuisine = "Tokyo Cuisine"
    Lucky_Indian_Cuisine = "Lucky Indian Cuisine"


###############################################################################
#   Global Variables
###############################################################################
TEAM_FAVORITES = {Team.Eric_Schrock: Restaurant.Grindstone_Charleys,
                  Team.Kin_Man_Lee: Restaurant.Grindstone_Charleys,
                  Team.Sandeep_Borra: Restaurant.Mexican_Grill,
                  Team.Satish_Vaishnav: Restaurant.PASTArrific,
                  Team.Kishore_Yenduri: Restaurant.Jays_Thai,
                  Team.Devin_Jaenicke: Restaurant.PASTArrific}

TEAM_BLACKLIST = {Team.Devin_Jaenicke: [Restaurant.Jays_Thai]}

GUEST_BLACKLIST = []

LAST_RESTAURANT = Restaurant.PASTArrific

NOT_COMING = []


###############################################################################
#   Classes
###############################################################################


###############################################################################
#   Main Function
###############################################################################
if __name__ == "__main__":
    # Create initial restaurants list
    restaurants = [r for r in Restaurant]  # Add list of area restaurants

    # Increase the chance of team favorites being selected (for everyone who is coming)
    restaurants += [TEAM_FAVORITES[key] for key in TEAM_FAVORITES.keys() if key not in NOT_COMING]

    # Increase the chance of going to restaurants blacklisted by people who are not coming
    restaurants += [restaurant for key in TEAM_BLACKLIST.keys() for restaurant in TEAM_BLACKLIST[key] if key in NOT_COMING]

    # Remove the last restaurant we went to
    restaurants = [restaurant for restaurant in restaurants if restaurant != LAST_RESTAURANT]

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
# 04/05/2019  Eric Schrock  Initial version
# 06/13/2019  Eric Schrock  Added blacklists
###############################################################################
