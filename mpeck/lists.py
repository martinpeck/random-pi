import string
import json
import csv

result = dict(name = "Martin", score = 19, time = 15)

t = string.Template("$name scored $score and did it in $time seconds")

message = t.substitute(name=result["name"],
                        score=result["score"],
                        time = result["time"])

print(message)

result_json = json.dumps(result)
print(result_json)

results = []

with open("results.csv", "w") as results_file:
    fieldnames = ['name', 'score', "time"]
    writer = csv.DictWriter(results_file, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow()
    
    for row in reader:
        results.insert(row)


#reader = csv.DictReader(results_file)
#    for row in reader:
#        results.insert(row)
#
#    print(results)

