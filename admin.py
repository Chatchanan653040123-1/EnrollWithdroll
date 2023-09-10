import json
from common import *
class Admin:

    def addSubject():
        while True:
            if input("คุณต้องการลงทะเบียนเรียนใช่หรือไม่ (y/n): ") == "n":
                return
            print("ลงทะเบียนเรียน\nกรุณากรอกตามแบบฟอร์มนี้")
            id = input("รหัสวิชา: ")
            subject = input("วิชา: ")
            section = input("เซคชั่น: ")
            teacher = input("อาจารย์ผู้สอน: ")
            try:
                with open(subjectPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    print(f"รหัสวิชา {id} มีอยู่ในระบบแล้ว")
                    return
                newData = {id: {"teacher":teacher,"subject":subject,"section": section}}
                data.update(newData)
                with open(subjectPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"เพิ่ม {subject} สำเร็จแล้ว")
            except Exception as e:
                print(e)

    def editSubject():
            if input("คุณต้องการแก้ไขวิชาใช่หรือไม่ (y/n): ") == "n":
                return
            print("แก้ไขวิชา\nกรุณากรอกข้อมูลใหม่")
            id = input("ระบุชื่อรหัสวิชาที่ต้องการแก้ไข: ")
            try:
                with open(subjectPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    new_subject_name = input("ระบุชื่อวิชาใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                    new_section = input("ระบุเวลาเรียนใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                    new_teacher = input("ระบุอาจารย์ผู้สอนใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                    if new_subject_name:
                        data[id]["subject"] = new_subject_name
                    if new_section:
                        data[id]["section"] = new_section
                    if new_teacher:
                        data[id]["teacher"] = new_teacher
                    with open(subjectPath, "w") as file:
                        json.dump(data, file, indent=4)
                    print(f"แก้ไข {id} สำเร็จแล้ว")
                else:
                    print(f"ไม่พบรหัสวิชา {id} ในระบบ")
            except Exception as e:
                print(e)


    def deleteSubject():
        while True:
            if input("คุณต้องการลบวิชาใช่หรือไม่ (y/n): ") == "n":
                return
            print("ลบวิชา\nกรุณากรอกชื่อวิชาที่ต้องการลบ")
            id = input("ระบุรหัสวิชาที่ต้องการลบ: ")
            try:
                with open(subjectPath, "r") as file:
                    data = json.load(file)
                if id in data:
                    del data[id]
                    with open(subjectPath, "w") as file:
                        json.dump(data, file, indent=4)
                    print(f"ลบ {id} สำเร็จแล้ว")
                else:
                    print(f"ไม่พบรหัสวิชา {id} ในระบบ")
            except Exception as e:
                print(e)

    def getSubject():
        try:
            with open(subjectPath, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(e)

    def getStudent():
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            return data
        except Exception as e:
            print(e)

    def logout():
        common(False,setLogin)
        print("ออกจากระบบสำเร็จ")

    def admin():
        if (not getLogin() and not getAdmin()):
            print("คุณยังไม่ได้ล็อคอินหรือไม่ใช่แอดมิน")
            return
        print("\n\n\nยินดีต้อนรับ นี่คือเมนูแอดมิน\n")
        while True:
            select = int(input("โปรดเลือก\n1.เพิ่มวิชา\n2.แก้ไขวิชา\n3.ลบวิชา\n4.ดูรายวิชาที่เปิดสอน\n5.ดูรายชื่อนักเรียนทั้งหมด\n6.Log out\nYour input:"))
            if select == 1:
                Admin.addSubject()
            elif select == 2:
                Admin.editSubject()
            elif select == 3:
                Admin.deleteSubject()
            elif select == 4:
                print(Admin.getSubject())
            elif select == 5:
                print(Admin.getStudent())
            elif select == 6:
                Admin.logout()
                break
            else:
                print("กรุณาเลือกใหม่อีกครั้ง")
