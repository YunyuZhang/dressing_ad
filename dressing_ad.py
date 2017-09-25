from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import random

app= Flask(__name__)
ask= Ask(app,"/dressing_advisor")

shirts=["AF red shirt","Hollister pink shirts","A E white shirt","Old Navy red shirt","AF blue shirt", "AF white shirt", "H and M forest hoodie"]
pants= ["AF jean", "Black jogger", "A E black pants"]
jackets=["Zara leather jacket", "AF lightweight jacket","AF Sweater","Old Navy blue sweater"]
shoes= ["Nike flower shoes","Convers","boat shoes", "Nike running shoes"]


def get_outfits():
        suggested_outfits=[]
        suggested_shirts= random.choice(shirts)
        suggested_outfits.append(suggested_shirts)

        suggested_jackets= random.choice(jackets)
        suggested_outfits.append(suggested_jackets)
        
        suggested_pants= random.choice(pants)
        suggested_outfits.append(suggested_pants)
        

        
        suggested_shoes= random.choice(shoes)
        suggested_outfits.append(suggested_shoes)

        

        return suggested_outfits;

@app.route("/")
def hello():
    return "Hello World!"





@ask.launch
def start_skill():
	welcome= 'Hello Yunyu, welcome to dressing advisor. Do you need my advice?'
	return question(welcome)

@ask.intent("YesIntent")
def speak():
        outfits=get_outfits();
        outfits_msg='The suggested outfits are {}'.format(outfits)
        return statement(outfits_msg). simple_card(outfits_msg)

@ask.intent("NoIntent")
def no_intent():
        bye="Do not waste your time on deciding what to wear"
        return statement(bye)

if __name__== '__main__':
        app.run(debug=True)



