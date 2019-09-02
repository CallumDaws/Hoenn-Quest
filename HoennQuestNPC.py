#!python

from PRO_API import *

if user.vars.KantoChamp and user.vars.JohtoChamp:
    if user.vars.HoennQuestMagmaChoice or user.vars.HoennQuestAquaChoice:
        user.say("Please help, he's still out there somewhere!")
    else:
        user.say("Please help me, my pokemon has been stolen and i followed the thief here from Hoenn")
        choice = user.select("I think he was wearing a uniform, the colour was" , ["Red (Hard)", "Blue (Normal)", "Cancel"])
        if choice[0] == 0:
            user.vars.set(HoennQuestMagmaChoice, True)
        if choice[0] == 1:
            user.vars.set(HoennQuestAquaChoice, True)
        else:
            user.say("Ok, please help me when you can remember")



if user.vars.CompletedHoennQuestBattleMagma:
    user.say("Thank you very much for helping me, I think Numel would be safer with you")
    Numel = Pokemon("Numel", 5, shiny=True)
if user.vars.CompletedHoennQuestBattleAqua:
    user.say("Thank you very much for helping me, I think Poochyena would be safer with you")
    Poochyena = Pokemon("Poochyena", 5, shiny=True)

