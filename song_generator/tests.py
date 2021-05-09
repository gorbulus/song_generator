'''
# tests.py
# William Ponton
# 5.9.21
# Tests for the song_generator project
'''
# import pacagkes
import song_generator.generator as gen
import song_generator.song_data as s_data
import song_generator.string_literals as s_lit
from song_generator.SongClass import Song # Song class

# test output from each import file
def test_import_files():
  print("\n...testing...")
  print("Hello world ~ from main.py")
  gen.test_output()
  s_data.test_output()
  Song.test_output()
  s_lit.test_output()
  print("Hello world ~ from tests.py")
  return print("...testing completed...")