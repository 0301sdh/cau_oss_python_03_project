class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method

    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {
            'name' : name,
            'city' : city,
            'district' : district,
            'ptype' : ptype,
            'longitude' : float(longitude),
            'latitude' : float(latitude)

        }
    
    def get(self, keyword = 'name'):
        return self.__item[keyword]  

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def str_list_to_class_list(self, str_list):
        class_list = []
        for item in str_list:
            data = item.rstrip().split(',')
            name = data[1]
            city = data[2]
            district = data[3]
            ptype = data[4]
            longitude = float(data[5])
            latitude = float(data[6])
            space = parking_spot(name, city, district, ptype, longitude, latitude)
            class_list.append(space)
        return class_list
    
    def print_spots(self, spots):
        print(f"---print elements({len(spots)})---")
        for space in spots:
            print(space)

    def filter_by_name(self, spots, name):
        return [space for space in spots if name.lower() in space.get('name').lower()]

    def filter_by_city(self, spots, city):
        return [space for space in spots if city.lower() in space.get('city').lower()]

    def filter_by_district(self, spots, district):
        return [space for space in spots if district.lower() in space.get('district').lower()]

    def filter_by_ptype(self, spots, ptype):
        return [space for space in spots if ptype.lower() in space.get('ptype').lower()]
    
    def filter_by_location(self, spots, min_lat, max_lat, min_long, max_long):
        return [
            space for space in spots
            if min_lat <= space.get('latitude') <= max_lat
            and min_long <= space.get('longitude') <= max_long
        ]
    
    def sort_by_keyword(self, spots, keyword):
        return sorted(spots, key=lambda space: space.get(keyword))
    
Myparking  = parking_spot("Name", "City", "District", "Ptype", 30.534, 130.23)
 

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = Myparking.str_list_to_class_list(str_list)
    Myparking.print_spots(spots)

    # version#3
    spots = Myparking.filter_by_district(spots, '동작')
    Myparking.print_spots(spots)
    
    # version#4
    spots = Myparking.sort_by_keyword(spots, 'name')
    Myparking.print_spots(spots)