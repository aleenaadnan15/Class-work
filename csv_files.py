import csv
# with open('data.csv','r') as fdr:
#     students = csv.reader(fdr)
#     for student in students:
#         print(student)
singal_student = ['Ailn','AI','12345678']
students = [
    ['Ailn','AI','12345678'],
    ['Ailn','AI','12345678'],
    ['Ailn','AI','12345678']
]
print(singal_student)
with open('data.csv','w',newline='') as fdes:
    writer = csv.writer(fdes, delimiter='|')
    # writer.writerow(singal_student)
    for student in students:
        writer.writerow(student)