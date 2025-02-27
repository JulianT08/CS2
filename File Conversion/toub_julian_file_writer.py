import csv
fhand = open('student_data_cs2.txt')
with open('student_data.csv', 'w', newline='') as file:

    for line in fhand:
        ID = line[0:4].strip()
        first_name = line[4:19].strip()
        last_name = line[21:30].strip()
        grade = line[36:42].strip()
        GPA = line[42:45].strip()
        birthday = line[45:58].strip()
        gender = line[60:66].strip()
        class_rank = line[67:76].strip()
        attendence = line[76:80].strip()
        honors = line[86:93].strip()
        sports = line[93:102].strip()
        club_count = line[102:112]
        file.write(ID + ',' + first_name + ',' + last_name + ',' + grade + ',' + GPA + ',' + birthday + ',' + gender + ',' + class_rank + ',' + attendence + ',' + honors + ',' + sports + ',' + club_count + '\n')


