# โค้ดที่ซ้ำซาก - การคำนวณเงินเดือนพนักงาน
# พนักงานคนที่ 1
salary_1 = 25000
overtime_hours_1 = 10
overtime_rate_1 = 200
bonus_1 = 5000
tax_rate_1 = 0.05

gross_pay_1 = salary_1 + (overtime_hours_1 * overtime_rate_1) + bonus_1
tax_1 = gross_pay_1 * tax_rate_1
net_pay_1 = gross_pay_1 - tax_1

print(f"พนักงานคนที่ 1 - เงินเดือนสุทธิ: {net_pay_1:,.2f} บาท")

# พนักงานคนที่ 2
salary_2 = 30000
overtime_hours_2 = 5
overtime_rate_2 = 250
bonus_2 = 3000
tax_rate_2 = 0.07

gross_pay_2 = salary_2 + (overtime_hours_2 * overtime_rate_2) + bonus_2
tax_2 = gross_pay_2 * tax_rate_2
net_pay_2 = gross_pay_2 - tax_2

print(f"พนักงานคนที่ 2 - เงินเดือนสุทธิ: {net_pay_2:,.2f} บาท")