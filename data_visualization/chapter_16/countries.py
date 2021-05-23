from pygal_maps_world.i18n import COUNTRIES
# COUNTRIES是一个字典

# 打印两个字母的国别码和对应的国家名称
for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])