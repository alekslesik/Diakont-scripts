import re
import os

from Cell import Cell
from FaPassport import FaPassport
from Utils import Utils

main_path = 'd:\BUILDS\СУМП_Руппур\Work\SUMP\DB\FHMControlMode\\'
service_area_path = main_path + 'Ini\ServiceArea.ini'
reloaded_items_map_path = main_path + 'Ini\ReloadedItemsMap.ini'
passports_path = main_path + 'ReloadedItems\\'
# main_directory = input("Введи путь")

# Cells count
cells_count = 1
# Dictionary includes all Cell and FaPassport objects
reactor_cells = dict()
all_passports = dict()

# Get file encoding
service_area_enc = Utils.define_ini_encoding(service_area_path)
passport_enc = Utils.define_ini_encoding(passports_path + os.listdir(passports_path)[0])
reloaded_items_map_enc = Utils.define_ini_encoding(reloaded_items_map_path)

# Parse ServiceArea.ini file to configServiceArea variable
config_service_area = Utils.get_config_parser(service_area_path, service_area_enc)

# Parse ReloadedItemMap.ini file to configReloadItemsMap variable
config_reload_items_map = Utils.get_config_parser(reloaded_items_map_path, reloaded_items_map_enc)

# Fill object Cell
# Fill reactorCells dictionary
# Fill allPassports dictionary
for cell_name in config_service_area.sections():
    pattern = 'N_[01]\d{3}$'
    if re.match(pattern, cell_name):
        cell = Cell()
        cell.set_name(cell_name)
        cell.set_xc(config_service_area[cell_name]['XC'])
        cell.set_yc(config_service_area[cell_name]['YC'])
        reactor_cells[cells_count] = cell
        passport = FaPassport()
        passport.set_encoding(passport_enc)
        passport.set_name('UkuTest' + str(cells_count) + '.txt')
        passport.set_num(passport.get_name()[:-4])
        passport.set_path(passports_path + passport.get_name())
        passport.set_x(cell.get_xc())
        passport.set_y(cell.get_yc())
        passport.create_passport_file()
        all_passports[cells_count] = passport
        config_reload_items_map.set(cell_name, "Number_R_I", "1")
        config_reload_items_map.set(cell_name, "Name_R_I1", passport.get_num())
        cells_count += 1

    Utils.write_ini_file(config_reload_items_map, reloaded_items_map_path, reloaded_items_map_enc)
