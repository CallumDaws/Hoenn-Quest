#!python

from PRO_API import *

default = Pokemon()
default.ivs = 31, 31, 31, 31, 31, 31
default.evs = 252, 252, 252, 252, 252, 252

Sharpedo = Pokemon("Sharpedo", 80)
Sharpedo.ability = "Rough Skin"
Sharpedo.ivs = default.ivs
Sharpedo.evs = default.evs
Sharpedo.nature = Nature.Jolly
Sharpedo.skills = ("Crunch", "Ice Fang", "Earthquake", "Protect")

Crobat = Pokemon("Crobat", 80)
Crobat.ability = "Inner Focus"
Crobat.nature = Nature.Jolly
Crobat.skills = ("Brave Bird", "Taunt", "Poison Fang", "Super Fang")
Crobat.ivs = default.ivs
Crobat.evs = default.evs

Mightyena = Pokemon("Mightyena", 80)
Mightyena.ability = "Intimidate"
Mightyena.ivs = default.ivs
Mightyena.evs = default.evs
Mightyena.nature = Nature.Jolly
Mightyena.skills = ("Sucker Punch", "Crunch", "Toxic", "Dig")

Muk = Pokemon("Muk", 80)
Muk.ability = "Poison Touch"
Muk.ivs = default.ivs
Muk.evs = default.evs
Muk.nature = Nature.Careful
Muk.skills = ("Toxic", "Poison Jab", "Rest", "Sleep Talk")

Kyogre = Pokemon("Kyogre", 80)
Kyogre.ability = "Drizzle"
Kyogre.ivs = default.ivs
Kyogre.evs = default.evs
Kyogre.nature = Nature.Bold
Kyogre.skills = ("Rest", "Scald", "Roar", "Ice Beam")

MegaSharpedo = Pokemon("MegaSharpedo", 80)
MegaSharpedo.ability = "Strong Jaw"
MegaSharpedo.ivs = default.ivs
MegaSharpedo.evs = default.evs
MegaSharpedo.nature = Nature.Adamant
MegaSharpedo.skills = ("Crunch", "Ice Fang", "Earthquake", "Protect")

npc.team = [Mightyena, Crobat, Sharpedo, Muk, MegaSharpedo, Kyogre]
if user.vars.HoennQuestAquaChoice:
    npc.hide = False
    user.say("You found me, now I'll show you how we battle in Hoenn")
    result = user.battle(npc)

    if result == 1:
        user.say("ugh, I'll be telling my boss about you in Hoenn")
        user.vars.set("CompletedHoennQuestBattleAqua", True)
else:
    npc.hide = True
