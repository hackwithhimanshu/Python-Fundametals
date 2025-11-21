def make_album(artist_name, album_title, total_songs=None):
    your_album = {'artist_name' : artist_name, 'album_title' : album_title,}
    if total_songs:
        your_album['total_songs'] = total_songs
    print(your_album)
    return your_album

make_album('king', 'carnival')
make_album('neffex', 'destiny')
make_album('arjit singh', 'sitara', total_songs=8)