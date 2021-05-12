def make_car(owner, typ, **car_info):
    car = {}
    car['owner'] = owner
    car['typ'] = typ
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
