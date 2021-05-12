favorite_places = {
    'wang': ['beijing', 'changsha', 'shenzhen'],
    'hu': ['yunlan', 'xian'],
    'jiang': ['qinghai'],
    }
for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are: ")
    if len(places) > 1:
        for place in places:
            print("\t" + place.title())
    else:
        print("\t" + places[0].title())
