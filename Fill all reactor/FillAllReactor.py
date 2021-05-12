import re

from Cell import Cell
from FaPassport import FaPassport
from ReloadeItemsMap import ReloadedItemsMap
from ServiceArea import ServiceArea

main_path = 'd:\BUILDS\СУМП_Руппур\Work\SUMP\DB\FHMControlMode\\'
# main_directory = input("Введи путь")

# Cells count
cells_count = 1

service_area = ServiceArea(main_path)
reloaded_items_map = ReloadedItemsMap(main_path)

# Fill object Cell
for cell_name in service_area.ini_config.sections():
    pattern = 'N_[01]\d{3}$'
    if re.match(pattern, cell_name):
        cell = Cell()
        cell.name = cell_name
        cell.xc = service_area.get_setting(cell_name, 'XC')
        cell.yc = service_area.get_setting(cell_name, 'YC')
        passport = FaPassport(main_path)
        passport.name = 'UkuTest' + str(cells_count) + '.txt'
        passport.num = passport.name[:-4]
        passport.path = passport.passports_path + passport.name
        passport.x = cell.xc
        passport.y = cell.yc
        passport.create_passport_file()
        reloaded_items_map.update_setting(cell_name, "Number_R_I", "1")
        reloaded_items_map.update_setting(cell_name, "Name_R_I1", passport.num)
        cells_count += 1

