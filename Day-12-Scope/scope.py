# # Scope #

# enemies = 1

# def scope():
#     enemies = 2
#     print(f"There ARE {enemies} enemies.")

# scope()
# print(f"There IS {enemies} enemies.")


# # Local Scope

# def drink_potion():
#     potion_health = 2
#     print(potion_health)

# drink_potion()
# #print(potion_health) # This give us an error


# # Global Scope
# player_health = 10

# def game():
#       def drink_potion():
#           poton_health = 2
#           print(player_health)
      
#       drink_potion()

# game()


# Modyfing Global Values

# enemies = 1

# def scope():
#     global enemies
#     enemies += 1
#     print(f"There ARE {enemies} enemies.")

# scope()
# print(f"There IS {enemies} enemies.")



# Global Constans

PI = 3.14
TWITTER_NAME = "@Matthew_1401"
# Declaring constant values use a uppercase