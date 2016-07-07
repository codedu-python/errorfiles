my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 188 # cm
my_weight = 82 # kg
my_eyes = '파랑'
my_teeth = '하양'
my_hair = '갈색'

print("{}에 대해 이야기해 보죠."format(my_name)
print("키는 {} 센티미터고요."format(my_height))
print("몸무게는 {} 킬로그램이에요."format(my_weight))
print("사실 아주 많이 나가는 건 아니죠.")
print("눈은 {eye}이고 머리는 {hair}이에요."format(hair=my_hair, eye=my_eyes))
print("이는 보통 {}이고 커피를 먹으면 달라져요."format(my_teeth))

# 이 줄은 까다롭지만 정확히 따라 하세요
print("{1}, {0}, {2}를 모두 더하면 {3} 랍니다.".format(
my_height, my_age, my_weight, my_age + my_height + my_weight ))
