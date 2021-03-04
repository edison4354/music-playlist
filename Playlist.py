from Song import Song

class Playlist:
  def __init__(self):
    self.first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    new_song = Song(title)
    
    if self.first_song == None:
      self.first_song = new_song
      return

    current_song = self.first_song
    while(current_song.next_song):
      current_song = current_song.next_song
    current_song.next_song= new_song



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    counter = 0
    current_song = self.first_song

    while (current_song.get_title().lower() != title.lower()):
      if current_song.get_next_song() == None:
        return -1
      current_song = current_song.get_next_song()
      counter += 1
    return counter 


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    current_song = self.first_song

    if (current_song.get_title() == title.title()):
      self.first_song = current_song.get_next_song()
      print(f'{current_song.get_title()} has been removed!')
      return



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    if self.first_song == None:
      return 0
    else:
      counter = 1
      current_song = self.first_song
      while(current_song.next_song):
        current_song = current_song.next_song
        counter +=1
      return counter


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    current_song = self.first_song
    
    if current_song == None:
      print('This playlist is empty.')
    else:
      for i in range(self.length()):
        print(f'{i+1}. {current_song}')
        current_song = current_song.next_song

  