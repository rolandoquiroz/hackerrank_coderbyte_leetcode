#!/usr/bin/python3
"""
Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer at position.
    print: Print the list.
    remove e: Delete the first occurrence of integer.
    append e: Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of
followed by lines of commands where each command will be of the

types listed above. Iterate through each command in order and
perform the corresponding operation on your list.

Input Format

The first line contains an integer, denoting the number of commands.
Each line of the

subsequent lines contains one of the commands described above.

Constraints

    The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""

if __name__ == '__main__':
    my_list = []
    N = int(input("Please input your total number of commands: "))
    for i in range(N):
        cmd = input("Please input your command number "+str(i)+" : ")
        cmd_splitted = cmd.split()
        if cmd_splitted[0] == 'pop':
            my_list.pop()
        elif cmd_splitted[0] == 'print':
            print(my_list)
        elif cmd_splitted[0] == 'reverse':
            my_list.reverse()
        elif cmd_splitted[0] == 'sort':
            my_list.sort()
        elif cmd_splitted[0] == 'append':
            my_list.append(int(cmd_splitted[1]))
        elif cmd_splitted[0] == 'insert':
            my_list.insert(int(cmd_splitted[1]), int(cmd_splitted[2]))
        elif cmd_splitted[0] == 'remove':
            my_list.remove(int(cmd_splitted[1]))
        else:
            print("Invalid command")
