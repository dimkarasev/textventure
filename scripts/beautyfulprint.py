import time

def exe(word):
    for char in word:
        print(char.replace("⡀", " "), end='', flush=True)
        time.sleep(0.005)
    print ()
    
def exeloong(word):
    for char in word:
        print(char.replace("⡀", " "), end='', flush=True)
        time.sleep(0.03)
    print ()
    
def wait():
    for char in '...':
        print(char.replace("⡀", " "), end='', flush=True)
        time.sleep(1.5)
    print ()