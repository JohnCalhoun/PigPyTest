import csv

class schema:
    def __init__(self,filename=None):
        if filename:
            self.load(filename)

    def load(self,filename):
        with open(filename) as f:
            reader=csv.read(f)
        schema_list=reader.readlines() 

    def render(self):
        fields=[":".join([item[0],item[1]]) for item in self.schema_list]
        return("("+','.join(fields)+")")
