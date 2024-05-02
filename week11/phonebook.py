import csv
import psycopg2
from config import host, password, db_name, user

def insert_or_update_user(first_name, last_name, phone):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s) "
            "ON CONFLICT (phone) DO UPDATE SET first_name = EXCLUDED.first_name",
            (first_name, last_name, phone)
        )
    conn.commit()

def upload_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            first_name, last_name, phone = row
            insert_or_update_user(first_name, last_name, phone)

def enter_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    with conn.cursor() as cur:
        insert_or_update_user(first_name, last_name, phone)

def update_data():
    new_first_name = input("Enter the new first name: ")
    phone = input("Enter the phone number to update: ")
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE phone = %s",
            (new_first_name, phone)
        )
    conn.commit()
    
def query_with_pagination(limit, offset):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM phonebook LIMIT %s OFFSET %s",
            (limit, offset)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)

# def query_data():
#     with conn.cursor() as cur:
#         cur.execute("SELECT * FROM phonebook WHERE first_name = %s", ('John',))
#     rows = cur.fetchall()
#     for row in rows:
#         print(row)

# def delete_data():
#     phone_to_delete = input("Enter the phone number to delete: ")
#     with conn.cursor() as cur:
#         cur.execute(
#             "DELETE FROM phonebook WHERE phone = %s",
#             (phone_to_delete,)
#         )
#     conn.commit()

def search_by_pattern(pattern):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM phonebook WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s",
            ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%',)
        )
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_by_username_or_phone(identifier):
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM phonebook WHERE first_name = %s OR last_name = %s OR phone = %s",
            (identifier, identifier, identifier)
        )
    conn.commit()
    
def insert_many_users(data):
    invalid_data = []
    for item in data:
        first_name, last_name, phone = item
        if not phone.isdigit() or len(phone) != 10:
            invalid_data.append(item)
            continue
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (first_name, last_name, phone)
            )
    conn.commit()
    return invalid_data


def main():
    while True:
        print("1. Upload from CSV")
        print("2. Enter from console")
        print("3. Update data")
        print("4. Query data with pagination")
        print("5. Delete data")
        print("6. Search by pattern")
        print("7. Insert many contacts")
        print("8. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            file_path = input("Enter the path to the CSV file: ")
            upload_from_csv(file_path)
        elif choice == '2':
            enter_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            limit = int(input("Enter the limit: "))
            offset = int(input("Enter the offset: "))
            query_with_pagination(limit, offset)
        elif choice == '5':
            identifier = input("Enter the username or phone number to delete: ")
            delete_by_username_or_phone(identifier)
        elif choice == '6':
            pattern = input("Enter the pattern to search: ")
            search_by_pattern(pattern)
        elif choice == '7':
            data = [('John', 'Doe', '1234567890'), ('Jane', 'Smith', '555-5678'), ('Michael', 'Johnson', '555-9012')]
            invalid_data = insert_many_users(data)
            if invalid_data:
                print("Invalid data:", invalid_data)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

try:
    conn = psycopg2.connect(
        host=host, 
        user=user,
        password=password,
        database=db_name
    )
    main()
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if conn:
        conn.close()
        print("[INFO] PostgreSQL connection closed")
