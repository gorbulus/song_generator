'''
# Music Prompt Generator
# William Ponton
# 5.8.21
# A program that generates random constraints for creating a piece of music.  
# The constraints will be in place to force the creator to avoid the exquisite misery of choice.
# Sometimes the best music is the most inspired by chance and dancing with the moment.
'''

# impoart packages
import song_generator.generator as gen
import song_generator.string_literals as lit
import song_generator.song_data as s_data

# Song class
from song_generator.SongClass import Song

# main funtion
def main():

  # test output
  print("Hello world ~ from main.py")
  gen.test_output()
  lit.test_output()
  s_data.test_output()
  
  # create a copy of the song_data_dict
  # save the values for each key into the variables used in the Song constructor
  dict_copy = s_data.song_data_dict
  genres = dict_copy['genres']
  tempos = dict_copy['tempos']
  time_signatures = dict_copy['time_signatures']
  key_signatures = dict_copy['key_signatures']
  chord_progressions = dict_copy['chord_progressions']
  drum_machines = dict_copy['drum_machines']
  instruments = dict_copy['instruments']
  pedals = dict_copy['pedals']
  synths = dict_copy['synths']
  samplers = dict_copy['samplers']

  mySong = dict_copy
  newSong = Song(genres, tempos, time_signatures, key_signatures, chord_progressions, drum_machines, instruments, pedals, synths, samplers)

  print(str(newSong))

  mySong = Song('Metal', 120, '4/4', 'E minor', 'IV', 'Arturia Drumbute', 'Ibanex RG (blue flame)', 'Catalinbread Octopussy', 'Arturia MicroBrute', 'Elektron Digitakt')

  print(str(mySong))
  
  
  
  return

# control initiating event
if __name__ == '__main__':
  main()