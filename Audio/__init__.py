from Audio.link import link
from Audio.down import get_audio
from Audio.play import play_mp3

from utils.safe import sleep

def audio(word, save_base, loca='uk', is_play=False):
    targ_link = link(word, loca='uk')
    sleep(mode='spy')
    mp3_path, flag = get_audio(targ_link, save_base, word, loca=loca)
    if is_play:
        play_mp3(mp3_path)
    return mp3_path, flag


if __name__ == "__main__":
    targ = "link"
    t_link = link(targ)
    p = get_audio(t_link, '../test/audio_test', targ)
    play_mp3(p)


