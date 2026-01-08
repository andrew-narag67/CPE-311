Pole1 = 'A'
Pole2 = 'B'
Pole3 = 'C'
def towerofHanoi(n, Pole1, Pole2, Pole3):
    if n == 1:
        print(f"Move Disk {n} from {Pole1} to {Pole3}" )
        return 
    towerofHanoi(n-1, Pole1, Pole3, Pole2)
    print(f"Move Disk {n} from {Pole1} to {Pole3}")
    towerofHanoi(n-1, Pole2, Pole1, Pole3)
    return

n = int(input("How many disks = ") )
towerofHanoi( n, Pole1, Pole2, Pole3)

"""
How the program works is by implementing the process called recursion, it first initialize the base case of n==1 
therefore the only thing that can be done is to move the first disk for this instance we can call it the smallest disk then it moves 
on to the next disks initialized by (n-1) using this we can call the function to move the top n-1 disk from Pole1 to Pole2 as temporary 
placement then to the destined destination of Pole 3. This  program then moves the largest disk or the nth disk (nth disk is whatever we initialized n to be) 
from Pole1 to Pole3. Lastly moves the n-1 disks again from Pole3 to Pole1 to Pole2 then loops until the disks are solved.

"""