from common import *
import json
class Enroll:
    def enroll():
        if (not getLogin()):
            print("คุณยังไม่ได้ล็อคอิน")
            return
        elif input("คุณต้องการลงทะเบียนเรียนใช่หรือไม่ (y/n): ") == "n":
            return
        print("---------------\nรายวิชาที่สามารถลงทะเบียนได้มีดังนี้\n---------------")
        try:
            with open(subjectPath, "r") as file:
                data = json.load(file)
            for i in data:
                print(f"{i} {data[i]['subject']} {data[i]['section']} {data[i]['teacher']}")
            print("---------------")
            subject = input("กรุณากรอกรหัสวิชาที่ต้องการลงทะเบียน: ")
            if subject in data:
                with open(userPath, "r") as file:
                    data = json.load(file)
                if subject in data[getUserName()]["subject"]:
                    print("คุณลงทะเบียนวิชานี้ไปแล้ว")
                    return
                data[getUserName()]["subject"].append(subject)
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"ลงทะเบียน {subject} สำเร็จแล้ว")
        except Exception as e:
            print(e)
    def withdraw():
        if (not getLogin()):
            print("คุณยังไม่ได้ล็อคอิน")
            return
        elif input("คุณต้องการถอนวิชาใช่หรือไม่ (y/n): ") == "n":
            return
        print("---------------\nรายวิชาที่สามารถถอนได้มีดังนี้\n---------------")
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            for i in data[getUserName()]["subject"]:
                print(i)
            print("---------------")
            subject = input("กรุณากรอกรหัสวิชาที่ต้องการถอน: ")
            if subject in data[getUserName()]["subject"]:
                data[getUserName()]["subject"].remove(subject)
                with open(userPath, "w") as file:
                    json.dump(data, file, indent=4)
                print(f"ถอน {subject} สำเร็จแล้ว")
        except Exception as e:
            print(e)