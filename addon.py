from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
URL = "https://feed.podbean.com/thericksmithshow/feed.xml"

@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/762480/FSTV_Head_shot_time.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('latest_episodes'),
            'thumbnail': "https://pbcdn1.podbean.com/imglogo/image-logo/762480/FSTV_Head_shot_time.jpg"},
   ]
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

@plugin.route('/latest_episodes/')
def latest_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

if __name__ == '__main__':
    plugin.run()
