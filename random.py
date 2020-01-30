import random
import pymysql

m30 =[4,6,9,11]
m31 =[1,3,5,7,8,10,12]
m28 = 2
fam_names = list("김이박최강고윤엄한배성백정송황서천방지마피")
first_name = list("건성현욱정민상주동혜도모영규선재현호춘시구우인성마무병별은회홍환솔철하라석훈")
years =list(range(70,99))
month =list(range(1,13))
days =list(range(1,32))
days30 =list(range(1,31))
days28 = list(range(1,29))
alphas =list("abcdefghijklmnop"*3)
nums =list("0123456789" *4)

def nr(n=4) :
    return "".join(random.sample(nums,n)) 

def ar(n=5) :
    return "".join(random.sample(alphas,n))

def make_birth():
    y = random.choice(years)
    m = random.choice(month)
    d = random.choice(days)
    if m in m30 and d>30 :
        d= random.choice(days30)
    elif m==2 and d >28 : 
        d= random.choice(days28)
    return "{}{:02d}{:02d}".format(y,m,d)

def make_data() :
    sung = random.choice(fam_names)
    name ="".join(random.sample(first_name,2))
    tel ="010-{}-{}".format(nr(), nr())
    email ="{}@gmail.com".format(ar(random.randrange(3,9)))
        
    return (sung+name,tel,email,make_birth())

   

data =[]
for i in range(0,100):
    data.append(make_data())


print(data)


conn = pymysql.connect(
    host ='localhost',
    user ="root",
    password ="vetec3721",
    port = 3306,
    db = "person",
    charset ='utf8'
)

with conn : 
    cur =conn.cursor()
    sql = "insert into student values(%s,%s,%s,%s)"
    cur.executemany(sql,data)
    print("Account row count is ",cur.rowcount)
    conn.commit()
