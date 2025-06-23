def calculate_net_salary(salary, overtime_hours, overtime_rate, bonus, tax_rate):
    """
    คำนวณเงินเดือนสุทธิของพนักงาน
    
    Args:
        salary (float): เงินเดือนฐาน
        overtime_hours (int): ชั่วโมงทำงานล่วงเวลา
        overtime_rate (float): อัตราค่าล่วงเวลาต่อชั่วโมง
        bonus (float): โบนัส
        tax_rate (float): อัตราภาษี (เป็นทศนิยม เช่น 0.05 = 5%)
    
    Returns:
        tuple: (เงินเดือนก่อนหักภาษี, ภาษี, เงินเดือนสุทธิ)
    """
    gross_pay = salary + (overtime_hours * overtime_rate) + bonus
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    
    return gross_pay, tax, net_pay

# การใช้งาน - สะอาดและอ่านง่าย
employee_1 = calculate_net_salary(25000, 10, 200, 5000, 0.05)
employee_2 = calculate_net_salary(30000, 5, 250, 3000, 0.07)

print(f"พนักงานคนที่ 1 - เงินเดือนสุทธิ: {employee_1[2]:,.2f} บาท")
print(f"พนักงานคนที่ 2 - เงินเดือนสุทธิ: {employee_2[2]:,.2f} บาท")