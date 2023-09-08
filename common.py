userPath = "userProfile.json"
subjectPath = "subject.json"
userNameCache = ""
isLogin = False
isAdmin = False
domain =[".com",".net",".co.th",".ac.th",".go.th",".or.th",".in.th",".mil",".int",".net",".edu",".gov",".org",".biz",".info",".mobi",".name",".tv",".ws",".asia",".xxx",".idv.tw",".me",".co",".cc",".bz",".de",".tw",".eu",".us",".uk",".ca",".cn",".fr",".in",".jp",".kr",".ru",".sg",".vn",".com.tw",".net.tw",".org.tw",".com.cn",".net.cn",".org.cn",".gov.cn",".co.jp",".co.uk",".co.kr",".co.th",".co.in",".co.id",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve",".co.nz",".co.za",".co.il",".co.at",".co.ve"]

def setUserName(name):
    global userNameCache
    userNameCache = name
def getUserName():
    global userNameCache
    return userNameCache
def setAdmin(status):
    global isAdmin
    isAdmin = status
def setLogin(status):
    global isLogin
    isLogin = status
def getLogin():
    global isLogin
    return isLogin
def getAdmin():
    global isAdmin
    return isAdmin
def passwordStrength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    is_length_valid = len(password) >= 8
    return has_upper and has_lower and has_digit and is_length_valid

def emailStrength(email):
    for i in domain:
        if i in email:
            hasDomain=True
            break
        else:
            hasDomain=False
    hasAt = "@" in email
    hasDot = "." in email
    return hasDomain and hasAt and hasDot
