import time
from lists import my_list

def output(my_list):
    if my_list == []:
        print("Конец списка.")
    else:
        print(my_list[0])
        output(my_list[1:])

output(my_list)
time.sleep(1.75)
exit()
