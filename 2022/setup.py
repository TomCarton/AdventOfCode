#!/usr/bin/python3
import sys
import os
import stat

day = int(sys.argv[1])

folder_name = f'day{day:02}'
if os.path.exists(folder_name):
    print(f"!Error: Folder {folder_name} already exists!")
    sys.exit(1)

os.mkdir(folder_name)
print(f"Folder {folder_name} created.")

## - Python file
filename = f'{folder_name}/day{day:02}.py'
with open(filename, 'w') as f:
    f.write(f"""#!/usr/bin/python3
import sys
import os

# Advent of Code 2022
# Day {day:02}

def main(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    # Part One:
    # 

    print("Part One: ")

    # Part Two:
    # 

    print("Part Two: ")


# Main
if __name__ == '__main__':
    path = os.path.dirname(os.path.join(os.getcwd(), sys.argv[0]).replace("/./", "/"))

    filename = os.path.join(path, 'input.txt')
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    main(filename)
""")

# make python file executable
st = os.stat(filename)
os.chmod('somefile', st.st_mode | stat.S_IEXEC)

## - Input.txt file
filename = f'{folder_name}/input.txt'
file = open(filename, "w")
file.write("")
file.close()
