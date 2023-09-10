import json
from common import subjectPath,userPath,getLogin,getUserName
from user import User
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
                    print(f"รหัสวิชา {id} มีอยู่ในระบบแล้ว\n\n")
                    return
                newData = {id: {"teacher":teacher,"subject":subject,"section": section}}
                data.update(newData)
                with open(subjectPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"เพิ่ม {subject} สำเร็จแล้ว\n\n")
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
                    print(f"แก้ไข {id} สำเร็จแล้ว\n\n")
                else:
                    print(f"ไม่พบรหัสวิชา {id} ในระบบ\n\n")
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
                    print(f"ลบ {id} สำเร็จแล้ว\n\n")
                else:
                    print(f"ไม่พบรหัสวิชา {id} ในระบบ\n\n")
            except Exception as e:
                print(e)

    def getSubject():
        try:
            with open(subjectPath, "r") as file:
                data = json.load(file)
            print("--------------------วิชาที่เปิดสอน--------------------")
            for i in data:
                print(f"รหัสวิชา:{i} วิชา:{data[i]['subject']} เวลาเรียน:{data[i]['section']} ชื่ออาจารย์:{data[i]['teacher']}")
            print("--------------------------------------------------------\n")
        except Exception as e:
            print(e)
            
    def getStudent():
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            print("--------------------นักเรียนทั้งหมด--------------------")
            for i in data:
                print(f"ชื่อยูสเซอร์:{i} ชื่อ:{data[i]['fname']} นามสกุล:{data[i]['lname']} ชื่อเล่น:{data[i]['nickname']} อีเมล:{data[i]['email']} เบอร์โทรศัพท์:{data[i]['phoneNumber']} รหัสผ่าน:{data[i]['password']} เป็นแอดมิน:{data[i]['isAdmin']}")
            print("--------------------------------------------------------\n")
        except Exception as e:
            print(e)
    def editStudent():
        if input("คุณต้องการแก้ไขข้อมูลนักเรียนใช่หรือไม่ (y/n): ") == "n":
            return
        print("แก้ไขข้อมูลนักเรียน\nกรุณากรอกข้อมูลใหม่")
        id = input("ระบุชื่อผู้ใช้ที่ต้องการแก้ไข: ")
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if id in data:
                new_fname = input("ระบุชื่อใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                new_lname = input("ระบุนามสกุลใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                new_nickname = input("ระบุชื่อเล่นใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                new_email = input("ระบุอีเมลใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                new_phoneNumber = input("ระบุเบอร์โทรศัพท์ใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                new_password = input("ระบุรหัสผ่านใหม่ (หากไม่ต้องการแก้ไขให้กด Enter): ")
                if new_fname:
                    data[id]["fname"] = new_fname
                if new_lname:
                    data[id]["lname"] = new_lname
                if new_nickname:
                    data[id]["nickname"] = new_nickname
                if new_email:
                    data[id]["email"] = new_email
                if new_phoneNumber:
                    data[id]["phoneNumber"] = new_phoneNumber
                if new_password:
                    data[id]["password"] = new_password
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"แก้ไข {id} สำเร็จแล้ว\n\n")
            else:
                print(f"ไม่พบชื่อผู้ใช้ {id} ในระบบ\n\n")
        except Exception as e:
            print(e)
    def deleteStudent():
        if input("คุณต้องการลบข้อมูลนักเรียนใช่หรือไม่ (y/n): ") == "n":
            return
        print("ลบข้อมูลนักเรียน\nกรุณากรอกชื่อผู้ใช้ที่ต้องการลบ")
        id = input("ระบุชื่อผู้ใช้ที่ต้องการลบ: ")
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if id in data:
                del data[id]
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"ลบ {id} สำเร็จแล้ว\n\n")
            else:
                print(f"ไม่พบชื่อผู้ใช้ {id} ในระบบ\n\n")
        except Exception as e:
            print(e)
    def addStudent():
        while True:
            if input("คุณต้องการเพิ่มข้อมูลนักเรียนใช่หรือไม่ (y/n): ") == "n":
                return
            print("เพิ่มข้อมูลนักเรียน\nกรุณากรอกตามแบบฟอร์มนี้")
            fname = input("ชื่อ : ")
            lname = input("นามสกุล : ")
            nickname = input("ชื่อเล่น : ")
            email = input("อีเมล : ")
            phoneNumber = input("เบอร์โทรศัพท์ : ")
            userName = input("ชื่อผู้ใช้ : ")
            password = input("รหัสผ่าน : ")
            try:
                with open(userPath, "r") as file:
                    data = json.load(file)  
                newData = {userName:{"fname":fname,"lname":lname,"nickname":nickname,"email":email,"phoneNumber":phoneNumber,"password":password,"isAdmin":False,"subject":[]}}
                if userName in data:
                    print("มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว\n\n")
                    return
                data.update(newData) 
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print("เพิ่มข้อมูลนักเรียนสำเร็จ\n\n")
            except Exception as e:
                print(e)
    def setAdmin():
        if input("คุณต้องการเพิ่มสิทธิ์แอดมินใช่หรือไม่ (y/n): ") == "n":
            return
        print("เพิ่มสิทธิ์แอดมิน\nกรุณากรอกชื่อผู้ใช้ที่ต้องการเพิ่มสิทธิ์")
        id = input("ระบุชื่อผู้ใช้ที่ต้องการเพิ่มสิทธิ์: ")
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if id in data:
                data[id]["isAdmin"] = True
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"เพิ่มสิทธิ์แอดมิน {id} สำเร็จแล้ว\n\n")
            else:
                print(f"ไม่พบชื่อผู้ใช้ {id} ในระบบ\n\n")
        except Exception as e:
            print(e)
    def removeAdmin():
        if input("คุณต้องการลบสิทธิ์แอดมินใช่หรือไม่ (y/n): ") == "n":
            return
        print("ลบสิทธิ์แอดมิน\nกรุณากรอกชื่อผู้ใช้ที่ต้องการลบสิทธิ์")
        id = input("ระบุชื่อผู้ใช้ที่ต้องการลบสิทธิ์: ")
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if id in data:
                data[id]["isAdmin"] = False
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"ลบสิทธิ์แอดมิน {id} สำเร็จแล้ว\n\n")
            else:
                print(f"ไม่พบชื่อผู้ใช้ {id} ในระบบ\n\n")
        except Exception as e:
            print(e)

    def logout():
        User.userMenu()

    def admin():
        selectList = {
            1: Admin.addSubject,
            2: Admin.editSubject,
            3: Admin.deleteSubject,
            4: Admin.getSubject,
            5: Admin.getStudent,
            6: Admin.editStudent,
            7: Admin.deleteStudent,
            8: Admin.addStudent,
            9: Admin.setAdmin,
            10: Admin.removeAdmin,
            11: Admin.logout
        }
        while True:
            if input("คุณต้องการเข้าสู่เมนูแอดมินใช่หรือไม่ (y/n): ") == "n":
                return
            with open(userPath, "r") as file:
                data = json.load(file)
            if (not getLogin() or not data[getUserName()]["isAdmin"]):
                print("\n\n\nคุณยังไม่ได้ล็อคอินหรือไม่ใช่แอดมิน")
                break
            print("----------------เมนูแอดมิน----------------")
            select = int(input("โปรดเลือก\n1.เพิ่มวิชา\n2.แก้ไขวิชา\n3.ลบวิชา\n4.ดูวิชาทั้งหมด\n5.ดูข้อมูลนักเรียนทั้งหมด\n6.แก้ไขข้อมูลนักเรียน\n7.ลบข้อมูลนักเรียน\n8.เพิ่มข้อมูลนักเรียน\n9.เพิ่มสิทธิ์แอดมิน\n10.ลบสิทธิ์แอดมิน\n11.เมนูผู้ใช้\nคำตอบ:"))
            selectList[select]() if select in selectList else print("Invalid input. Please try again.")
