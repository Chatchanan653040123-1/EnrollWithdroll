from authentication import Authentication as auth
def main():
    try:
        while True:
            select = int(input("ยินดีต้อนรับ โปรดเลือก\n1.สมัครสมาชิก\n2.ล็อคอิน\nคำตอบ:"))
            attemps = 0
            if select == 1:
                print("สมัครสมาชิกกรุณากรอกตามแบบฟอร์มนี้")
                fname = input("ชื่อ : ")
                lname = input("นามสกุล : ")
                nickname = input("ชื่อเล่น : ")
                email = input("อีเมล : ")
                phoneNumber = input("เบอร์โทรศัพท์ : ")
                userName = input("ชื่อผู้ใช้ : ")
                password = input("รหัสผ่าน : ")
                print(auth.register(fname, lname, nickname, email, phoneNumber, userName, password))
            elif select == 2:
                userName = input("ชื่อผู้ใช้:")
                password = input("รหัสผ่าน:")
                auth.login(userName, password)
            elif attemps == 3:
                print("คุณใส่กรอกผิดเกินกว่าที่กำหนด โปรดลองใหม่อีกครั้งในภายหลัง")
                attemps = 0
                break
            else:
                attemps += 1
                print("-------------\n-------------\nกรุณาเลือกใหม่อีกครั้ง")
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น\n")
while True:
    main()