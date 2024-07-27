
print("                 __..-----")
print("       ,.--._ .-'_..--...-'")
print("      '-\"'. _/_ /  ..--''\"\"'-.")
print("      _.--\"\"...:._:(_ ..:\"::. \\")
print("   .-' ..::--\"_(##)#)\"':. \\ \\)    \\ _|_ /")
print("  /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'")
print("  \"  / |  :' :/\"\"\\///)  /:.'    --(       )--")
print("    / :( :( :(   (#//)  \"       .-'\\.___./'-.")
print("   / :/|\\ :\\_:   \\#//\\            /  |  \\")
print("   |:/ | \"\"--':\\   (#//)              '")
print("   \\/  \\ :|  \\ :\\  (#//)")
print("        \\:\\   '.':. \\#//\\")
print("         ':|    \"--'(#///)")
print("                    (#///)")
print("                    (#///)")
print("                     \\#///\\")
print("                     (##///)")
print("                     (##///)")
print("                     (##///)")
print("                     (##///)")
print("                      \\##///\\")
print("                      (###///)")
print("                      (sjw////)__...-----....__")
print("                      (#/::'''                 \"\"--.._")
print("                 __..-'''                             \"-._")
print("         __..--\"\"                                         '._")
print("___..--\"\"                                                    \"-..____")
print("  (_ \"\"---....___                                     __...--\"\" _)")
print("    \"\"\"--...  ___\"\"\"\"\"-----......._______......----\"\"\"     --\"")
print("                  \"\"\"\"       ---.....   ___....----\"")

print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()

if direction == "right":
    print("You fell into a hole. Game Over.")
    exit()
elif direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
  
else:
    print("Invalid input. Game Over.")
    exit()
    
print("Type 'wait' to wait for a boat. Type 'swim' to swim across.")
action = input().lower()

if action == "swim":
    print("You were attacked by a trout. Game Over.")
    exit()
elif action == "wait":
    print("You arrived at the island unharmed.")
else:
    print("Invalid input. Game Over.")
    exit()
    
print("There is a house with 3 doors. One red, one yellow, and one blue.")  
print("Which color do you choose?")
color = input().lower()

if color == "red":
    print("You were burned by fire. Game Over.")
    exit()
elif color == "yellow":
    print("You found the treasure! You win!")
elif color == "blue":
    print("You were eaten by beasts. Game Over.")
    exit()
else:
    print("Invalid input. Game Over.")
    exit()
    
    

