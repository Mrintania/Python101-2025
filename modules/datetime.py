from datetime import datetime, date, timedelta
import calendar

# วันที่และเวลาปัจจุบัน
now = datetime.now()
today = date.today()

print(f"วันที่และเวลาตอนนี้: {now}")
print(f"วันที่วันนี้: {today}")
print(f"ปีปัจจุบัน: {today.year}")
print(f"เดือนปัจจุบัน: {today.month}")
print(f"วันปัจจุบัน: {today.day}")

# การจัดรูปแบบวันที่
formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
thai_format = now.strftime("%A, %d %B %Y")

print(f"รูปแบบไทย: {formatted_date}")
print(f"รูปแบบอังกฤษ: {thai_format}")

# การคำนวณวันที่
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
last_month = today - timedelta(days=30)

print(f"พรุ่งนี้: {tomorrow}")
print(f"อาทิตย์หน้า: {next_week}")
print(f"เดือนที่แล้ว: {last_month}")

# การคำนวณอายุ
def calculate_age(birth_date):
    """คำนวณอายุจากวันเกิด"""
    today = date.today()
    age = today.year - birth_date.year
    
    # ตรวจสอบว่าครบวันเกิดแล้วหรือยัง
    if today.month < birth_date.month or \
       (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    return age

# ทดสอบการคำนวณอายุ
birthday = date(1995, 5, 15)
age = calculate_age(birthday)
print(f"เกิดวันที่ {birthday} อายุ {age} ปี")

# การทำงานกับปฏิทิน
print(f"\nปฏิทินเดือนนี้:")
print(calendar.month(today.year, today.month))