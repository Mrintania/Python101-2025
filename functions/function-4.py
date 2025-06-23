###Functions ที่รับพารามิเตอร์:
def greet_person(name):
    """ทักทายโดยใช้ชื่อ"""
    print(f"สวัสดี คุณ{name}!")

def calculate_circle_area(radius):
    """คำนวณพื้นที่วงกลม"""
    import math
    area = math.pi * radius ** 2
    return area

def add_numbers(a, b):
    """บวกเลขสองตัว"""
    result = a + b
    return result

# การใช้งาน
greet_person("สมชาย")
area = calculate_circle_area(5)
sum_result = add_numbers(10, 20)

print(f"พื้นที่วงกลมรัศมี 5: {area:.2f}")
print(f"10 + 20 = {sum_result}")