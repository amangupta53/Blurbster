print("BLURBSTER v0.1a")
print("A simple python script to generate common blurbs.")

# Open File and store content in object
dict = open("blurb.txt", "r")
blurb = dict.read()
dict.close()

print("Currently Using blurb.txt")
# Input values from user
instanceid = input("Enter Instance ID: ")
volid = input("Enter Volume ID: ")
az = input("Enter the Availability Zone: ")

#Actual replace logic (Chained as a hack for immutable objects)
ex1 = blurb.replace('instanceid', instanceid)
ex2 = ex1.replace('volumeid', volid)
ex3 = ex2.replace('az', az)

# Output the Blurb
print(ex3)