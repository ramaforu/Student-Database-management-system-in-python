import mysql.connector
try:
    conn = mysql.connector.connect(user='root',password='',host='127.0.0.1',database='data_science_task')
    cursor = conn.cursor()
    def Add_student():
        
        # get_input()
        # get_total()
        # get_average()
        # get_grade()
        # add_student_db()
        
        print("Add Student")
        name=input("Enter the student name  ")
        dept=input("Enter the student department name  ")
        s1=float(input("Enter the subject 1 mark  "))
        s2=float(input("Enter the subject 2 mark  "))
        s3=float(input("Enter the subject 3 mark  "))
        s4=float(input("Enter the subject 4 mark  "))
        s5=float(input("Enter the subject 5 mark  "))
        total=s1+s2+s3+s4+s5
        avegare_value=total/5
        if avegare_value>=90:
            grade="S"
        elif avegare_value>=80:
            grade="A"
        elif avegare_value>=70:
            grade="B"
        elif avegare_value>=60:
            grade="C"
        elif avegare_value>=50:
            grade="D"
        else:
            grade="E"
        #print(name,dept,s1,s2,s3,s4,s5,total,avegare_value,grade)
        insert_data= (
            "INSERT INTO student_details(Name, Departments, s1,s2,s3,s4,s5,total,average,grade)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            )
        data = (name,dept,s1,s2,s3,s4,s5,total,avegare_value,grade)
        #print(sql)
        try:
            cursor.execute(insert_data, data)
            print("Student Added Successfully")
            conn.commit()
        except:
            conn.rollback()
            
    def Edit_Student():
        #print("Edit Student")
        cursor.execute("SELECT id,Name, Departments FROM student_details")
        for result in cursor.fetchall():
            print(result)
        edit_opt=int(input("Enter the id of student, to cancel enter 0   "))
        if edit_opt:
            search=f"""SELECT * FROM student_details where id={edit_opt}"""
            cursor.execute(search)
            records=cursor.fetchall()
            if records:
                dept=input("Enter the student department name  ")
                s1=float(input("Enter the subject 1 mark  "))
                s2=float(input("Enter the subject 2 mark  "))
                s3=float(input("Enter the subject 3 mark  "))
                s4=float(input("Enter the subject 4 mark  "))
                s5=float(input("Enter the subject 5 mark  "))
                total=s1+s2+s3+s4+s5
                avegare_value=total/5
                if avegare_value>=90:
                    grade="S"
                elif avegare_value>=80:
                    grade="A"
                elif avegare_value>=70:
                    grade="B"
                elif avegare_value>=60:
                    grade="C"
                elif avegare_value>=50:
                    grade="D"
                else:
                    grade="E"
                update=f"""UPDATE `student_details` SET Departments="{dept}",s1={s1}, s2={s2}, s3={s3}, s4={s4}, s5={s4}, total={total},average={avegare_value},grade="{grade}" WHERE  id={edit_opt}"""
                #print(update)
                cursor.execute(update)
                print("Student Update")
                conn.commit()
            else:
                print("Given id is not there...\n")
        
    def Delete_Student():
        #print("Delete Student")
        cursor.execute("SELECT id,Name, Departments FROM student_details")
        for result in cursor.fetchall():
            print(result)
        delte_opt=int(input("Enter the id of student, to cancel enter 0   "))
        search=f"""SELECT * FROM student_details where id={delte_opt}"""
        cursor.execute(search)
        records=cursor.fetchall()
        if records:
            delete_data=f"""DELETE FROM `student_details` where id={delte_opt}"""
            if delte_opt:
                cursor.execute(delete_data)
                print("Student Deleted")
                conn.commit()
            else:
                print("delete failed")
        else:
            print("Given id is not there...\n")
        
    def Get_all_Student():
        #print("Get All Student")
        cursor.execute("SELECT * FROM student_details")
        for result in cursor.fetchall():
            print(result)
        
    def Get_a_Student():
        print("Get a Student")
        searc_opt=int(input("Enter the id of student "))
        search=f"""SELECT * FROM student_details where id={searc_opt}"""
        cursor.execute(search)
        records=cursor.fetchall()
        if records:
            print(records)
        else:
            print("Given id is not there...\n")
    def Exit():
        conn.close()
        print("Exit....")

    def operation_selection(value):
        if value==1:
            Add_student()
            menu()
        elif value==2:
            Edit_Student()
            menu()
        elif value==3:
            Delete_Student()
            menu()
        elif value==4:
            Get_all_Student()
            menu()
        elif value==5:
            Get_a_Student()
            menu()
        elif value==6:
            Exit()
        else:
            print("Please select option as given in menu")
            menu()

    def menu():
        # print("Menu")
        # print("1 Add Student")
        # print("2 Edit_Student")
        # print("3 Delete_Student")
        # print("4 Get_all_Student")
        # print("5 Get_a_Student")
        # print("6 Exit")
        opt=int(input("Menu\n1 Add Student\n2 Edit_Student\n3 Delete_Student\n4 Get_all_Student\n5 Get_a_Student\n6 Exit\nChoose any of the above option  "))
        operation_selection(opt)

    menu()
except:
    print("connection error")