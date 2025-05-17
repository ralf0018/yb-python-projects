from database import create_table
from user_manager import *

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced Search")
    print("==== Course Manager ====")
    print("7. Add Course")
    print("8. Assign a User to a Course")
    print("9. Search User Name and Course ID")
    print("0. View all courses")
    

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            name = input("Enter name to search: ")
            user_id = int(input("Enter user ID: "))
            users = advanced_search(user_id, name)
            for user in users:
                print(user)
        elif choice == '7':
            name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            units = int(input("Enter course unit: "))
            add_course(name, course_id, units)
        elif choice == '8':
            user_name = input("Enter user name: ")
            course_id = int(input("Enter course id: "))
            insert_userToCourse(user_name, course_id)
        elif choice == '9':
            name_id = input("Enter course name or user id: ")
            courses = search_data(name_id)
            for course in courses:
                print(course)
        elif choice == '0':
            courses = view_courses()
            for course in courses:
                print(course)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
