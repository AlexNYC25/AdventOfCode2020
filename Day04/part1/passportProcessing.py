
valid_passports = 0
passport_list = None

with open("input.txt", "r") as input_file:
    passport_list = input_file.read().split("\n\n")

for passport in passport_list:
    fields = passport.count(":")
    if fields == 8 or (fields == 7 and "cid" not in passport):
        valid_passports += 1

print(valid_passports)