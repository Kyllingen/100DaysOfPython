line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot!")

position = input("Where do you want to put the treasure? (a,b,c and 1,2,3) ")

letter = position[0].lower()
number = position[1]

letter_index = ["a", "b", "c"].index(letter)
int_index = int(number) - 1

map[int_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")