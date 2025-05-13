from character import Character
from weapon import Weapon
from room import Room


#weapons
gun = Weapon("gun", 30)
teeth = Weapon("teeth", 1)
kickflips = Weapon("absolutely sick kickflips", 6)
punches = Weapon("rapid punches and kicks", 7)

#characters
player = Character("you", 20, gun, 0)
rats = Character("a pile of 111 rats", 111, teeth, 1)
potted_plant = Character("a singular potted plant", 90, kickflips, 2)
fishies = Character("a fish without legs or arms", 70, punches, 2)

#room
nest = Room("rat's nest", player, rats, None, 'You find yourself in a rat nest. There seems to be 111 rats chanting "rats rats we are the rats" in front of you. They spot you and lunge at you.')
shop = Room("shop", player, None, "shop", "yer at ye olde shoppe")
garden = Room("garden", player, potted_plant, None, "it's a beautiful garden with plants, including regular old plants that can do normal potted plant things")
aquarium = Room("aquarium", player, fishies, None, "all around you you see fishes and other sealife as you now are in an aquarium")

nest.con_room = [shop]
shop.con_room = [garden, aquarium, nest]
garden.con_room = [shop]

# print("")
# print('()(),~~,.')
# print(' .. ___; )')
# print('=`=     (_.')
# print("")

nest.enter()

