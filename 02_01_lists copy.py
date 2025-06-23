# เริ่มต้นด้วย list ว่าง
todo_list = []

# เพิ่มรายการทีละตัวท้าย list
todo_list.append("ซื้อของ","ทำการบ้าน")
todo_list.append("ทำการบ้าน")
todo_list.append("ออกกำลังกาย")
print(f"สิ่งที่ต้องทำ: {todo_list}")

# เพิ่มหลายรายการพร้อมกัน
# more_tasks = ["อ่านหนังสือ", "โทรหาแม่"]
# todo_list.extend(more_tasks)
# print(f"เพิ่มเติมแล้ว: {todo_list}")

# # แทรกรายการในตำแหน่งเฉพาะ
# todo_list.insert(0, "ตื่นเช้า")  # แทรกที่ตำแหน่งแรก
# todo_list.insert(2, "แปรงฟัน")   # แทรกที่ตำแหน่งที่ 2
# print(f"แทรกเพิ่มแล้ว: {todo_list}")