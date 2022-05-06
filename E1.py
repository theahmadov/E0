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
