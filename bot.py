from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome Your BOT, It has Successfully BORN OUT ! "

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'joke' in incoming_msg:
        # return a joke
        r = requests.get('https://official-joke-api.appspot.com/random_joke')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n {data["setup"]} \n("{data["punchline"]}")'
        else:
            quote = 'I could not retrieve a joke at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'joks' in incoming_msg:
        # return a joke
        r = requests.get('https://v2.jokeapi.dev/joke/Any')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n {data["setup"]} \n("{data["delivery"]}")'
        else:
            quote = 'I could not retrieve a joks at this time, sorry.'
        msg.body(quote)
        responded = True       
    if 'weather' in incoming_msg:
        # return a joke
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=visakhapatnam&appid=d163faeeb15ef8501c8b28c107bf29c9')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n *Visakhapatnam Stats* humidity = {data["main"]["humidity"]}\n weather = {data["weather"][0]["description"]}\nlongitude = {data["coord"]["lon"]} \n latitude ={data["coord"]["lat"]} '
        else:
            quote = 'I could not retrieve weather at this time, sorry.'
        msg.body(quote)
        responded = True      
    if 'bored' in incoming_msg:
        # return a hobby
        r = requests.get('http://www.boredapi.com/api/activity/')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n {data["activity"]} \n *Type* -("{data["type"]}")'
        else:
            quote = 'I could not retrieve anything useful at this time, sorry.'
        msg.body(quote)
        responded = True   
    if 'advice' in incoming_msg:
        # return a hobby
        r = requests.get('https://api.adviceslip.com/advice')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n {data["slip"]["advice"]} '
        else:
            quote = 'I could not retrieve a advice at this time, sorry.'
        msg.body(quote)
        responded = True          
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n "{data["content"]}" \n- {data["author"]}'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'swift' in incoming_msg:
        # return a quote
        r = requests.get('https://api.taylor.rest/')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n"{data["quote"]}"'
        else:
            quote = 'I could not retrieve a taylor swift quotes at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'covid india' in incoming_msg:
        # return a quote
        r = requests.get('https://api.covid19india.org/data.json')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n India \n Active Cases : *{data["statewise"][0]["active"]}* \n Recovered Cases : *{data["statewise"][0]["active"]}* \n Deaths : *{data["statewise"][0]["active"]}*'
        else:
            quote = 'I could not retrieve covid info at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'covid tn' in incoming_msg:
        # return a quote
        r = requests.get('https://api.covid19india.org/data.json')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n Tamil Nadu \n Active Cases : *{data["statewise"][4]["active"]}* \n Recovered Cases : *{data["statewise"][4]["active"]}* \n Deaths : *{data["statewise"][4]["active"]}*'
        else:
            quote = 'I could not retrieve covid info at this time, sorry.'
        msg.body(quote)
        responded = True    
    if 'pic' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'this' in incoming_msg:
        # return a quote
        r = requests.get('http://itsthisforthat.com/api.php?json')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n this : {data["this"]}\nthat : {data["that"]}'
        else:
            quote = 'I could fetch data at this time, sorry.'
        msg.body(quote)
        responded = True  
    if 'number' in incoming_msg:
        # return a quote
        r = requests.get('http://numbersapi.com/random?min=0&max=1000')
        if r.status_code == 200:
            data = r.json()
            quote = f' {data["text"]} '
        else:
            quote = 'I could fetch facts at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'year' in incoming_msg:
        # return a quote
        r = requests.get('http://numbersapi.com/random/year?json')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n {data["text"]} '
        else:
            quote = 'I could fetch facts at this time, sorry.'
        msg.body(quote)
        responded = True            
    if 'sharpe' in incoming_msg:
        # return a quote
        r = requests.get('http://burli.pythonanywhere.com/shayshay/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n "{data["quote"]}"'
        else:
            quote = 'I could not retrieve a shannon sharpe quotes at this time, sorry.'
        msg.body(quote)
        responded = True 
    if 'cat fact' in incoming_msg:
        # return a quote
        r = requests.get('https://meowfacts.herokuapp.com/')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n"{data["data"][0]}"'
        else:
            quote = 'I could not retrieve a cat fact at this time, sorry.'
        msg.body(quote)
        responded = True    
    if 'dice' in incoming_msg:
        # return a quote
        r = requests.get('http://roll.diceapi.com/json/d6')
        if r.status_code == 200:
            data = r.json()
            quote = f'\n"{data["dice"][0]["value"]}"'
        else:
            quote = 'I could not roll a dice at this time, sorry.'
        msg.body(quote)
        responded = True        
    if 'coin' in incoming_msg:
        # return a quote
        r = requests.get('https://api.toys/api/coin_flip')
        if r.status_code == 200:
            data = r.json()
            quote = f' "{data["result"]}"'
        else:
            quote = 'I could not retrieve at this time, sorry. '
        msg.body(quote)
        responded = True         
    if not responded:
        msg.body('I am learning and growing day by day \n- *Be a nerd BOT*')
    return str(resp)


if __name__ == '__main__':
    app.run()