#파이썬을 실행할때 python 파일이름 임의문서로 쳐주셔야되요 예를들어 python ex16.py 1.txt
import sys from argv

scripts, filename = args

print('We're going to erase {}.'.format(filename))
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input(?)

print("Opening the file...")
target = open(filename, 'r')

print("Truncating the file.  Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
