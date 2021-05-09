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
import song_generator.string_literals as s_lit
import song_generator.song_data as s_data
import song_generator.tests as test

# Song class
from song_generator.SongClass import Song

# main funtion
def main():
  
  # test output from each import file
  test.test_import_files()

  # testing Song object creation with literal constructors
  mySong = Song('Metal', 120, '4/4', 'E minor', 'IV', 'Arturia Drumbute', 'Ibanex RG (blue flame)', 'Catalinbread Octopussy', 'Arturia MicroBrute', 'Elektron Digitakt')
  
  # testing methods in Song class
  print("\n\nUsing hardcoded constructor for the Song class")
  print(str(mySong))

  # TODO - fix get_random_parameters function in SongClass  
  # this should take a Song object and create save random choices back
  mySong = mySong.get_random_parameters(mySong)
  print("Using the get_random_parameters function in the Song class")
  print(str(mySong))

  # create a Song object from the gen.generate_parameters() method
  myDict = {}
  myDict = gen.generate_parameters(myDict)
  print("Using the gen.generate_parameters function in the generate.py file (converts dictionary to Song class)")
  print(myDict)
  print(type(myDict))

  return 0

# control initiating event
if __name__ == '__main__':
  main()