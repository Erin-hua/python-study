cats = {'mi': 'wang', 'cici': 'kun'}
dogs = {'cathey': 'hu', 'eric': 'hua'}
pets = [cats, dogs]
for pet_owner in pets:
    for pet_name, owner_name in pet_owner.items():
        print(pet_name.title() + ' belongs to ' + owner_name.title() + '.')
