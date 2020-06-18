#!/usr/bin/python3
"""
Given the names and grades for each student in a Physics class of
students, store them in a nested list and print the name(s) of any
student(s) having the second lowest grade.

Note: If there are multiple students with the same grade,
order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,
N, the number of students.
The 2N subsequent lines describe each student over
2 lines; the first line contains a student's name,
and the second line contains their grade.

Constraints

1 <= N <= 5

There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print
each one on a new line.

Input (stdin)

    5

    Harsh

    20

    Beria

    20

    Varun

    19

    Kakunami

    19

    Vikas

    21

Expected Output(stdout)

    Beria

    Harsh
"""

if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = []
    for i in range(len(students)):
        grades.append(students[i][1])
    grades = list(set(grades))
    grades.sort()

    names = []
    for i in range(len(students)):
        if grades[1] == students[i][1]:
            names.append(students[i][0])
    names.sort()

    for n in names:
        print(n)
