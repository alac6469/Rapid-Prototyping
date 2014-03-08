import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from table_def import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Kid Cudi")
new_artist.albums = [Album("Man on the moon", 
                           "rap",
                           "Universal Motown", "CD")]
 
# add more albums
more_albums = [Album("Cabin by the Sea",
                     "rock",
                     "Groovy Tunes", "CD"),
               Album("Hell's Bells", 
                     "Rock",
                     "Majestic", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("Iration"),
    Artist("Eminem"),
    Artist("The Dirty Heads")
    ])
session.commit()
