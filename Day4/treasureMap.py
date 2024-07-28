line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot!")

position = input("Where do you want to put the treasure? ")

letter = position[0].lower()
number = position[1]

letterIndex = ["a", "b", "c"].index(letter)
intIndex = int(number) - 1

map[intIndex][letterIndex] = "X"

print(f"{line1}\n{line2}\n{line3}")