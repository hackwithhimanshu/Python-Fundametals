def make_album(artist_name, album_title, total_songs=None):
    your_album = {'artist_name' : artist_name, 'album_title' : album_title,}
    if total_songs:
        your_album['total_songs'] = total_songs
    return your_album

while True:
    print("\n(Press 'q' anytime to quit)")
    print("Enter your favorite.")
    n_artist = input("Artist name: ")
    if n_artist == 'q':
        break
    a_artist = input("Artist album: ")
    if a_artist == 'q':
        break
    t_artist = input("Total songs: ")
    if t_artist == 'q':
        break

    if t_artist.isdigit():
        custom_album = make_album(n_artist, a_artist, int(t_artist))
    else:
        custom_album = make_album(n_artist, a_artist,)

    print(custom_album)