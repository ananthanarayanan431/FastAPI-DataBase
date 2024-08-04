# Database.py

import mysql.connector 

class Database:

    def __init__(self) -> None:
        self.connection = None
        self.mycursor = None 

    def connect(self):
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="python",
        )

        try:
            if db.is_connected():
                print("Connection is Established!")
                self.connection = db
                self.mycursor = db.cursor()
                self.mycursor.execute("CREATE DATABASE IF NOT EXISTS fastapi")
                self.mycursor.execute("USE fastapi")
                self.mycursor.execute("CREATE TABLE IF NOT EXISTS person (ItemID int PRIMARY KEY AUTO_INCREMENT, Task varchar(100), isCompleted varchar(50))")
        except Exception as e:
            print(f"Error during connection: {e}")

    def Insert_data(self, Task, isCompleted):
        if self.connection and self.mycursor:
            try:
                self.mycursor.execute("INSERT INTO person (Task, isCompleted) VALUES (%s, %s)", (Task, isCompleted))
                self.connection.commit()
                print("Data is Entered Successfully!")
            except Exception as e:
                print(f"Error inserting data: {e}")
        else:
            print("Cannot Insert Data!")

    def update_data(self, TaskId, isCompleted):
        if self.connection and self.mycursor:
            try:
                self.mycursor.execute("UPDATE person SET isCompleted=%s WHERE ItemID=%s", (isCompleted, TaskId))
                self.connection.commit()
                print("Update was Successful!")
            except Exception as e:
                print(f"Error updating data: {e}")
        else:
            print("Cannot Update Data!")

    def delete_data(self, TaskId):
        if self.connection and self.mycursor:
            try:
                self.mycursor.execute("DELETE FROM person WHERE ItemID=%s", (TaskId,))
                self.connection.commit()
                print("Deletion was Successful!")
            except Exception as e:
                print(f"Error deleting data: {e}")
        else:
            print("Item not found!")

    def Get_all(self):
        if self.connection and self.mycursor:
            try:
                self.mycursor.execute("SELECT * FROM person")
                result = self.mycursor.fetchall()  # Use fetchall() to get all rows
                return result
            except Exception as e:
                print(f"Error fetching data: {e}")
                return None 
        else:
            print("Connection or cursor error!")
            return None

if __name__=="__main__":
    obj = Database()
    obj.connect()
    # obj.Insert_data("Checking", "No")
    print(obj.Get_all())
