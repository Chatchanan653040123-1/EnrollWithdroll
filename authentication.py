import json
from common import *
from admin import *
from user import *
class Authentication:
    #ล็อคอิน
    def login(userName, password):
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == True:
                print("ยินดีต้อนรับแอดมิน", data[userName]["fname"], data[userName]["lname"])
                callback(True,setAdmin)
                callback(True,setLogin)
                callback(userName, setUserName)
                Admin.admin()
            if userName in data and data[userName]["password"] == password:
                print("ยินดีต้อนรับคุณ", data[userName]["fname"], data[userName]["lname"])
                callback(True,setLogin)
                callback(userName, setUserName)
                User.userMenu()
            elif userName not in data:
                print("ไม่มีชื่อผู้ใช้ในระบบ กรุณาลองใหม่อีกครั้ง")
            else:
                print("รหัสผ่านผิด กรุณาลองใหม่อีกครั้ง")
        except Exception as e:
            print(e)
    #สมัครสมาชิก
    def register(fname, lname, nickname, email, phoneNumber, userName, password):
        if not callback(email, emailStrength):
            return "\n-------------------------\nอีเมลไม่ถูกต้อง\n-------------------------\n"
        if not callback(password,passwordStrength):
            return "\n-------------------------\nรหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร\nรหัสผ่านต้องประกอบไปด้วยตัวอักษรพิมพ์ใหญ่ พิมพ์เล็ก และตัวเลข\n-------------------------\n"
        try:
            with open(userPath, "r") as file:
                data = json.load(file)  
            newData = {userName:{"fname":fname,"lname":lname,"nickname":nickname,"email":email,"phoneNumber":phoneNumber,"password":password,"isAdmin":False,"subject":[]}}
            if userName in data:
                return "มีชื่อผู้ใช้นี้อยู่ในระบบแล้ว"
            data.update(newData) 
            with open(userPath, "w") as file:
                json.dump(data, file, indent=4)
            return "สมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ"
        except Exception as e:
            return e
        