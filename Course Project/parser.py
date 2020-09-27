data_file = open("Family_tree.txt")
rules_file = open("Family_tree.pl", "w")
lines = data_file.readlines()
list_of_id = []
list_of_names = []
list_of_surnames = []
for line in lines:
    if line.find("@I500") != -1 and line.find("HUSB") == -1 and line.find("WIFE") == -1 and line.find("CHIL") == -1:
        words = line.split()
        id = words[1]
        list_of_id += [id]
    if line.find("GIVN") != -1:
        words = line.split()
        name = words[2]
        list_of_names += [name]
    if line.find("SURN") != -1:
        words = line.split()
        surname = words[2]
        list_of_surnames += [surname]
    if line.find("HUSB") != -1:
        words = line.split()
        husb_id = words[2]
    if line.find("WIFE") != -1:
        words = line.split()
        wife_id = words[2]
    if line.find("CHIL") != -1:
        words = line.split()
        chil_id = words[2]    
        rules_file.write("father(" + list_of_names[list_of_id.index(husb_id)] + "_" + list_of_surnames[list_of_id.index(husb_id)] +", " + list_of_names[list_of_id.index(chil_id)]+ "_" + list_of_surnames[list_of_id.index(chil_id)] + ")." + "\n")
        rules_file.write("mother(" + list_of_names[list_of_id.index(wife_id)] + "_" + list_of_surnames[list_of_id.index(wife_id)] +", " + list_of_names[list_of_id.index(chil_id)]+ "_" + list_of_surnames[list_of_id.index(chil_id)] + ")." + "\n")
data_file.close()
rules_file.close()