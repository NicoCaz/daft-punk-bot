import tweepy
import random
import time
import os
from os import environ
consumer_key=environ["consumer_key"]  
consumer_secret=environ["consumer_secret"]  
key=environ["key"] 
secret=environ["secret"] 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


Letras={
    "1":("Something About Us",
        "It might not be the right time \nI might not be the right one",
        "But there's something about us I want to say \nCause there's something between us anyway",
        "I might not be the right one \nIt might not be the right time",
        "But there's something about us I've got to do \nSome kind of secret I will share with you",
        "I need you more than anything in my life \nI want you more than anything in my life \nI'll miss you more than anyone in my life \nI love you more than anyone in my life",
        ),
    "2":("One more Time",
        "One more time x3",
        "We're gonna celebrate \nOh yeah, all right \nDon't stop the dancing",
        "You know I'm just feeling",
        "Don't wait to late \nUhmmm, you know \nYou don't stop \nYou can't stop \nWe're gonna celebrate",
        "Celebrate and dance so free \nMusic's got me feeling so free \nCelebrate and dance so free",
        ),
    "3":("Digital Love",
        "Last night I had a dream about you \nIn this dream I'm dancing right beside you \nAnd it looked like everyone was having fun \nA kind of feeling I've waited so long",
        "Don't stop come a little closer \nAs we jam the rythm gets stronger",
        "There's nothing wrong with just a little bit of fun \nWe were dancing all night long",
        "The time is right to put my arms around you \nYou're feeling mine \nYou wrap your arms around too \nBut suddenly I feel the shining sun \nBefore I knew it this dream was all gone",
        "Ooh I don't know what to do \nAbout this dream and you \nI wish this dream comes true",
        "Why don't you play the game?",
        ),
    "4":("Harder, Better, Faster, Stronger",
        "Work it, make it, do it, makes us \nHarder, better, faster, stronger \nMore than, hour, our, never \nEver, after, work is, over",
        "Work it, make it, do it, makes us \nHarder, better, faster, stronger \nWork it harder, make it better \nDo it faster, makes us stronger \nMore than ever, hour after, our \nWork is never over",
        ),
    "5":("Around the world",
        "Around the world, around the world x39",
    ),
    "6":("Give Life Back To Music",
        "Let the music in tonight, just turn on the music",
        "Let the music of your life; give life back to music",
        "Life back to music \nGive life back to music",
        ),
    "7":("The Game Of Love",    
        "There is a game of love \nThis is a game of love \nAnd it was you \nThe one that would be breaking my heart \nWhen you decided to walk away",
        "When I wanted you to stay \n(Ooooooo....) \nAnd it was you \nI just wanted you to stay \nMe, I just wanted you to stay",
        ),
    "8":("Giorgio By Moroder",
        "They already had discotheques",
        "And then have a sound of the future",
        "And I said,\n'Wait a second ,I know the synthesizer',\nwhy don't I use the synthesizer",
        "Which is the sound of the future?",
        "My name is Giovanni Giorgio, but everybody calls me Giorgio",
        "You can do whatever you want \nSo nobody told me what to do \nAnd there was no preconception of what to do",
        ),
    "9":("Within",
        "There are so many things that I don't understand \nThere's a world within me that I cannot explain",
        "I've been for some time \nLooking for someone \nI need to know now \nPlease, tell me who I am?",
        ),
    "10":("Instant Crush",
        "I didn't want to be the one to forget \nI thought of everything I'd never regret \nA little time with you is all that I get",
        "That's all we need, because it's all we can take",
        "One thing I never see the same when your round",
        "But no one gives us any time anymore",
        "You made an offer for it, then you ran off",
        "I got this picture of us kids in my head",
        "And all I hear is the last thing that you said",
        "I listened to your problems, now listen to mine \nI didn't want to anymore, oh oh oh",
        "And we will never be alone again \nCause it doesn't happen every day \nKinda counted on you being a friend \nCan I give it up or give it away?",
        "Now I thought about what I wanna say \nBut I never really know where to go \nSo I chained myself to a friend \nSome more again",
        "It didn't matter what they wanted to see \nHe thought he saw someone that looked just like me",
        "The summer memory that just never dies \nWe worked too long and hard to give it no time",
        "He sees right through me, it's so easy with lies",
        "Cracks in the road that I would try and disguise",
        "One thousand lonely stars hiding in the cold \nTake it, I don't wanna sing anymore",
        "I don't understand, don't get upset, I'm not with you",
        "We're swimming around, it's all I do when I'm with you",
        ),
    "11":("Lose Yourself To Dance",
        "I know you don't get chance to take a break this often",
        "I know your life is speeding and it isn't stopping",
        "You take my shirt and just go ahead and wipe up all the \nSweat, sweat, sweat",
        "Lose yourself to dance \nLose yourself to dance \nLose yourself to dance",
    ),
    "12":("Touch",
        "Touch, I remember touch",
        "I need something more in my mind",
        "Pictures came with touch",   
        "A painter in my mind \nTell me what you see",
        "A half forgotten song",

        "Where do I belong",
        "Tell me what you see \nI need something more",
        "Kiss suddenly alive \nHappiness arrive \nHungry like a storm \nHow do I begin",
        "Hold on, hold on \nIf love is the answer you're home",
        "Touch sweet touch \nYou give me too much to feel",
        "You’ve almost convinced me I’m real \nI need something more \nI need something more",
        
        ),
    "13":("Get Lucky",
       "Like the legend of the Phoenix \nAll ends with beginnings",
        "We've come too far \nTo give up who we are \nSo let's raise the bar \nAnd our cups to the stars",
       "She's up all night to the Sun, I'm up all night to get some \nShe's up all night for good fun, I'm up all night to get lucky",   
       "We're up all night to the Sun, we're up all night to get some",
       "We're up all night for good fun, we're up all night to get lucky",
       "We're up all night to get lucky, we're up all night to get lucky",
       "The present has no ribbon \nYour gift keeps on giving \nWhat is this I'm feeling? \nIf you wanna leave, I'm with it",
       "We're up all night to get back together",
       ),
    "14":("Beyond",       
        "Dream, beyond dreams \nBeyond life you will find your song",
        "You are the night, you are the ocean \nYou are the light behind the cloud \nYou are the end and the beginning",
        "A world with time is not allowed \nThere's no such thing as competition \nTo find a way we lose control",
        "Remember love, the holy mission \nThis is the journey of the soul",
        "The perfect song is framed with silence",
        "Your home's a promise long forgotten \nIt is the birthplace of your dreams",

        ),
    "15":("Fragments Of Time",
        "Driving this road down to paradise",
        "Our only plan is to improvise",
        "That I don't ever want it to end",
        "If I had my way, I would never leave",
        "Keep building these random memories",
        "But since I can't stay",
        "I'll just keep playing back \nThese fragments of time \nEverywhere I go, these moments will shine",
        "Familiar faces I've never seen \nLiving the gold and the silver dream \nMaking me feel like I'm 17",
    ),
    "16":("Doin' It Right",
        "Doin' it right",
        "Everybody will be dancing \nAnd we'll be feeling it right",
        "If you do it right \nLet it go all night \nShadows on you break \nOut into the light",
        "If you lose your way tonight \nThat's how you know the magic's right",
    ),
    "17":("meme",
        "Veridis Quo \ntururu tururu",
        "Motherboard noises*",
    ),
}




class Twit:
    def __init__(self):
        self.anterior=-1
        self.cancion=-1
    def twit(self):
        while self.anterior == self.cancion:
            self.cancion=random.randint(1,len(Letras))
        self.anterior=self.cancion
        array= Letras[str(self.cancion)]
        frase=random.randint(1,len(Letras[str(self.cancion)])-1)        
        return array[frase]
   


lyrics = Twit()

while  True:
    api.update_status(lyrics.twit())
    time.sleep(1800)
