### Functions แบบง่าย - ไม่รับพารามิเตอร์:
def greet():
    """ทักทายแบบง่าย"""
    print("สวัสดีครับ!")
    print("ยินดีที่ได้รู้จัก")

def get_current_time():
    """ดึงเวลาปัจจุบัน"""
    from datetime import datetime
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# การใช้งาน
greet()  # ไม่ return อะไร
current_time = get_current_time()  # return string
print(f"เวลาตอนนี้: {current_time}")