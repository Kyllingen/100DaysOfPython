import requests

def get_questions():
    '''get questions from open trivia DB'''
    parameters = {
        "amount": 10,
        "type": "boolean"
    }
    try:
        response = requests.get("https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()
    except:
        print("Error trying to fetch data from database")
        
    data = response.json()
    
    return data["results"]
   

question_data = get_questions()