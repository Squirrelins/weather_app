# # Open file and read the last 50 characters.

# with open(r"reportcard.txt", "") as r:
#     r.seek(-51, 2)
#     print(r.tell())
#     lines = r.read(50)
#     print(lines)

# Open the file in append mode and write some text at the end of the file.

# with open(r"reportcard.txt", "r+") as r:
#     r.seek(0, 2)
#     r.write("\nThis is the end of the file.")
#     r.seek(0, 0)
#     lines = r.read()
#     print(lines)

# 5. Open the file in read mode and read the content of the file line by line and print at the same time.

# with open(r"reportcard.txt", "r") as r:
#     lines = r.readlines()
#     for line in lines:
#         print(line)

