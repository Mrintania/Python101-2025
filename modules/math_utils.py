"""
Module สำหรับคำนวณทางคณิตศาสตร์
"""

import math

# Constants
PI = 3.14159265359

def calculate_circle_area(radius):
    """คำนวณพื้นที่วงกลม"""
    return PI * radius ** 2

def calculate_circle_perimeter(radius):
    """คำนวณเส้นรอบวงวงกลม"""
    return 2 * PI * radius

def calculate_rectangle_area(length, width):
    """คำนวณพื้นที่สี่เหลี่ยม"""
    return length * width

def calculate_triangle_area(base, height):
    """คำนวณพื้นที่สามเหลี่ยม"""
    return 0.5 * base * height

def is_prime(n):
    """ตรวจสอบว่าเป็นจำนวนเฉพาะหรือไม่"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """คำนวณแฟกทอเรียล"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# ตัวแปรที่ใช้ร่วมกัน
calculations_count = 0

def increment_counter():
    """เพิ่มจำนวนการคำนวณ"""
    global calculations_count
    calculations_count += 1

if __name__ == "__main__":
    # โค้ดที่จะรันเฉพาะตอนไฟล์นี้ถูกเรียกโดยตรง
    print("ทดสอบ math_utils module")
    print(f"พื้นที่วงกลมรัศมี 5: {calculate_circle_area(5)}")
    print(f"7 เป็นจำนวนเฉพาะ: {is_prime(7)}")