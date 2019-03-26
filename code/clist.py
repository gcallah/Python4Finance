import sys
import csv

FNAME = 0
LNAME = 1
JOB = 2
EMAIL = 3 

client_file = None  # type: str

if len(sys.argv) < 2:
    print("Must supply a client file.")
    exit(1)

client_file = sys.argv[1]

delimiter = ","  # type: str
if len(sys.argv) > 2:
    delimiter = sys.argv[2]

with open(client_file, "r") as input_file:
    freader = csv.reader(input_file, delimiter=delimiter)
    prev_entry = None
    good_entries = []
    for row_num, entry in enumerate(freader):
        if prev_entry is not None:
            if entry[EMAIL] == prev_entry[EMAIL]:
                print("duplicate email detected: " + entry[EMAIL])
                continue
        good_entries.append(entry)
        # print("For row# " + str(row_num)
            # + " LNAME = " + entry[LNAME] + " EMAIL = " + entry[EMAIL])
        prev_entry = entry

    for entry in good_entries:
        print(" LNAME = " + entry[LNAME] + " EMAIL = " + entry[EMAIL])
              
