# Program to arrange Challonge participants into proper order
# This one handles the odd contestants
odd = open("odd.txt", "w")

# Reads in total entrants and selects the odd out
with open('entrants.csv', 'r') as entrants:
    # Counter for skipping
    counter = 0
    for line in entrants:
        split = line.split(',')
        counter = counter + 1
        if counter % 2 == 0:
            print split[1]
            odd.write(split[1] + "\n")
