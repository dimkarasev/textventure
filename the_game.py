from scripts import beautyfulprint, awesometextart, achievementmanager
from colorama import just_fix_windows_console
import random
name = "random_guy"
def die(cause):
    deadlist = open("The hall of stupidity.txt", "a")
    deadlist.write(name + " died because of " + cause + "\n")
    deadlist.close()
    
    randint = random.randint(1, 10)
    if randint == 1:
        beautyfulprint.exeloong("oh shit ur dead!")
    if randint == 2:
        beautyfulprint.exeloong("damn... ur dead.")
    if randint == 3:
        beautyfulprint.exeloong("u r dead. skill issue.")
    if randint == 4:
        beautyfulprint.exeloong("you are dead. (this is not what the top would be)")
    if randint == 5:
        beautyfulprint.exeloong("lol u died.")
    if randint == 6:
        beautyfulprint.exeloong("you died. (hope you will be ashamed in front of your ancestors)")
    if randint == 7:
        beautyfulprint.exeloong("it's too late for " + name  + ".")
    if randint == 8:
        beautyfulprint.exeloong("nobody will remember " + name + ".")
    if randint == 9:
        beautyfulprint.exeloong("SKILL ISSUE, " + name.upper() + "!")
    if randint == 10:
        beautyfulprint.exeloong("what a waste of time and effort!")
    input("enter to exit\n")
    exit()

just_fix_windows_console()

print (awesometextart.logo)
#beautyfulprint.exe (awesometextart.logo)
beautyfulprint.exe ("\033[32m for correct images set console font to NSim Sun \033[0m")
beautyfulprint.exe ('''
[ply] - play
[esc] - quit
[hlp] - help
[ach] - achievements
''')

inp = "none"
while inp != "ply":
    inp = input("\n>>>").lower()
    if inp == "esc":
        exit()
    if inp == "hlp":
        beautyfulprint.exeloong ('''
When it comes to games, "oh shit!" is one of the trollest. 
In this article, we will look at the basic steps that will help you play a game "oh shit!". We'll start from the beginning...

Step 1: Don't screw up.

Well, that's all you need to know, thanks for your attention, I'm going to have tea for now

.....................................................................

Oh, I forgot to give you the right to act
''')
        achievementmanager.add("get trolled lol")
    if inp == "ach":
        beautyfulprint.exe("your achievements:\n" + achievementmanager.read())
    if inp == "die":
        die("testing")

beautyfulprint.exeloong("In a distant land where magic and miracles are part of everyday life, there lived a brave hero named...")
beautyfulprint.wait()
beautyfulprint.exeloong("Damn it, I forgot the name...")
name = input("enter a name \n>>>")
beautyfulprint.exeloong("Oh, yeah... " + name +".")
beautyfulprint.exeloong("I... I will continue this story of an old senile man...")
beautyfulprint.exe('''
One day, when the sun was already setting, the hero heard a strange noise in the forest. 
Deciding to check what was going on, he set off. But what he found exceeded all his expectations. 
In the depths of the forest, he found an ancient artifact that, as the legends said, had incredible power.
...
Without thinking twice, the hero decided to take it, but he did not know about the consequences...
''')

beautyfulprint.exeloong("you woke up after a long blackout.")
beautyfulprint.wait()
beautyfulprint.exeloong("You have that artifact in your hand... but something is wrong with you...")

beautyfulprint.exe('''
what will you do?
[1] - check your body
[2] - go to the village for advice from a wizard
''')
while inp != "2":
    inp = input("\n>>>")
    if inp == "1":
        beautyfulprint.exe("oh shit, you`re a vampire!")
beautyfulprint.exeloong("You're waiting for the night...")
beautyfulprint.wait()
beautyfulprint.exeloong("You finally got to the house of your old friend, a magician named Prospero")

inp = "reset"

beautyfulprint.exe('''
[1] - knock on the door
[2] - knock out the door
''')
inp = input("\n>>>")
if inp == "2":
    beautyfulprint.exe("\n\033[0;36mGet out, barbarian!\033[0m - magician said \n(you were killed by a fireball)")
    achievementmanager.add("get out, barbarian!")
    die("stupidness + fireball")
beautyfulprint.exeloong('"\033[0;36mGreetings, my old friend,\033[0m" he says. "\033[0;36mWhat brings you here at this time of night?\033[0m"')

beautyfulprint.exeloong('i became a vampire')
beautyfulprint.exeloong("\033[0;36m...\033[0m")
beautyfulprint.exeloong("WHAT!? ARE YOU SEROUS?")
beautyfulprint.wait()
beautyfulprint.exeloong('\n[after a long talk]\n')


beautyfulprint.exeloong("\033[0;36mSo... you need to go yo the mt.Cursed. \nthere you will find the mushroom for the potion of restoration.\033[0m")









































input("adventure ended. any key to close")