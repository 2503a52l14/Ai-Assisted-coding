with open("data1.txt", "w") as f1, open("data2.txt", "w") as f2:
    f1.write("First file content\n")
    f2.write("Second file content\n")
print("Files written successfully")
# FIXED: Files closed automatically!
# This code writes to two files and ensures they are properly closed