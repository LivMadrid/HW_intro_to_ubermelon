# opens file text
log_file = open("um-server-01.txt")

# defines function for 
def sales_reports(log_file):
# iterate over each line in the file
    for line in log_file:
# method .rstrip removes blanks spaces from line
        line = line.rstrip()
# selects index of line to reference day of week ex. Sat = saturday
        day = line[0:3]
#verify if day of week matches the sales_report day searching for
# change this to Monday for Mel
        if day == "Mon":
            print(line)


sales_reports(log_file)
