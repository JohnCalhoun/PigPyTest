from threading import Thread
from schema import schema
import json

class PigPyTest(Thread):
    "Class to test pig scripts in a unittest like way"

    def __init__(self,filename=None,variables=None):
        super(pipeline,self).__init__()  
        if filename:
            self.load_config_from_file(filename)
        elif variables:
            self.load_config_from_dict(filename)

    def load_config_from_dict(self,dictionary):
        self.input=dictionary['inputs'] 
        self.output=dictionary['outputs'] 
        self.script=dictionary['script'] 
        self.opts=dictionary['opts'] 

    def load_config_from_file(self,filename):
        with open(filename, 'r') as f:
            var=json.load(f)
        self.load_config_from_dict(var)
    
    def run(self):
        self.edit_script(self.input,self.output,self.script)
        self.run_script(self.tmp_script)
        self.compare(self.outputs)
  
    def edit_script(self,inputs,outputs,script):
        #load script
        #replace input aliases with load statements
        #append store statements after output aliases
        #save to tmp  
        pass

    def run_script(self,script,opts):
        #build pu command
            #script
            #opts
        pass

    def compare(self,outputs):
        for output in outputs
            A=self.parse_pig_data(fileA)
            B=self.parse_pig_data(fileB)
        #sort A and B
        #filter out lines that are equal

    def parse_pig_data(self,fileA):
        #replace 
        #then eval
        pass   



