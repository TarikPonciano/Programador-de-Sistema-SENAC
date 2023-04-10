import csv

with open("test.csv", "w") as testCSV:
    csvHeaders = ["nome", "idade", "salario"]
    csvWriter = csv.DictWriter(testCSV, fieldnames=csvHeaders)
    listaPessoas = [{"nome": "Manoel", "idade": 25, "salario": 3000},
                    {"nome": "Juliana", "idade": 30, "salario": 4000}]
    csvWriter.writeheader()

    for pessoa in listaPessoas:

        csvWriter.writerow(pessoa)
