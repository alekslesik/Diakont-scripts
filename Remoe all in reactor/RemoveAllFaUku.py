from Utils import Utils
import re


main_path = 'd:\BUILDS\СУМП_Руппур\Work\SUMP\DB\FHMControlMode\\'
reloaded_items_map_path = main_path + 'Ini\ReloadedItemsMap.ini'
passports_path = main_path + 'ReloadedItems\\'

for passport in Utils.listdir(passports_path):
    if re.match('UkuTest*', passport):
        path = Utils.path_join(passports_path, passport)
        Utils.remove_path(path)

config_reload_items_map = Utils.get_config_parser(reloaded_items_map_path)

for cell_name in config_reload_items_map.sections():
    pattern = 'N_[01]\d{3}$'
    if re.match(pattern, cell_name):
        config_reload_items_map.set(cell_name, "Number_R_I", "0")
        config_reload_items_map.remove_option(cell_name, "Name_R_I1")

    Utils.write_ini_file(config_reload_items_map, reloaded_items_map_path)
