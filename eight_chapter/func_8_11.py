def make_great(magicians,changes):
    while magicians:
        change = "The Great " + magicians.pop()
        changes.append(change)

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ["wang", "hu", "zhao"]
changes = []

make_great(magicians[:], changes)
show_magicians(magicians)
print('\n')
show_magicians(changes)
