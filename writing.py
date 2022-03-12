import json
  
# python object(dictionary) to be dumped
dict1 ={
    "emp1": {
        "name": "Lia",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
  
# the json file where the output must be stored
out_file = open("data.json", "a")
  
json.dump(dict1, out_file, indent = 6)
  
out_file.close()