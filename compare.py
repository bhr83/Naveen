import difflib, sys

srcfile = sys.argv[1]
destfile = sys.argv[2] 
with open(srcfile) as src_file:
    src_file_text = src_file.readlines()
 
with open(destfile) as dest_file:
    dest_file_text = dest_file.readlines()
 
# Find and print the diff:
for line in difflib.unified_diff(
        src_file_text, dest_file_text, fromfile=srcfile, 
        tofile=destfile, lineterm=''):  
    if (line.startswith("-") or line.startswith("+")) and not line.startswith(" "):
        print(line)