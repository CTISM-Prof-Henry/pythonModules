from artistas.kanye import configuracao
from artistas.kanye.songs import get_lyrics

if __name__ == '__main__':
    print('main.py: Vou executar a função configuracao() de __init__, e depois a função get_lyrics() de songs')
    configuracao()
    get_lyrics('Kanye West', 3)
