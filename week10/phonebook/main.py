import csv
import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres")
cur = conn.cursor()

def upload_from_csv(file_path):
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                row
            )
    conn.commit()

def enter_from_console():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()

def update_data():
    new_first_name = input("Enter the new first name: ")
    phone = input("Enter the phone number to update: ")
    cur.execute(
        "UPDATE phonebook SET first_name = %s WHERE phone = %s",
        (new_first_name, phone)
    )
    conn.commit()

def query_data():
    cur.execute("SELECT * FROM phonebook WHERE first_name = %s", ('John',))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete_data():
    phone_to_delete = input("Enter the phone number to delete: ")
    cur.execute(
        "DELETE FROM phonebook WHERE phone = %s",
        (phone_to_delete,)
    )
    conn.commit()

def main():
    while True:
        print("1. Upload from CSV")
        print("2. Enter from console")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            file_path = input("Enter the path to the CSV file: ")
            upload_from_csv(file_path)
        elif choice == '2':
            enter_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

cur.close()
conn.close()
