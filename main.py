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

  # welcome message
  s_lit.welcome()

  # Case 1
  # testing Song object creation with literal constructors
  s_lit.case_1()
  # make a new Song() object, mySong, and instantiate by hardcoding
  mySong = Song('Metal', 120, '4/4', 'E minor', 'IV', 'Arturia Drumbute', 'Ibanex RG (blue flame)', 'Catalinbread Octopussy', 'Arturia MicroBrute', 'Elektron Digitakt')
  # display the results
  print(str(mySong))

  # Case 2
  # testing methods in Song class
  s_lit.case_2()
  # call the Song.get_random_parameters(mySong) function on the mySong object
  newSong = mySong.get_random_parameters(mySong)
  # display the results
  print(str(newSong))

  # Case 3
  # create a Song object from the gen.generate_parameters() method
  s_lit.case_3() 
  # create a new dictionary
  myDict = {}
  # call the generate_parameters(myDict) function to turn into a randomized Song()
  myDict = gen.generate_parameters(myDict)
  # display the results
  print(myDict)
  # show that dict was converted to Song()
  print(type(myDict))

  return 0
  
# control initiating event
if __name__ == '__main__':
  main()