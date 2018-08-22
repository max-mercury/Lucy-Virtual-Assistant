import random
from SenseCells.tts import tts

def who_are_you():
    messages = ['I am, your personal assistant.',
    'Max, did I not tell you before?',
    'You ask that so many times! I am Lucy.']
    tts(random.choice(messages))

def how_am_i():
    replies = ['You are goddamn handsome!', 'My knees go weak when I see you.',
    'You are sexy!', 'You look like the kindest person that I have met.']
    tts(random.choice(replies))

def tell_joke():
    jokes=['What happens to a frogs car when it breaks down? It gets toad away.',
    'Why was six scared of seven? Because seven ate nine.', 'No, I always forget the punch line.']
    tts(random.choice(jokes))

def who_am_i():
    tts('You are ,brilliant person. I like you!')

def where_born():
    tts('I was created by a speedster.')

def how_are_you():
    tts('I am fine, thank you.')

def undefined():
    tts('I dont know what that means!')
