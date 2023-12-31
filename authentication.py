import json
from common import setAdmin, setLogin, setUserName, common, userPath, emailStrength, passwordStrength
from admin import Admin
from user import User
class Authentication:
    #ล็อคอิน
    def login(userName, password):
        try:
            with open(userPath, "r") as file:
                data = json.load(file)
            if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == True:
                print("\n\nยินดีต้อนรับแอดมิน", data[userName]["fname"], data[userName]["lname"])
                common(True,setAdmin)
                common(True,setLogin)
                common(userName, setUserName)
                Admin.admin()
            if userName in data and data[userName]["password"] == password and data[userName]["isAdmin"] == False:
                print("\n\nยินดีต้อนรับคุณ", data[userName]["fname"], data[userName]["lname"])
                common(True,setLogin)
                common(userName, setUserName)
                User.userMenu()
            elif userName not in data:
                print("\n\nไม่มีชื่อผู้ใช้ในระบบ กรุณาลองใหม่อีกครั้ง")
            elif data[userName]["password"] != password:
                print("\n\nรหัสผ่านผิด กรุณาลองใหม่อีกครั้ง")
            else:
                print("\n\nกรุณา Login อีกครั้ง")
        except Exception as e:
            print(e)
    #สมัครสมาชิก
    def register(fname, lname, nickname, email, phoneNumber, userName, password):
        if not common(email, emailStrength):
            return "\n-------------------------\nอีเมลไม่ถูกต้อง\n-------------------------\n"
        if not common(password,passwordStrength):
            return "\n-------------------------\nรหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร\nรหัสผ่านต้องประกอบไปด้วยตัวอักษรพิมพ์ใหญ่ พิมพ์เล็ก ตัวเลข และตัวอักษรพิเศษ\n-------------------------\n"
        try:
            with open(userPath, "r") as file:
                data = json.load(file)  
            newData = {userName:{"fname":fname,"lname":lname,"nickname":nickname,"email":email,"phoneNumber":phoneNumber,"password":password,"isAdmin":False,"subject":[]}}
            if userName in data:
                return "\n\nมีชื่อผู้ใช้นี้อยู่ในระบบแล้ว"
            data.update(newData) 
            with open(userPath, "w") as file:
                json.dump(data, file, indent=4)
            return "\n\nสมัครสมาชิกสำเร็จ กรุณาเข้าสู่ระบบ"
        except Exception as e:
            return e
        