class parking_spot:
    
    def __init__(self, name, city, district, ptype, longitude, latitude): # parking_spot의 생성자
        self.__item = {'name':name, 'city':city, 'district':district, 'ptype':ptype, 'longitude':str(longitude), 'latitude':str(latitude)}

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword = 'name'):
        """
        Args:
            keyword(string) : 반환할 문자열 keyword 기본인수는 'name'.
        Returns:
            key : 반환할 문자열
        """
        key = self.__item[keyword]
        return key

def str_list_to_class_list(str_list):
    """
    Args:
        str_list : 객체 리스트로 변환할 문자열 리스트
    Returns:
        class_list : parking_spot 클래스 객체의 리스트
    """
    class_list = []
    for item in str_list: # 반복문으로 변환 진행
        temp = item.split(',') # split함수 이용해서 구분
        name = temp[1]
        city = temp[2]
        district = temp[3]
        ptype = temp[4]
        longitude = temp[5]
        latitude = temp[6]
        parking = parking_spot(name, city, district, ptype, longitude, latitude)
        class_list.append(parking) #클래스 객체 리스트 생성
    return class_list

def print_spots(spots):
    """
     Args:
        spots : 클래스 객체의 리스트[spots]
    """
    print("---print elements({})---".format(len(spots))) # 리스트 길이 출력
    for item in spots:
        print("[{}({})] {} {}(lat:{}, long:{})".format(item.get('name'), item.get('ptype'), item.get('city'), item.get('district'), item.get('latitude'), item.get('longitude'))) # 출력형식에 맞추어 출력

def filter_by_name(spots, name):
    """
    Args:
        spots : 클래스 객체의 리스트[spots]
        name : 필터 요소
    Returns:
        함축 리스트를 이용한 필터 적용된 리스트
    """
    return [aname for aname in spots if name in aname.get('name')]

def filter_by_city(spots, city):
    """
    Args:
        spots : 클래스 객체의 리스트[spots]
        city : 필터 요소
    Returns:
        함축 리스트를 이용한 필터 적용된 리스트
    """
    return [acity for acity in spots if city in acity.get('city')]

def filter_by_district(spots, district):
    """
    Args:
        spots : 클래스 객체의 리스트[spots]
        district : 필터 요소
    Returns:
        함축 리스트를 이용한 필터 적용된 리스트
    """
    return [adistrict for adistrict in spots if district in adistrict.get('district')]

def filter_by_ptype(spots, ptype):
    """
    Args:
        spots : 클래스 객체의 리스트[spots]
        ptype : 필터 요소
    Returns:
        함축 리스트를 이용한 필터 적용된 리스트
    """
    return [aptype for aptype in spots if ptype in aptype.get('ptype')]

def filter_by_location(spots, locations):
    """
    Args:
        spots : 클래스 객체의 리스트[spots]
        locations : 필터 적용 시킬 튜플
    Returns:
        함축 리스트를 이용한 필터 적용된 리스트
    """
    min_lat = locations[0]
    max_lat = locations[1]
    min_long = locations[2]
    max_long = locations[3]
    return [alocations for alocations in spots if min_lat<float(alocations.get('latitude'))<max_lat and min_long<float(alocations.get('longitude'))<max_long]

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)