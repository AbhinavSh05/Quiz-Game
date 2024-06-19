from datetime import date
import time
import mysql.connector
cnx=mysql.connector.connect(user='root',password='Abhinav',host="127.0.0.1",database='gamescore')
mycursor=cnx.cursor()


def game(questions):
    score=0
    for i in questions:
        print(i)
        ans=int(input("Enter your answer:"))
        if ans==questions[i]:
            print("Correct Answer.")
            score+=1
            print(f"your score:{score}")
        else:
            print("wrong answer .")
            print(f"your score:{score}")
    print(f"Thank you ! final score is : {score}")
    return score
        
        


questions={
    "Question1:What is Mysql ?: \n 1.A Programming language. \n 2.Relational Database Management System (RDBMS).":2,
    "Question2:What is the full form of TCP ?: \n 1.Transfer Control protocol. \n 2.Transport control phase.":1,
    "Question3:What is pyhton3 ? : \n 1.Animal \n 2.Programming Language.":2,
    "Question4:what is full form of LAN ?: \n 1.Masters in computer application. \n 2.Local Area Network.":2,
    "Question5:Mwsql is developed by : \n 1.Alphabet. \n 2.Oracle.":2,
}


print("****Welcome to the Quiz *****")
user_name=input("Please enter your user name : ")
print(f"Hey! {user_name}")
curr_date=date.today()
curr_time = time.strftime("%H:%M:%S", time.localtime())
res=game(questions)
sql = "INSERT INTO gamerec (user_name,date,time,score) VALUES (%s, %s,%s,%s)"
val = (user_name,curr_date,curr_time, res)
mycursor.execute(sql, val)
cnx.commit()
print("your score has been recorded..")
print("your previous record is : ")
mycursor.execute("select date,time,score from gamerec where user_name=%s",(user_name,))
previous=mycursor.fetchall()
for i in previous:
    print(f"{i[0].isoformat()}, {i[1]} ,{i[2]}")