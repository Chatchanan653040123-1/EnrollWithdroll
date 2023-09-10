from enroll import Enroll
class User:
    def userMenu():
        while True:
            select = int(input("ยินดีต้อนรับนี่คือเมนู User \n1.ลงทะเบียนเรียน\n2.ถอนการลงทะเบียนเรียน\nYour input:"))
            if select == 1:
                Enroll.enroll()
            elif select == 2:
                Enroll.withdraw()
            else:
                print("กรุณาเลือกใหม่อีกครั้ง")