#Andrew Jermaine C. Narag                                                                               # 08/01/2026
#CPE 311-CPE22S3 - Computational Thinking with Python                                                   #Engr. Neal Barton James Matira
def print_states(pole_states):
    print(f"  Pole A: {pole_states['A']}")
    print(f"  Pole B: {pole_states['B']}")
    print(f"  Pole C: {pole_states['C']}")
    print("-" * 25)

Pole1_label = 'A'
Pole2_label = 'B'
Pole3_label = 'C'

def towerofHanoi(n, source_label, auxiliary_label, destination_label, pole_states):
    if n == 1:
        disk = pole_states[source_label].pop()
        pole_states[destination_label].append(disk)
        print(f"Move Disk {disk} from {source_label} to {destination_label}")
        print_states(pole_states)
        return

    towerofHanoi(n-1, source_label, destination_label, auxiliary_label, pole_states)

    disk = pole_states[source_label].pop()
    pole_states[destination_label].append(disk)
    print(f"Move Disk {disk} from {source_label} to {destination_label}")
    print_states(pole_states)

    towerofHanoi(n-1, auxiliary_label, source_label, destination_label, pole_states)
    return

n = int(input("How many disks = ") )

pole_states = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

print(f"Initial state for {n} disks:\n")
print_states(pole_states)

towerofHanoi(n, Pole1_label, Pole2_label, Pole3_label, pole_states)

print(f"Final state:\n")
print_states(pole_states)

"""
How the program works is by implementing the process called recursion, it first initialize the base case of n==1
therefore the only thing that can be done is to move the first disk for this instance we can call it the smallest disk then it moves
on to the next disks initialized by (n-1) using this we can call the function to move the top n-1 disk from Pole1 to Pole2 as temporary
placement then to the destined destination of Pole 3. This  program then moves the largest disk or the nth disk (nth disk is whatever we initialized n to be)
from Pole1 to Pole3. Lastly moves the n-1 disks again from Pole3 to Pole1 to Pole2 then loops until the disks are solved.

"""
