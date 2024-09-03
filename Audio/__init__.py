import os

from Audio.link import link
from Audio.down import get_audio
from Audio.play import play_mp3

from utils.safe import sleep

def audio(word, save_base, loca='uk', is_play=False):
    if os.path.exists((mp3_path := os.path.join(save_base, f"{loca}/{word}.mp3"))):
        print(f'{word} is exist, search next!')
        return mp3_path, True
    targ_link = link(word, loca='uk')
    sleep(mode='spy')
    mp3_path = get_audio(targ_link, save_base, word, loca=loca)
    if is_play:
        play_mp3(mp3_path)
    return mp3_path, False


if __name__ == "__main__":
    # targ = "link"
    # t_link = link(targ)
    # p = get_audio(t_link, '../test/audio_test', targ)
    # play_mp3(p)
    p, f = audio('link', '../test/audio_test', 'uk')


