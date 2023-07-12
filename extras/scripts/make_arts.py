import xbmc
import xbmcvfs
import xbmcgui
import xbmcaddon
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

SETTINGS = xbmcaddon.Addon('plugin.program.newsstand')

# Get Settings from NewsStand
characters_arts_dir = SETTINGS.getSetting('characters_arts_dir')
genres_arts_dir = SETTINGS.getSetting('genres_arts_dir')
publishers_arts_dir = SETTINGS.getSetting('characters_arts_dir')

banners_arts_dir = SETTINGS.getSetting('banners_arts_dir')
clearlogos_arts_dir = SETTINGS.getSetting('clearlogos_arts_dir')
fanarts_arts_dir = SETTINGS.getSetting('fanarts_arts_dir')

# Get Directory and name from image
image_file = sys.argv[2]
#xbmcgui.Dialog().ok('kodi', '{}'.format(image_file))
folder = sys.argv[3]
# name   = sys.argv[4]

options = ['Character', 'Genre', 'Publisher']
dialog = xbmcgui.Dialog()
selected_option = dialog.select('Select the item to be used:', options)

if selected_option != -1:
    selected = options[selected_option]
    if selected == 'Character':
        items = ['Character Poster', 'Character Fanart', 'Character Banner']
    elif selected == 'Genre':
        items = ['Genre Poster', 'Genre Fanart', 'Genre Banner']
    elif selected == 'Publisher':
        items = ['Publisher Poster', 'Publisher Fanart', 'Publisher Banner']
    selected_item = dialog.select('Select an item:', items)    
    
    if selected == 'Character':
        if selected_item == 0:
            name_list_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.program.newsstand/db_characters')
            name_list_ext = os.listdir(name_list_path)
            name_list_items = [x.split('.json')[0] for x in name_list_ext]
            name_list_items.insert(0, '[ ADD NEW ]')
            if '[ Not set ]' in name_list_items:
                name_list_items.remove('[ Not set ]')
            selected_name = dialog.select('Select the Character Name:', name_list_items)
            if not selected_name == -1:
                if name_list_items[selected_name] == '[ ADD NEW ]':
                    char_name = xbmcgui.Dialog().input('Name of Character:')
                else:
                    char_name = name_list_items[selected_name]
                
                file_path = os.path.join(characters_arts_dir + char_name + '.jpg')
                big_image = Image.open(image_file)
                big_image.thumbnail((1000, 1500))
                if not os.path.exists(file_path):
                    big_image.save(characters_arts_dir + char_name + '.jpg')
                    xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Character poster'.format(char_name + '.jpg')))
                else:
                    ret = xbmcgui.Dialog().yesno('Newsstand', '{} already has a poster. Do you want to replce?'.format(char_name))
                    if ret:
                        big_image.save(characters_arts_dir + char_name + '.jpg')
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Character poster'.format(char_name + '.jpg')))
                    else:
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Character poster cancelled!'))
                    
                VCATEGORY_NAMES_ID = 'vcategory_names'
            else:
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Character poster cancelled!'))
        elif selected_item == 1:
            name_list_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.program.newsstand/db_characters')
            name_list_ext = os.listdir(name_list_path)
            name_list_items = [x.split('.json')[0] for x in name_list_ext]
            name_list_items.insert(0, '[ ADD NEW ]')
            if '[ Not set ]' in name_list_items:
                name_list_items.remove('[ Not set ]')
            selected_name = dialog.select('Select the Character Name:', name_list_items)
            if not selected_name == -1:
                if name_list_items[selected_name] == '[ ADD NEW ]':
                    char_name = xbmcgui.Dialog().input('Name of Character:')
                else:
                    char_name = name_list_items[selected_name]
                
                file_path = os.path.join(fanarts_arts_dir + char_name + '.jpg')
                big_image = Image.open(image_file)
                big_image.thumbnail((1920, 1280))
                if not os.path.exists(file_path):
                    big_image.save(fanarts_arts_dir + char_name + '.jpg')
                    xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Character fanart'.format(char_name + '.jpg')))
                else:
                    ret = xbmcgui.Dialog().yesno('Newsstand', '{} already has a fanart. Do you Want to replace?'.format(char_name))
                    if ret: 
                        big_image.save(fanarts_arts_dir + char_name + '.jpg')
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Character fanart'.format(char_name + '.jpg')))
                    else: 
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Character fanart cancelled!'))
            else:
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Character fanart cancelled!'))
        elif selected_item == 2:
            name_list_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.program.newsstand/db_characters')
            name_list_ext = os.listdir(name_list_path)
            name_list_items = [x.split('.json')[0] for x in name_list_ext]
            name_list_items.insert(0, '[ ADD NEW ]')
            if '[ Not set ]' in name_list_items:
                name_list_items.remove('[ Not set ]')
            selected_name = dialog.select('Select the Character Name:', name_list_items)
            if not selected_name == -1:
                if name_list_items[selected_name] == '[ ADD NEW ]':
                    char_name = xbmcgui.Dialog().input('Name of Character:')
                else:
                    char_name = name_list_items[selected_name]
                big_image = Image.open(image_file)
                big_image.thumbnail((1000, 323))
                big_image.save(banners_arts_dir + char_name + '.jpg')
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Character fanart'.format(char_name + '.jpg')))
            else:
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Character fanart cancelled!'))
    
    elif selected == 'Genre':
        if selected_item == 0:
            genre_list_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.program.newsstand/db_genres')
            genre_list_ext = os.listdir(genre_list_path)
            genre_list_items = [x.split('.json')[0] for x in genre_list_ext]
            genre_list_items.insert(0, '[ ADD NEW ]')
            if '[ Not set ]' in genre_list_items:
                genre_list_items.remove('[ Not set ]')
            selected_genre = dialog.select('Select the Genre Name:', genre_list_items)
            if not selected_genre == -1:
                if genre_list_items[selected_genre] == '[ ADD NEW ]':
                    genre_name = xbmcgui.Dialog().input('Name of Genre:')
                else:
                    genre_name = genre_list_items[selected_genre]
                big_image = Image.open(image_file)
                big_image.thumbnail((1000, 1500))
                big_image.save(genres_arts_dir + genre_name + '.jpg')
                dialog.ok('Selected', '{}'.format(genres_arts_dir + genre_name + '.jpg'))
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Genre poster'.format(genre_name + '.jpg')))
                VCATEGORY_GENRES_ID = 'vcategory_genres'
            else:
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Genre poster cancelled!'))
        elif selected_item == 1:
            genre_list_path = xbmcvfs.translatePath('special://profile/addon_data/plugin.program.newsstand/db_genres')
            genre_list_ext = os.listdir(genre_list_path)
            genre_list_items = [x.split('.json')[0] for x in genre_list_ext]
            genre_list_items.insert(0, '[ ADD NEW ]')
            if '[ Not set ]' in genre_list_items:
                genre_list_items.remove('[ Not set ]')
            selected_genre = dialog.select('Select the Genre Name:', genre_list_items)
            if not selected_genre == -1:
                if genre_list_items[selected_genre] == '[ ADD NEW ]':
                    genre_name = xbmcgui.Dialog().input('Name of Genre:')
                else:
                    genre_name = genre_list_items[selected_genre]
                
                file_path = os.path.join(fanarts_arts_dir + char_name + '.jpg')
                big_image = Image.open(image_file)
                big_image.thumbnail((1920, 1280))
                if not os.path.exists(file_path):
                    big_image.save(fanarts_arts_dir + char_name + '.jpg')
                    xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Genre fanart'.format(char_name + '.jpg')))
                else:
                    ret = xbmcgui.Dialog().yesno('Newsstand', '{} already has a fanart'.format(char_name))
                    if ret: 
                        big_image.save(fanarts_arts_dir + char_name + '.jpg')
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', '{} set as Genre fanart'.format(char_name + '.jpg')))
                    else: 
                        xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Genre fanart cancelled!'))
                
                VCATEGORY_GENRES_ID = 'vcategory_genres'
            else:
                xbmc.executebuiltin("Notification(%s, %s,)" % ('NewsStand', 'Set Genre fanart cancelled!'))

    
    elif selected == 'Publisher' and selected_item == 0:
        dialog.ok('Selected', '{}'.format('Publisher Poster'))
    
    elif selected_item == 1:
        dialog.ok('Selected', '{}'.format('fanart'))
    elif selected_item == 2:
        dialog.ok('Selected', '{}'.format('banner'))
    elif selected_item == 3:
        dialog.ok('Selected', '{}'.format('clearlogo'))
    