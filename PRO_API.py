import enum
import datetime
import random
from typing import Union, Tuple, NamedTuple, Iterator, Any, List, Optional, Type

timedelta = datetime.timedelta
date = datetime.date
datetime = datetime.datetime
random = random


class Guild(NamedTuple):
    id: int
    name: str
    rank: int


class Region(enum):
    kanto = 1
    johto = 2
    hoenn = 3
    sinnoh = 4


class PokedexEntry:
    @property
    def region(self)->Region: pass

    @property
    def id(self)->int: pass

    @property
    def caught(self)->bool: pass

    @property
    def evolved(self)->bool: pass


class Pokedex:
    def __iter__(self)->Iterator[PokedexEntry]: pass

    def __contains__(self, item: Union[str, int])->bool: pass

    def __getitem__(self, item: Union[str, int])->PokedexEntry: pass

    def add(self, item: Union[str, int], caught: bool=False, evolved: bool=False): pass


class PokemonSkills:
    def __contains__(self, item: str)->bool: pass


class Pokemon:
    def __init__(self, poke: Union[int, str], lvl: int, shiny: bool=False, form: int=0, ability: int=-1): pass

    @property
    def name(self)->str: pass

    @property
    def dex_id(self)->int: pass

    @property
    def shiny(self)->bool: pass

    @shiny.setter
    def shiny(self, val: bool): pass

    @property
    def pos(self)->int: pass

    @property
    def form(self)->int: pass

    @property
    def level(self)->int: pass

    @property
    def happiness(self)->int: pass

    @happiness.setter
    def happiness(self, val: int): pass

    @property
    def region(self)->Region: pass

    @property
    def iv_atk(self)->int: pass

    @iv_atk.setter
    def iv_atk(self, val: int): pass

    @property
    def iv_def(self)->int: pass

    @iv_def.setter
    def iv_def(self, val: int): pass

    @property
    def iv_spd(self)->int: pass

    @iv_spd.setter
    def iv_spd(self, val: int): pass

    @property
    def iv_spatk(self)->int: pass

    @iv_spatk.setter
    def iv_spatk(self, val: int): pass

    @property
    def iv_spdef(self)->int: pass

    @iv_spdef.setter
    def iv_spdef(self, val: int): pass

    @property
    def iv_hp(self)->int: pass

    @iv_hp.setter
    def iv_hp(self, val: int): pass

    @property
    def total_ivs(self)->int: pass

    @property
    def ev_atk(self)->int: pass

    @ev_atk.setter
    def ev_atk(self, val: int): pass

    @property
    def ev_def(self)->int: pass

    @ev_def.setter
    def ev_def(self, val: int): pass

    @property
    def ev_spd(self)->int: pass

    @ev_spd.setter
    def ev_spd(self, val: int): pass

    @property
    def ev_spatk(self)->int: pass

    @ev_spatk.setter
    def ev_spatk(self, val: int): pass

    @property
    def ev_spdef(self)->int: pass

    @ev_spdef.setter
    def ev_spdef(self, val: int): pass

    @property
    def ev_hp(self)->int: pass

    @ev_hp.setter
    def ev_hp(self, val: int): pass

    @property
    def hidden_power(self)->str: pass

    @property
    def skills(self)->PokemonSkills: pass

    @skills.setter
    def skills(self, val: List[str]): pass

    def can_learn(self, name: str)->bool: pass


class UserPokemon:
    @property
    def id(self)->int: pass

    @property
    def ot(self)->str: pass

    @property
    def name(self)->str: pass

    @property
    def dex_id(self)->int: pass

    @property
    def shiny(self)->bool: pass

    @property
    def pos(self)->int: pass

    @property
    def form(self)->int: pass

    @property
    def level(self)->int: pass

    @property
    def happiness(self)->int: pass

    @property
    def region(self)->Region: pass

    @property
    def iv_atk(self)->int: pass

    @property
    def iv_def(self)->int: pass

    @property
    def iv_spd(self)->int: pass

    @property
    def iv_spatk(self)->int: pass

    @property
    def iv_spdef(self)->int: pass

    @property
    def iv_hp(self)->int: pass

    @property
    def total_ivs(self)->int: pass

    @property
    def ev_atk(self)->int: pass

    @property
    def ev_def(self)->int: pass

    @property
    def ev_spd(self)->int: pass

    @property
    def ev_spatk(self)->int: pass

    @property
    def ev_spdef(self)->int: pass

    @property
    def ev_hp(self)->int: pass

    @property
    def hidden_power(self)->str: pass

    @property
    def skills(self)->PokemonSkills: pass

    def can_learn(self, name: str)->bool: pass

    def learn(self, name: str): pass


class Pokes:
    def __iter__(self)->Iterator[UserPokemon]: pass

    def __getitem__(self, item: int)->UserPokemon: pass

    def __delitem__(self, key: int): pass

    def __contains__(self, item: Union[int, str])->bool: pass

    def add(self, poke: Pokemon): pass

    def heal(self): pass


class NPC:
    @property
    def hide(self)->bool: pass

    @hide.setter
    def hide(self, val: bool): pass

    def hide_for(self, td: timedelta): pass

    team: List[Pokemon]

    @property
    def los(self)->int: pass

    def emote(self, eid: int): pass

    @property
    def last_fight(self)->datetime: pass


class BattleResult(enum):
    pass


class UserVars:
    def __getattr__(self, item: str)->Any: pass

    def __setattr__(self, key: str, value: Any): pass

    def set(self, key: str, value: Any, expire: timedelta): pass


class Items:
    def __iter__(self)->Iterator[Tuple[str, int]]: pass

    def __getitem__(self, item: str)->int: pass

    def __setitem__(self, key: str, value: int): pass

    def __delitem__(self, key: str): pass

    def __contains__(self, item: str)->bool: pass


class User:
    def say(self, msg: str): pass

    def teleport(self, mname: str, x: int, y: int)->bool: pass

    def battle(self, a: Union[Pokemon, NPC],
               noexp: Optional[bool]=False,
               no_teleport: Optional[bool]=False)->BattleResult: pass

    def say_system(self, msg: str): pass

    def play_music(self, mid: int): pass

    def play_sound(self, sid: int): pass

    def play_cry(self, cid: int): pass

    def shop(self, shop_id: int): pass

    def pause(self)->Union[True, None]: pass

    def select(self, question: str, choices: list)->Tuple[int, str]: pass

    def select_pokemon(self, question: str)->UserPokemon: pass

    id: int
    username: str
    position: Tuple[int, int]
    security: Tuple[int, str]
    money: int
    coins: int
    playtime: timedelta
    guild: Guild
    vars: UserVars
    pokes: Pokes
    team: Pokes
    items: Items
    dex: Pokedex
    registration_date: date
    membership: bool
    black_membership: bool


class NPCs:
    @staticmethod
    def __getitem__(item: int)->NPC: pass


npc = NPC()
npcs = NPCs()
user = User()
