'''
# Song.py
# William Ponton
# 5.8.21
# Specification of the Prompt class
# The Song class attributes:

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
import song_generator.generator as gen
import song_generator.song_data as s_data

# set the seed for random
random.seed()

# Song class
class Song():
  # Song class constructor
  def __init__(self, genre, tempo, time_signature, key_signature, chord_progression, drum_machines, instruments, pedals, synths, samplers):
    self.genre = genre
    self.tempo = tempo
    self.time_signature = time_signature
    self.key_signature = key_signature
    self.chord_progression = chord_progression
    self.drum_machines = drum_machines
    self.instruments = instruments
    self.pedals = pedals
    self.synths = synths
    self.samplers = samplers
  
  # test_output
  def test_output():
    test = "Hello world ~ from Song class.py"
    return print(test)

  # string representation of the class
  def __str__(self):
    output = 'Genre: %s\nTempo: %s\nTime Signature: %s\nKey Signature: %s\nChord Progression: %s\nDrum Machines: %s\nInstruments: %s\nPedals: %s\nSynths: %s\nSamplers: %s\n' % (self.genre, self.tempo, self.time_signature, self.key_signature, self.chord_progression, self.drum_machines, self.instruments, self.pedals, self.synths, self.samplers) 
    return output
  
  # randomized song parameters
  @staticmethod
  def get_random_parameters(self, **kwargs):
    dict_copy = s_data.song_data_dict
    # set values for Song class constructor
    genres = random.choice(dict_copy['genres'])
    tempos = random.randrange(75, 150)
    time_signatures = random.choice(dict_copy['time_signatures'])
    key_signatures = random.choice(dict_copy['key_signatures'])
    chord_progressions = random.choice(dict_copy['chord_progressions'])
    drum_machines = random.choice(dict_copy['drum_machines'])
    instruments = random.choice(dict_copy['instruments'])
    pedals = random.choice(dict_copy['pedals'])
    synths = random.choice(dict_copy['synths'])
    samplers = random.choice(dict_copy['samplers'])
    # instantiate a new Song object using the constructor variables
    mySong = Song(genres, tempos, time_signatures, key_signatures, chord_progressions, drum_machines, instruments, pedals, synths, samplers)
    return mySong
