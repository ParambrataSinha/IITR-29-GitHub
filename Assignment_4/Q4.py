# From the following string
# From office@ch.iitr.ac.in Sat Jan 5 09:14:16 2008
# Print out the day of the week from the above line using “split” command. Write a small
# program that looks for lines where the line starts with “From”, split those lines, and then print
# out the third word in the line.

line = 'From office@ch.iitr.ac.in Sat Jan 5 09:14:16 2008'

if line.startswith('From'):
    words = line.split()
    print(words[2])

filename = "/Users/phantom/District/PhantomLab/CodeSpace/GitHub/IITR_29/Assignment_4/mbox.txt"
with open(filename) as f:
    for line in f:
        line = line.strip()
        if line.startswith("From "):
            words = line.split()
            print(words[2])

