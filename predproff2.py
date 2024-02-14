import csv
with open('vacancy.csv', encoding = 'utf8') as file:
    reader = csv.reader(file, delimiter = ';')
    answer = list(reader)
    #print(answer)
    for salary, workt, cs, role, company in answer:
        #перебираю столбцы и смотрю есть ли там классный руководитель
        if 'классный руководитель' in role:
            print(f'В компании {company} есть заданная профессия: {role}, з/п в такой компании составит: {salary}')