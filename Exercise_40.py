#Exercise 40: Modules, Classes, and Objects

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print "I am CLassy Apples!"

thing = MyStuff()
thing.apple()
print thing.tangerine

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you", "happy birthday to you, happy birthday dear..."])
bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
