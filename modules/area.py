"""
Module สำหรับคำนวณทางคณิตศาสตร์
"""

import math# Constants
PI = 3.14159265359

def calculate_circle_area(radius):
    """คำนวณพื้นที่วงกลม"""
    return PI * radius ** 2

print(f"พื้นที่วงกลมรัศมี 1: {calculate_circle_area(1):.2f}")