class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

emp = employee("coder",1)

print("employee name = ",emp.name)
print("employee id = ",emp.id) 

del emp.id

try:
    print(emp.id)
except Exception as e:
    print("error occurs :",e)

del emp

try:
    print(emp)
except Exception as e:
    print("error occured = ",e)

    

