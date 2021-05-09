'''
# song_data.py
# William Ponton
# 5.8.21
# Dictionaries and other data structures for use in the Song class
song_data dictionary:
Keys:
- genre
- tempo
- time_signature
- key_signature
- chord_progression
- drum_machines
- instruments
- pedals
- synths
- samplers
'''

# import packages
import random
from collections import defaultdict

random.seed()

''''TODO - make the data into a JSON file and parse the JSON object into a Python Dictionary
import json
with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)

# elsewhere...to load the file

with open('my_dict.json') as f:
    my_dict = json.load(f)
'''
# test_output
def test_output():
  test = "Hello world ~ from song_data.py"
  return print(test)

# collections
# lists
genres = ['Jazz','Rock','Metal','Electronic','SynthPop','Future Funk','Electro-Boogie','Vaporwave','Lo-Fi','Chill','Ambient','Psychedelic','Blues-Rock', 'Afro-Beat', 'Latin-Jazz']
time_signatures = ['4/4','3/4','2/4','7/8','6/8','5/8']
key_signatures = ['A major','B major','C major','D major','E major','F major','G major','a minor','b minor','c minor','d minor','e minor','f minor','g minor']
drum_machines = ['Volca Beats','PO-12','Arturia Drumbrute','Volca Sample','Beat Thang','Elektron Digitakt','Elektron Model:Samples', 'DAW']
instruments = ['Gibson SG','Fender Telecaster (modified)','Ibanez RG (Blue Flame)','Ibanez RG (Burst)','Washburn Acoustic','Michael Kelly Mandolin']
pedals = ['Catalinbread Octopussy','Catalinbread Topanga','Keeley Neutrino','Keeley Sfocato','Wampler Ego Compressor','Walrus Audio Slo','Benson Preamp','Keeley Caverns','JHS Unicorn','JHS Kodiak','Electro Harmonix Small Stone','Line 6 Delay','Keeley 4-Knob Compressor']
synths = ['Arturia MicroBrute','Korg Volca Keys','Korg Volca FM','Elektron DigiTone','Electron Heat','Elektron Model:Cycles','Korg Volca Bass','Korg Monotron','Korg Monotron Duo','Korg Monotron Delay','Teenage Engineering PO-14 Sub','Teenage Engineering PO-12 Drum','Teenage Engineering PO-16 Factory','Teenage Engineering PO-24 Office','Teenage Engineering PO-20 Arcade','Teenage Engineering PO-28 Robot', 'DAW']
samplers = ['Korg Volca Sample','Elektron DigiTakt','Eketron Model:Sample','Beat Thang','DAW']
#TODO - make a list of lists lie chord_progressions = [[1 [I, V, VI, VII]], [2, [V, VII, ii, IV]]
# list of lists 
chord_progressions = ['I','IV','III','V','VII','VI']

# song_data_dict
# a dictionary that holds all the song parameter data
song_data_dict = {
  'genres' : genres,
  'tempos' : random.randrange(75,150),
  'time_signatures' : time_signatures,
  'key_signatures' : key_signatures,
  'chord_progressions' : chord_progressions,
  'drum_machines' : drum_machines,
  'instruments' : instruments,
  'pedals' : pedals,
  'synths' : synths,
  'samplers' : samplers,
}
