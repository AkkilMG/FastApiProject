
from bson import ObjectId
from pymongo import MongoClient #, Connection
import subprocess

class Database:
    def __init__(self): #, url:str):
        """
        url: MongoDB url
        """
        try:
            myclient = MongoClient()
            # connection = Connection()
            # db = connection["studentDB"]
            # collection = db["studentCol"]
            mydb = myclient[f"studentDB"]
            self.mydb = mydb
            mycollection = self.mydb[f"studentCol"]
            self.mycollection = mycollection
        except Exception as e:
            print(f"Error: {e}")
            exit(0)
        
    def insert(self, name:str, usn:str, sem:int, gender:str, marks):
        """
        name: Name of the Student
        usn: USN of the Student
        sem: Sem of the Student
        gender: Gender of the Student
        marks: Array of Marks Student Secured
        """
        try:
            if gender not in ["male", "Male", "female", "Female"]:
                print("Enter correct gender")
                exit(0)
            try:
                gender = gender.lower()
            except Exception:
                gender = gender
            try:
                usn = usn.upper()
            except Exception:
                usn = usn
            total = marks[0]+marks[1]+marks[2];
            record = {
                "name": name,
                "usn": usn,
                "sem": sem,
                "gender": gender,
                "marks": marks,
                "total": total
            }
            self.mydb.studentCol.insert_one(record)
        except Exception as e:
            print(f"Error: {e}")
            exit(0)
        
    def find(self, key:str, value):
        """
        key: Key to check
        value: Value that you need to find
        """
        try:
            fd = []
            for i in self.mydb.studentCol.find({f'{key}': value}):
                fd.append(i)
            return fd
        except Exception as e:
            print(f"Error: {e}")
            exit(0)
    
    def getAll(self):
        """
        
        """
        try:
            name = []
            usn = []
            sem = []
            marks = []
            gender = []
            total = []
            id = []
            for i in self.mydb.studentCol.find({}):
                name.append(i["name"])
                usn.append(i["usn"])
                sem.append(i["sem"])
                marks.append(i["marks"])
                gender.append(i["gender"])
                total.append(i["total"])
                id.append(str(i["_id"]))
            
            data = [name, usn, sem, marks, gender, total, id]
            return data
        except Exception as e:
            print(f"Error: {e}")
            exit()

    def checker(self, key:str, value):
        """
        key: Key to check
        value: Value that you need to id
        """
        try:
            a = self.mydb.studentCol.find({f'{key}': value})
            try:
                a = a[0]["_id"]
                return True
            except Exception:
                return False
        except Exception as e:
            print(f"Error: {e}")
            exit()

    def getId(self, key:str, value):
        """
        key: Key to check
        value: Value that you need to id
        """
        try:
            a = self.mydb.studentCol.find({f'{key}': value})
            return a[0]["_id"]
        except Exception as e:
            print(f"Error: {e}")
            exit()

    def update(self, id:str, key:str, value):
        """
        id: Id to access the object
        key: Key to check
        value: Value that you need want to update
        """
        try:
            if key == "sem":
                value = int(value)

            self.mycollection.update_one({"_id": ObjectId(id)}, {"$set": {f'{key}': value}})
        except Exception as e:
            print(f"Error: {e}")
            exit()
    
    # def update_marks(self, id:str, marks1:int, marks2:int, marks3:int):
    #     """
    #     id: Id to access the object
    #     marks1: Marks
    #     marks2: Marks
    #     marks3: Marks
    #     """
    #     try:
    #         marks = [marks1, marks2, marks3]
    #         self.mycollection.update_one({"_id": ObjectId(id)}, {"$set": {'marks': f"{value}"}})
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         exit()

    def delete(self, id:str):
        """
        id: Id to delete the object
        """
        try:
            self.mycollection.delete_one({'_id': ObjectId(id)})
        except Exception as e:
            print(f"Error: {e}")
            exit()
        
# ============ Database Test ============ #
# d = Database() #"mongodb://localhost:27017")
# d.insert("Akkil", "4SF21IS006", 3, "Male", [28, 25, 29])
# id = d.getId("usn", "4SF21IS006")
# d.update(ObjectId('63aa7379f0bf5489d499da23'), "marks2", "20")
# d.delete('63a6e144ae24135f7d97206f')
# print(d.getAll())