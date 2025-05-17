from database import create_connection
import sqlite3

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print("🗑️ User deleted.")
    
    
def advanced_search(user_id, name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ? OR id LIKE ?", ('%' + name + '%',user_id))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_course(name, course_id, units):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO courses (name, course_id,units) VALUES (?, ?, ?)", (name, course_id, units))
        conn.commit()
        print("Course added successfully.")
    except sqlite3.IntegrityError:
        print(" Course ID must be unique.")
    conn.close()

def insert_userToCourse(user_name, course_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE name = '?'", (user_name))
    user_exists = cursor.fetchone()[0] > 0
    if user_exists:
        try:
            cursor.execute("INSERT INTO user_course (user_name, course_id) VALUES (?, ?)", (user_name, course_id))
            conn.commit()
        except sqlite3.IntegrityError:
            print()
    else:
        print(f"{user_name} doesn't exist, please check.")
    conn.close()

def search_data(keyword):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_course WHERE user_id LIKE ? OR course_id LIKE ?", ('%' + keyword + '%', '%' + keyword + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows
    
def view_courses():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    conn.close()
    return rows

# insert_userToCourse('Ada',1)