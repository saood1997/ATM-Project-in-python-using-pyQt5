import csv
import os

def join():
    directory = "Data"
    name = "usersdata.csv"
    filename = os.path.join(directory, name)
    return filename

#when 1 is entered from main(login_user)
def data():
    filename = join()
    d = {}
    # with open(filename, "r") as ap:
    with open(filename, "r") as rd:
            reader = csv.reader(rd) # This is an object for reader
            for us in reader:
                    us[1] = us[1]
                    us[2] = float(us[2])
                    d[us[0]] = us[1],us[2]
            # print(d)
            return d
        
    
    
d = {'ali':(1111,0)}

if 'ali' in d.keys() and 1111 in d['ali']:
    print("OK")
else:
    print("NO")
