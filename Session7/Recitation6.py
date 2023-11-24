import sys

infile = open(sys.argv[1], "r")
outfile = open(sys.argv[2], "w")
count = 0

while True: 
    line = infile.readline()
    count += 1
    if not line:
        break
    if count  >=5:
        count = 1

    if count == 1:
        outfile.write(f">{line[1:]}\n")

    elif count == 2:
        outfile.write(f"{line}\n")


infile.close()
outfile.close()  