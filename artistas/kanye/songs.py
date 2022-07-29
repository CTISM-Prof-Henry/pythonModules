"""
Este script usa a biblioteca externa https://github.com/johnwmillr/LyricsGenius

Veja a seção Instalação do arquivo README para ver como instalá-la.
"""

import lyricsgenius as lg
import json


def get_lyrics(artist, n_songs):
    client_access_token = 'kRNWH_GrdQsfGPOIOF4wI-hUkfhLdFry-QaNw6c0D0QIFaSf1p61Qb-vyuDlUrlS'

    genius = lg.Genius(
        client_access_token,  # token de acesso do Genius Client API
        skip_non_songs=True,
        excluded_terms=["(Remix)", "(Live)"],
        remove_section_headers=True
    )

    with open("lyrics.json", "w") as some_file:  # File to write lyrics to
        print(f'songs.py: Começando o processo de salvar músicas do {artist}...')
        some_dict = dict()

        try:
            songs = (genius.search_artist(artist, max_songs=n_songs, sort='popularity')).songs
            some_dict[artist] = [song.lyrics for song in songs]

            print(f"songs.py: Salvei {len(some_dict[artist])} músicas do {artist} no arquivo.")
        except Exception as e:
            print(f"songs.py: Uma exceção ocorreu:\n{e}")

        json.dump(some_dict, some_file, indent=2)  # escreve dicionário no arquivo json


# esse código só será executado se o usuário explicitamente executar o arquivo songs.py
if __name__ == '__main__':
    get_lyrics('Kanye West', 3)
