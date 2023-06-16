import file_manager
import parking_spot_manager
def start_process(path):
    str_list = file_manager.read_file(path)
    space_list = parking_spot_manager.Myparking.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.Myparking.print_spots(space_list)
            
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                parking_fliter_list = parking_spot_manager.Myparking.filter_by_name(space_list, keyword)
                parking_spot_manager.Myparking.print_spots(parking_fliter_list)
                
            elif select == 2:
                keyword = input('type city:')
                parking_fliter_list = parking_spot_manager.Myparking.filter_by_city(space_list, keyword)
                parking_spot_manager.Myparking.print_spots(parking_fliter_list)
                
            elif select == 3:
                keyword = input('type district:')
                parking_fliter_list = parking_spot_manager.Myparking.filter_by_district(space_list, keyword)
                parking_spot_manager.Myparking.print_spots(parking_fliter_list)
                
            elif select == 4:
                keyword = input('type ptype:')
                parking_fliter_list = parking_spot_manager.Myparking.filter_by_ptype(space_list, keyword)
                parking_spot_manager.Myparking.print_spots(parking_fliter_list)
                
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                parking_fliter_list = parking_spot_manager.Myparking.filter_by_location(space_list, min_lat, max_lat, min_lon, max_lon)
                parking_spot_manager.Myparking.print_spots(parking_fliter_list)
                
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                parking_space_list = parking_spot_manager.Myparking.sort_by_keyword(space_list, keyword)
                parking_spot_manager.Myparking.print_spots(parking_space_list)
                space_list = parking_space_list
                
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
           
        else:
            print("invalid input")