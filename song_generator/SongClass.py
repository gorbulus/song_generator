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
  
  # string representation of the class
  def __str__(self):
    output = 'Tempo: %s\nGenre: %s' % (self.tempo, self.genre) 
    return output  
