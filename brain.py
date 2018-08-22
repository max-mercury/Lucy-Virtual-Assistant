
from GreyMatter import tell_time, general_conversations, weather, define_subject,bussiness_news_reader,open_firefox,connect_proxy, sleep

from GreyMatter import play_music, faculty, mapvit


def brain(name, speech_text, music_path,city_name, city_code, proxy_username,proxy_password):
    def check_message(check):
        '''
        This function checks if the items in the list(specified in argument)
        are present in the user's input speech.
        '''
        words_of_message = speech_text.split()

        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
    if check_message(['who', 'are', 'you']):
        general_conversations.who_are_you()
    elif check_message(['how','i','look']) or check_message(['how','am','i']):
        general_conversations.how_am_i()
    elif check_message(['joke']) or check_message(['tell','joke']):
        general_conversations.tell_joke()
    elif check_message(['who','am','i']):
        general_conversations.who_am_i()
    elif check_message(['how','are','you']):
        general_conversations.how_are_you()
    elif check_message(['time']):
        tell_time.what_is_time()
    elif check_message(['how','weather']) or check_message(['hows','weather']):
        weather.weather(city_name, city_code)
    elif check_message(['define']):
        define_subject.define_subject(speech_text)
    elif check_message(['news']):
        bussiness_news_reader.news_reader()
    elif check_message(['open','firefox']):
        open_firefox.open_firefox()
    elif check_message(['google']):
        open_firefox.google_open(speech_text)
    elif check_message(['youtube']):
        open_firefox.youtube_open(speech_text)
    elif check_message(['sleep']):
        sleep.go_to_sleep()
    elif check_message(['play','music']) or check_message(['music']):
        play_music.play_random(music_path)
    elif check_message(['play']):
        play_music.play_specific_music(speech_text, music_path)
    elif check_message(['party','time']) or check_message(['party','mix']):
        play_music.play_shuffle(music_path)
    elif check_message(['faculty']):
        faculty.faculty_search(speech_text)
    elif check_message(['about','vit']):
        faculty.about_vit()
    elif check_message(['directions','electronics','department']):
        mapvit.etrx_block()
    elif check_message(['directions','biomedical','department']):
        mapvit.biom_block()
    elif check_message(['directions','library']):
        mapvit.library_block()
    elif check_message(['directions','vlounge','v','lounge']):
        mapvit.vlounge_block()

    else:
        open_firefox.search_net(speech_text)
