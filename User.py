import os
import json
import hashlib

class user :
    def __init__(self ,name, total , pswd, desc):
        self._name = name
        self._budget=int(total)
        self._expense = 0
        self._remain = int(total)
        self._detail = {}
        self._passwd=hashlib.sha256(pswd.encode('utf-8')).hexdigest()
        for key in self._detail:
            self._expense+=self._detail[key]
        self._remain = self._budget - self._expense
        
        
    def verify(self, pswd):
        if(hashlib.sha256(pswd.encode('utf-8')).hexdigest() == self._passwd):
            return True
        return False

    def add_detail(self, **kwargs):
        for key, value in kwargs.items():
            self._detail[key] = int(value)
            self._expense += int(value)
            self._remain -= int(value)
        with open('budg.json', 'w') as f:
            f.close()
        if os.stat('budg.json').st_size == 0:
            jsonified_s = json.dumps(self.__dict__, indent=4)
            with open("budg.json", "w") as outfile:
                outfile.write(jsonified_s)
                outfile.close()
        else:
            with open('budg.json') as file:
                file_data = json.load(file)
                temp=file_data
                temp.append(self.__dict__)
                with open('budg.json', 'w') as out_file:
                    json.dump(file_data, out_file, indent = 4)


    def update_detail(self , **kwargs):
        k,v
        for key, value in kwargs.items():
            k = key
            v=value
        temp = {k : v}
        if(self._detail.has_key(k)):
            self._detail.update(temp)
        else :
            print("Enter valid Expense!! ")

    def print_remain(self):
        print("The amount remaining is {}". format(self._remain))