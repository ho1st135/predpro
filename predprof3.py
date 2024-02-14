import csv
with open('vacancy.csv', encoding = 'utf8') as file:
    reader = csv.reader(file, delimiter = ';')
    answer = list(reader)
    print(answer)
    name = None
    while name != 'None':
        name = input('Введите название компании: ')
        for salary, work, cs, role, company in answer:
            #перебиираем все столбцы, далее спрашиваем есть ли введенное пользователем значение в списке компаний
            if name in company:
                print(f'{role}. З/п составит: {salary}')
    if name == 'None':
        print('К сожалению, ничего не удалось найти')
