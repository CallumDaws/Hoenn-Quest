#!python

from PRO_API import *


requestedPokemon = ["Turtwig", "Grotle", "Torterra", "Chimchar", "Monferno",
                    "Infernape", "Piplup", "Prinplup", "Empoleon", "Starly",
                    "Staravia", "Staraptor", "Kricketot", "Kricketune",
                    "Shinx", "Luxio", "Luxray", "Burmy", "Wormadam", "Mothim",
                    "Combee", "Vespiquen", "Pachirisu", "Buizel", "Floatzel",
                    "Cherubi", "Cherrim", "Shellos", "Gastrodon", "Glameow",
                    "Purugly", "Chingling", "Stunky", "Skunktank", "Bronzor",
                    "Chatot", "Croagunk", "Toxicroak", "Finneon", "Lumineon",
                    "Mantyke", "Snover", "Abomasnow"]
randomRewards = ["Ultra Ball", "Leppa Berry", "Revival Herb", "Rare Candy",
                 "Master Ball"]
shinyRewards = ["Sentret", "Pidgey", "Spinarak", "Magikarp", "Krabby",
                "Wooper"]

shinyRew = random.choice([shinyRewards])
reward = random.choice([randomRewards])
poke = random.choice([requestedPokemon])
complete = "Thanks for helping!"


def newsquest():
    count = user.vars.counter
    if not user.vars.NewsNPC:
        today = datetime.now()
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow = datetime.combine(tomorrow, datetime.min.time())
        HuntTime = tomorrow - today
        if not user.vars.counter:
            user.vars.set("HuntTime", True, HuntTime)
            user.say("""Hello, this is your first visit, I'm looking for a
                     pokemon for the news""")
            user.say("I'm looking for a {0}. you have {1} to make it in today's news"
                     .format(poke, user.expire.HuntTime))
        elif user.vars.HuntTime:
            choice = user.select("You have {0} hours left to find {1}, submit?"
                                 .format(user.expire.HuntTime, poke)["Yes", "No"])
            if choice[0] == 1:
                user.say("Ok! Please return with the Pokemon later")
                return
        else:
            user.say("""Hello {} It's a new day for the daily news!
                     Let's get down to business""".format(user.username))
            user.vars.set("HuntTime", True, HuntTime)

        p = user.select_pokemon("""I'm looking for a {0}, you have {1} hours left
                                to submit""".format(poke, user.expire.HuntTime))
        if p.name != poke:
            user.say("Sorry that is not a {} please return with one"
                     .format(poke))
            return
        elif p.ot != user.username:
            user.say("Sorry that is not your {} please catch your own"
                     .format(poke))
            return
        else:
            user.vars.set("HuntTime", False)
            user.say("This is your {} day of completion here's your reward"
                     .format(user.vars.counter))
            user.vars.set("NewsNPC", True, HuntTime)
            if user.vars.counter > 0:
                days = user.vars.counter % 7
        if user.vars.counter != 0 and user.vars.counter % 100 == 0:
            user.say("Wow you've helped me a lot, here you go")
            arceus = Pokemon("Arceus", 50, shiny=True)
            user.pokes.add(arceus)
        elif user.vars.counter != 0 and user.vars.counter % 25 == 0:
            user.say("""This is your {}th day of helping, you deserve a special
                     reward!""".format(user.vars.counter))
            shinymon = Pokemon(shinyRew, 5, shiny=True)
            user.pokes.add(shinymon)
            user.say("You recieved a shiny {}".format(shinymon.name))
            user.say(complete)
            count = count+1
            user.vars.set("counter", count, HuntTime + timedelta(days=1))
        elif days != 0 or count is None:
            user.items[reward] = user.items[reward] + days
            user.say("You recieved {0} {1}".format(days, reward))
            user.say(complete)
            if count is None:
                count = 0
            count = count + 1
            user.vars.set("counter", count, HuntTime + timedelta(days=1))
        elif days == 0:
            rerollTicket = random.randint(0, 100)
            user.say(complete)
            if rerollTicket < 90:
                user.items[reward] = user.items[reward] + days
                user.say("You recieved {0} {1}".format(days, reward))
                count = count + 1
                user.vars.set("counter", count, HuntTime + timedelta(days=1))
            else:
                user.items["Reroll Ticket"] = user.items["Reroll Ticket"] + 1
                user.say("You recieved a Reroll Ticket")
                count = count + 1
                user.vars.set("counter", count, HuntTime + timedelta(days=1))

    else:
        user.say("Sorry you've received a reward today come back in {}"
                 .format(timedelta(user.expire.HuntTime)))
