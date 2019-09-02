#!python

from PRO_API import *

default.ivs = 31, 31, 31, 31, 31, 31
default.evs = 252, 252, 252, 252, 252, 252

Camerupt = Pokemon("Camerupt", 100)
Camerupt.ability = "Magma Armor"
Camerupt.ivs = default.ivs
Camerupt.evs = default.evs
Camerupt.nature = Nature.Modest
Camerupt.skills = ("Fire Blast", "Earth Power", "Rock Slide", "Flamethrower")

Crobat = Pokemon("Crobat", 100)
Crobat.ability = "Inner Focus"
Crobat.nature = Nature.Jolly
Crobat.skills = ("Brave Bird", "Taunt", "Poison Fang", "Super Fang")
Crobat.ivs = default.ivs
Crobat.evs = default.evs

Mightyena = Pokemon("Mightyena", 100)
Mightyena.ability = "Intimidate"
Mightyena.ivs = default.ivs
Mightyena.evs = default.evs
Mightyena.nature = Nature.Jolly
Mightyena.skills = ("Sucker Punch", "Crunch", "Toxic", "Dig")

Weezing = Pokemon("Weezing", 100)
Weezing.ability = "Levitate"
Weezing.ivs = default.ivs
Weezing.evs = default.evs
Weezing.nature = Nature.Bold
Weezing.skills = ("Toxic", "Sludge Bomb", "Taunt", "Explosion")

Groudon = Pokemon("Groudon", 100)
Groudon.ability = "Drought"
Groudon.ivs = default.ivs
Groudon.evs = default.evs
Groudon.nature = Nature.Adamant
Groudon.skills = ("Earthquake", "Dragon Claw", "Stone Edge", "Overheat")

MegaCamerupt = Pokmeon("MegaCamerupt", 100)
MegaCamerupt.ability = "Sheer Force"
MegaCamerupt.ivs = default.ivs
MegaCamerupt.evs = default.evs
MegaCamerupt.nature = Nature.Modest
MegaCamerupt.skills = ("Eruption", "Earth Power", "Rock Slide", "Flamethrower")

npc.team = [Mightyena, Crobat, Camerupt, Weezing, MegaCamerupt, Groudon]
if user.vars.HoennQuestMagmaChoice:
    npc.hide = False
    user.say("You found me, now I'll show you how we battle in Hoenn")
    result = user.battle(npc)

    if result == 1:
        user.say("ugh, I'll be telling my boss about you in Hoenn")
        user.vars.set("CompletedHoennQuestBattleMagma", True)
else:
    npc.hide = True

