from enroll import Enroll

class User:
    @staticmethod
    def userMenu():
        while True:
            if input("คุณต้องการลงทะเบียนเรียนหรือไม่ (y/n): ") == "n":
                break
            select = int(input("ยินดีต้อนรับนี่คือเมนู User \n1.ลงทะเบียนเรียน\n2.ถอนการลงทะเบียนเรียน\nYour input:"))
            (Enroll.enroll() if select == 1 else Enroll.withdraw()) if select in [1, 2] else print("กรุณาเลือกใหม่อีกครั้ง")
