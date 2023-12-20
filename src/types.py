class Varchar:
    def __init__(self,length):
        self.length = length
    
    def __str__(self):
        return f"VARCHAR({self.length})"

class NotNull():
    def __str__(self):
        return "NOT NULL"

class Id:
    def __init__(self,title):
        self.title = title

    def __str__(self):
        return f"{self.title}"

class AutoIncrement:
    def __str__(self):
        return "PRIMARY KEY AUTOINCREMENT"

class Integer:
    def __str__(self):
        return "INTEGER"
