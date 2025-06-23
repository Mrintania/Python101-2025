import random

# การสุ่มตัวเลข
print("การสุ่มตัวเลข:")
print(f"เลขสุ่ม 0-1: {random.random()}")
print(f"เลขสุ่ม 1-10: {random.randint(1, 10)}")
print(f"เลขสุ่ม 1-100 (ทศนิยม): {random.uniform(1, 100):.2f}")

# การสุ่มจาก list
colors = ["แดง", "เขียว", "น้ำเงิน", "เหลือง", "ม่วง"]
print(f"\nสีสุ่ม: {random.choice(colors)}")

# การสุ่มหลายรายการ
random_colors = random.choices(colors, k=3)  # สุ่ม 3 รายการ (อาจซ้ำ)
print(f"สีสุ่ม 3 สี: {random_colors}")

# การสุ่มไม่ซ้ำ
unique_colors = random.sample(colors, 3)  # สุ่ม 3 รายการ (ไม่ซ้ำ)
print(f"สีสุ่มไม่ซ้ำ: {unique_colors}")

# การสับลำดับ
numbers = list(range(1, 11))
print(f"\nตัวเลขเดิม: {numbers}")
random.shuffle(numbers)
print(f"สับลำดับแล้ว: {numbers}")

# เกมทายตัวเลขแบบง่าย
def guess_number_game():
    """เกมทายตัวเลข"""
    secret = random.randint(1, 10)
    attempts = 3
    
    print("\n--- เกมทายตัวเลข ---")
    print("ฉันคิดตัวเลข 1-10")
    
    for attempt in range(attempts):
        try:
            guess = int(input(f"ครั้งที่ {attempt + 1}: "))
            if guess == secret:
                print("ถูกต้อง! คุณชนะ! 🎉")
                return
            elif guess < secret:
                print("น้อยเกินไป")
            else:
                print("มากเกินไป")
        except ValueError:
            print("กรุณาใส่ตัวเลข")
            
    print(f"หมดโอกาส! ตัวเลขคือ {secret}")

# เรียกเล่นเกม (สามารถ uncomment ได้)
# guess_number_game()