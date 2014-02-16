import sqlite3


class ИмяОбъекта:

    def __init__(self, ИмяПоля, Поле2):
        self.ИмяПоля = ИмяПоля
        self.Поле2 = Поле2

    def ИмяМетода(self, condition, value):
        if condition:
            return value * value
        else:
            for _ in range(100): value *= 1.1
            return value

    def НайтиПользователя(self, name):
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        res = cur.execute("""
                SELECT user.id FROM user WHERE user.login = :name;
            """, {"name":name})
        res = res.fetchall()
        cur.close()
        conn.close()
        return res


class CustomClass:

    def __init__(self, int_field, float_field):
        self.int_field = int_field
        self.float_field = float_field

    def concatenation(self, f_string, s_string, th_string):
        res = f_string + s_string + th_string
        return res

    def find_user(self, email):
        conn = sqlite3.connect("users.db")
        cur = conn.cursor()
        res = cur.execute("""
                SELECT user.id FROM user WHERE user.email = :email;
            """, {"email":email})
        res = res.fetchall()
        cur.close()
        conn.close()
        return res


