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
import song_generator.SongClass as sc
import song_generator.string_literals as lit

# main funtion
def main():

  # test output
  print("Hello world ~ from main.py")
  gen.test_output()
  lit.test_output()

  mySong = sc.Song("Metal", 120, "4/4", "E minor", "I V III VII", "Volca Beats", "Gibson SG", "Wampler Tumnus", "Volca FM", "Digitakt")
  
  print(str(mySong))
  return

# control initiating event
if __name__ == '__main__':
  main()

  '''
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