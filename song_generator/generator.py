'''
# generator.py
# William Ponton
# 5.8.21
# Implementation of the Prompt class
# Creates a music prompt
'''

# import packages
import random
import song_generator.song_data as s_data
import song_generator.string_literals as lit
from song_generator.SongClass import Song

# test_output
def test_output():
  test = "Hello world ~ from generator.py"
  return print(test)

# generate song parameters
def generate_parameters(mySong):
  # create a copy of the song_data_dict
  # save the values for each key into the variables used in the Song constructor
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
  # return the object
  return mySong