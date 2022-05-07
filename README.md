# E0 AI Chat Bot
Based on the message, it prints the answer with the highest probability using probability from the database.
# Install on linux (Arch,Debian,Termux)

```
git clone https://github.com/TheSadError/E0
cd E0
pip install -r requirements.txt
python3 E0.py # this is for run E0
```

# Explaination
## E0 Probability Algorithm For AI
```python
def probability(um, rw, schat=False, req=[]):
    count = 0
    hw = True
    for w in um:
        if w in rw:
            count += 1
    per = float(count) / float(len(rw))
    for w in req:
        if w not in um:
            hw = False
            break
    if hw or schat:
        return int(per * 100)
    else:
        return 0
```
## E1 Packet
This packet for advice codes and if there any result for message. It will write `I didnt understand sorry... Please reply.` or something.
```py
import random
advicelist = ["You can Improve my code. Its so simple...","You can play a game...","You may learn new programming language...","You can star my github repo."]
gamelist = ["Fortnite","Valorant","Far Cry 5","GTA V","Tomb Rider","Control","Far Cry 6","Snake Game","Football","Basketball"]
R_EATING = "Ummm... You may eat pasta. But my favorite foods are : CPU and RAM. They are awsome. You must try!"
R_ADVICE = random.choice(advicelist)
R_GAME = random.choice(gamelist)

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "I didnt understand sorry... Please reply.",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(5)]
    return response
```

## Data base :

Explaination : if user writed : hi after that bot will say `Hello!` Because `hi` is in 
`['hello', 'hi', 'hey', 'sup', 'heyo','hola','salam','merhaba']` list. It works like this

```py
    dns('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hola','salam','merhaba','selam','السلام عليكم','عليكم','السلام'], schat=True)
    dns('See you!', ['bye', 'goodbye'], schat=True)
    dns('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], req=['how'])
    dns('You\'re welcome!', ['thank', 'thanks'], schat=True)
    dns('Thank you!', ['i', 'love', 'code', 'palace'], req=['code', 'palace'])
    dns('Sure!',['want', 'to', 'be', 'my','friend'],schat=True)
    dns('My name is E0. And I created by Err0r. Err0r is python,cpp and ruby developer and competitive programmer.',['name', 'who', 'who are you', 'who are you', 'who are you?','are you?','are you'],schat=True)
    dns('I know python,c and java script languages.',['want', 'ruby', 'cpp', 'python','which language','do you know ?','know?','know','programming language'],schat=True)
    dns('',["play?","game?",'what we can do?','what we can do','what we can','what we can?','what can you do?','what can you do','what can you?',"what can you"],schat=True)
    dns('Yess...',['are you okey?','you okey?','you ok?','you okey'],schat=True)
    dns('I am feeling bad.','I am sad. Hope you are better.',['feel?','how are you feel?','feelings?'],req='feel')
    dns('Ah. I understand. I live in Github Repo. Write "github" for see it. My Discord :err0r#4018 ',['social','social media','discord','media'],schat=True)
    dns('Some Music Advices : Old Town Road , Montero , SR - Welcome To Brixton , 6 For 6',['music','musik','muzik'],schat=True)
    
    dns('WOW', ['wow', 'awsome', 'good', 'good' , 'col' ,'cool'], schat=True)
    dns(E0.R_ADVICE, ['give', 'advice'], req=['advice'])
    dns(E0.R_EATING, ['what', 'you', 'eat'], req=['you', 'eat'])
    dns(E0.R_GAME, ['what', 'game', 'you','play'], req=['game', 'play'])
    

    # People
    dns("""Elon Musk, aka Elon Reeve Musk, is an engineer, industrial designer, tech entrepreneur, 
and philanthropist. Apart from his birthplace of South Africa, he is a Canadian and US citizen 
and lives in the USA, where he immigrated at the age of 20.
    """,['elon musk','musk','elon'],schat=True)
    
    dns("""William Henry Bill Gates III or better known as Bill Gates, American entrepreneur,
software developer, author, investor and businessman
    """,['bill gates','bill','gates'],schat=True)

    dns("""Jeffrey Preston Bezos is an American internet entrepreneur, industrialist, media owner, and investor,
best known as the founder, CEO, and chairman of the worldwide technology company Amazon. Before 2017, 
Bezos, who was one of the first hundred billionaires on the Forbes wealth index list, became the richest 
man in the world after 2017.
    """,['jeff','bezos','jeff bezos'],schat=True)


    dns("""John Christopher Depp II is an American actor, producer and musician. Nominated for ten Golden Globe Awards, 
he was nominated for an Academy Award for Best Actor for his role as 
the Demon Barber in Sweeney Todd: The Demonic Barber of Fleet Street.
    """,['johnny','Johnny','depp','Depp','Johnny Depp','johnny depp'],schat=True)
```
## Info Function
```py

def info():
    print(Fore.BLUE+"""
    
            -_________________-_________________-
            |                                   |
            |  |-_-| Welcome to E0 Bot!  |-_-|  |
            -_________________-_________________- 

            Hi ? Are you there ? Ok... I will say 
            story. I created by Error. His other 
            name is TheSadError. He created my on 
            5 May 2022 . He used python3.9 . And he 
            added E1 packet for unknown things. It 
            working awsomely. And I am open source. 
            This means you can see my code and can edit
            them for yourself. For this Error shared 
            my code in his own github repo. Let me explain
            E0 logic. Logic : 
            User input a sentence or words probability
            function searching for probability. Which words 
            probability suitability is bigger in database
            E0 prints answear of the word base. Its simple AI. 

    """)

```

## Some commands
```
[1] 'clear' : For clear chat
[2] 'exit'  : Break code and exit from E0
[3] 'menu'  : To print menu (other functions Of bot)
[4] 'help'  : To list commands
[5] 'dir'   : To dir files
[6] 'ls'    : To list files in directory
[7] 'face'  : To run face dedection
[8] 'info'  : To see E0's info
```


**Copright To Error**
