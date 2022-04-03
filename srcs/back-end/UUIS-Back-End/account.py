#coding:utf-8
import sqlite3


def create_sql():
    sql = sqlite3.connect("user_data.db")
    sql.execute(
        """create table if not exists
        %s(
        %s integer primary key autoincrement,
        %s varchar(128),
        %s varchar(128))"""
        % ('user',
           'id',
           'name',
           'passworld'))
    sql.close()
    return sql



def add_data():
    input_name = str(input("Username："))
    input_password = str(input("Password："))
    sql = sqlite3.connect("user_data.db")
    sql.execute("insert into user(name,passworld) values(?,?)",
                (input_name, input_password))
    sql.commit()
    sql.close()


def show_all_data():
    sql = sqlite3.connect("user_data.db")
    data = sql.execute("select * from user").fetchall()
    sql.close()
    return data


def register():
    while 1:
        input_name = str(input("Password："))
        sql = sqlite3.connect("user_data.db")
        data = sql.execute("select * from user where name='%s'" % input_name).fetchone()
        if not data:
            input_password = str(input("Password："))
            sql.execute("insert into user(name,passworld) values(?,?)",
                        (input_name, input_password))
            sql.commit()
            print("Register successfully.")
            sql.close()
            break
        else:
            print("Account already exists.")




def showdate(username):
    sql = sqlite3.connect('user_data.db')
    data = sql.execute("select * from user where name='%s'"% username).fetchone()
    sql.close()
    return data


def val():
    while 1:
        name = input("Username:")
        data = showdate(name)
        if data:
            passworld = input("Password:")
            if data[2] == passworld:
                print("Login in successfully")
                break
            else:
                print("Wrong password")
        else:
            print("Wrong username")



def option():
    while 1:
        optionflag = """R: register an account\nL: login in\nQ: quit\nYour option:"""
        cho = input(optionflag)
        if cho == 'R':
            register()
            break
        if cho == 'L':
            val()
            break
        if cho == 'Q':
            break
        else:
            print("Wrong Input")


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     create_sql()
#     option()

