client_access_token = 'kRNWH_GrdQsfGPOIOF4wI-hUkfhLdFry-QaNw6c0D0QIFaSf1p61Qb-vyuDlUrlS'

import lyricsgenius as lg  # https://github.com/johnwmillr/LyricsGenius


def get_lyrics(arr, k):  # Write lyrics of k songs by each artist in arr

    genius = lg.Genius(client_access_token,  # Client access token from Genius Client API page
                       skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                       remove_section_headers=True)

    with open("lyrics.txt", "w") as some_file:  # File to write lyrics to

        c = 0  # Counter
        for name in arr:
            try:
                songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
                s = [song.lyrics for song in songs]
                some_file.write("\n \n   <|endoftext|>   \n \n".join(s))  # Deliminator
                c += 1
                print(f"Songs grabbed:{len(s)}")
            except Exception as e:
                print(f"some exception at {name}: {c}\nMessage: {e}")


get_lyrics(['Logic', 'Rihanna', 'Frank Sinatra'], 3)