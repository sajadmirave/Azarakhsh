# create Column
class Column:
    def __init__(self,name,*types):
        self.name = name
        self.types = types

    def __str__(self):
        # create columns query
        return f"{self.name} {' '.join(map(str, self.types))}"