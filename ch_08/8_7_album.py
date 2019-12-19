def make_album(artist_name, album_title, num_tracks = ''):
	"""Build dictionary containing information."""
	album = {'artist': artist_name, 'title': album_title}
	if num_tracks:
		album['num_tracks'] = num_tracks
	return album

album = make_album('Queen', 'Queen', 5)
print(album)
album = make_album('Queen', 'Queen')
print(album)