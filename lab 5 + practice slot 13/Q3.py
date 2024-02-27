def q1():
    dict1 = {'Ten' : 10, 'Twenty' : 20, 'Thirty' : 30}
    dict2 = {'Thirty' : 30, 'Fourty' : 40, 'Fifty' : 50}
    
    dict3 = {**dict1, **dict2}
    print(dict3)

def q2():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                    }
                }
            }
        }
    print(sampleDict['class']['student']['marks']['history'])

