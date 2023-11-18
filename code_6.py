import sqlite3
import json
import xml.etree.ElementTree as ET
from ftplib import FTP

class Student:
    def __init__(self, last_name, first_name, middle_name, group, birth_date=None, address=None):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name
        self._group = group
        self._birth_date = birth_date
        self._address = address

    @property
    def full_name(self):
        return f"{self._last_name} {self._first_name} {self._middle_name}"

    @property
    def group(self):
        return self._group

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def address(self):
        return self._address

    def set_birth_date(self, birth_date):
        self._birth_date = birth_date

    def set_address(self, address):
        self._address = address

    def to_dict(self):
        return {
            "last_name": self._last_name,
            "first_name": self._first_name,
            "middle_name": self._middle_name,
            "group": self._group,
            "birth_date": self._birth_date,
            "address": self._address
        }

class Success:
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = scores

    def average_score(self):
        return sum(self.scores) / len(self.scores)

class DesiredSuccess(Success):
    def __init__(self, subjects, scores):
        super().__init__(subjects, scores)

class StudentData:
    def __init__(self, student, real_success, desired_success):
        self.student = student
        self.real_success = real_success
        self.desired_success = desired_success

class DataStorage:
    def save(self, data, filename):
        pass

class JSONDataStorage(DataStorage):
    def save(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename} successfully.")

class XMLDataStorage(DataStorage):
    def save(self, data, filename):
        root = ET.Element("data")
        student_elem = ET.SubElement(root, "student")
        student_elem.set("full_name", data.student.full_name)
        student_elem.set("group", data.student.group)

        real_success_elem = ET.SubElement(student_elem, "real_success")
        for subject, score in zip(data.real_success.subjects, data.real_success.scores):
            subject_elem = ET.SubElement(real_success_elem, "subject")
            subject_elem.set("name", subject)
            subject_elem.text = str(score)

        desired_success_elem = ET.SubElement(student_elem, "desired_success")
        for subject, score in zip(data.desired_success.subjects, data.desired_success.scores):
            subject_elem = ET.SubElement(desired_success_elem, "subject")
            subject_elem.set("name", subject)
            subject_elem.text = str(score)

        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Data saved to {filename} successfully.")

class FTPUploader:
    def __init__(self, filename, ftp_connection):
        self.filename = filename
        self.ftp_connection = ftp_connection

    def upload(self):
        try:
            ftp = FTP(self.ftp_connection['host'])
            ftp.login(self.ftp_connection['user'], self.ftp_connection['password'])

            remote_directory = "/upload"
            ftp.cwd(remote_directory)

            with open(self.filename, 'rb') as file:
                ftp.storbinary(f'STOR {self.filename}', file)

            ftp.quit()
            print(f"File '{self.filename}' uploaded successfully to FTP server.")
        except Exception as e:
            print(f"Error uploading file to FTP server: {str(e)}")

class DatabaseSetup:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_data (
                id INTEGER PRIMARY KEY,
                student_json TEXT,
                real_success_json TEXT,
                desired_success_json TEXT
            )
        ''')

        conn.commit()
        conn.close()
        print("Database table created successfully.")

if __name__ == "__main__":
    db_setup = DatabaseSetup("student_database.db")
    db_setup.create_table()

    student = Student("Doe", "John", "Smith", "CS101", "2000-01-01", "123 Main St")
    real_success = DesiredSuccess(["Math", "Physics", "Chemistry"], [90, 85, 92])
    desired_success = DesiredSuccess(["Math", "Physics", "Chemistry"], [95, 90, 95])
    student_data = StudentData(student, real_success, desired_success)

    student_data_dict = {
        "student": student.to_dict(),
        "real_success": {
            "subjects": real_success.subjects,
            "scores": real_success.scores
        },
        "desired_success": {
            "subjects": desired_success.subjects,
            "scores": desired_success.scores
        }
    }

    json_storage = JSONDataStorage()
    json_storage.save(student_data_dict, "student_data.json")
    print("Data saved to JSON file successfully.")

    xml_storage = XMLDataStorage()
    xml_storage.save(student_data, "student_data.xml")
    print("Data saved to XML file successfully.")

    ftp_connection_info = {
        "host": "31.28.191.34",
        "user": "student@goodshop.com.ua",
        "password": "zu^DR{znaaYT"
    }
    uploader = FTPUploader("student_data.json", ftp_connection_info)
    uploader.upload()
    
    # Add data to the database
    conn = sqlite3.connect("student_database.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO student_data (student_json, real_success_json, desired_success_json)
        VALUES (?, ?, ?)
    ''', (json.dumps(student_data_dict), json.dumps(real_success.__dict__), json.dumps(desired_success.__dict__)))
    conn.commit()
    conn.close()
    print("Data added to the database successfully.")
