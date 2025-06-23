# คำสั่ง pip พื้นฐาน (รันใน command line)
'''
# ดูเวอร์ชัน pip
pip --version

# ติดตั้ง package
pip install requests
pip install pandas
pip install matplotlib

# ติดตั้งเวอร์ชันเฉพาะ
pip install numpy==1.21.0

# อัปเกรด package
pip upgrade requests

# ดู packages ที่ติดตั้งแล้ว
pip list

# ดูข้อมูลของ package
pip show pandas

# ถอนการติดตั้ง
pip uninstall matplotlib

# บันทึกรายการ packages
pip freeze > requirements.txt

# ติดตั้งจาก requirements.txt
pip install -r requirements.txt

'''