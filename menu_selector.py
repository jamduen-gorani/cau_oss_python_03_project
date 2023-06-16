# 필요 모듈 import
import file_manager
import parking_spot_manager

def start_process(path):
    list = file_manager.read_file(path) # 리스트 불러오기
    spots = parking_spot_manager.str_list_to_class_list(list) # 클래스 객체 리스트로 변환
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots) # 출력형식에 맞추어 출력
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
                spots = parking_spot_manager.filter_by_name(spots, keyword) # 함수 호출해 필터 적용
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword) # 함수 호출해 필터 적용
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword) # 함수 호출해 필터 적용
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword) # 함수 호출해 필터 적용
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                location = (min_lat, max_lat, min_lon, max_lon) # 튜플 생성
                spots = parking_spot_manager.filter_by_location(spots, location) # 함수 호출해 필터 적용
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                spots = parking_spot_manager.sort_by_keyword(spots, keyword) # 정렬된 리스트 저장
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break # 반복문 탈출
        else:
            print("invalid input")