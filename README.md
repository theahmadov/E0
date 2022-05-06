# E0 AI Chat Bot
Based on the message, it prints the answer with the highest probability using probability from the database.

# E0 Probability Algorithm For AI
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
# E1 Packet
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

# Data base :

Explaination : if user writed : hi after that bot will say `Hello!` Because `hi` is in 
`['hello', 'hi', 'hey', 'sup', 'heyo','hola','salam','merhaba']` list. It works like this

```py
    dns('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo','hola','salam','merhaba'], schat=True)
    dns('See you!', ['bye', 'goodbye'], schat=True)
    dns('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], req=['how'])
    dns('You\'re welcome!', ['thank', 'thanks'], schat=True)
    dns('Thank you!', ['i', 'love', 'code', 'palace'], req=['code', 'palace'])
    dns('Sure!',['want', 'to', 'be', 'my','friend'],schat=True)
    dns('My name is E0. And I created by Err0r. Err0r is python,cpp and ruby developer and competitive programmer.',['name', 'who', 'who are you', 'who are you', 'who are you?','are you?','are you'],schat=True)
    dns('I know python,c and java script languages.',['want', 'ruby', 'cpp', 'python','which language','do you know ?','know?','know','programming language'],schat=True)
    dns(E0.R_ADVICE, ['give', 'advice'], req=['advice'])
    dns(E0.R_EATING, ['what', 'you', 'eat'], req=['you', 'eat'])
    dns(E0.R_GAME, ['what', 'game', 'you','play'], req=['game', 'play'])
```

## Some commands
```
[1] 'clear' : for clear chat
[2] 'exit'  : break code and exit from E0
```
Copright To Error
