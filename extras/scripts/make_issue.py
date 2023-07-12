import xbmc
import xbmcgui
import sys
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

path   = sys.argv[2]
folder = sys.argv[3]
name   = sys.argv[4]


def make_issue_file():

    if not os.path.exists(path + folder + '.issue'):
        with open(path + folder + '.issue', 'w') as f:
            f.write('this is a album file!')
            xbmcgui.Dialog().notification('NewsStand', 'Issue "{}" created on "{}"'.format(folder, path), xbmcgui.NOTIFICATION_INFO, 5)
    else: 
        xbmcgui.Dialog().notification('NewsStand', 'Issue "{}" already saved on "{}"'.format(folder, path), xbmcgui.NOTIFICATION_WARNING, 5)  
        
def make_issue_folder():

    # xbmcgui.Dialog().ok('NewsStand', path + name + '\\' + name + '.issue')

    if not os.path.exists(path + name + '\\' + name + '.issue'):
        with open(path + name + '\\' + name + '.issue', 'w') as f:
            f.write('this is a album file!')
            xbmcgui.Dialog().notification('NewsStand', 'Issue "{}" created on "{}"'.format(name, path), xbmcgui.NOTIFICATION_INFO, 5)
    else: 
        xbmcgui.Dialog().notification('NewsStand', 'Issue "{}" already saved on "{}"'.format(name, path), xbmcgui.NOTIFICATION_WARNING, 5) 

def make_all_folder():    
    count = 0
    folder_dir = (next(os.walk(path))[1])    
    folder_count = len(folder_dir)
    
    progress = xbmcgui.DialogProgress()    
    
    for issues in folder_dir: 
        folder_name = os.path.basename(issues) 
        filename = folder_name + '.issue'
        
        progress.create('NewsStand', '')
        
        if not os.path.exists(path + folder_name + '\\' + filename):
             
            if progress.iscanceled():
                break   
            if folder_name == '':
                continue
            if os.path.exists(path + folder_name + '\\' + 'folder.jpg'):
                with open(path + folder_name + '\\' + filename, "w") as f:
                    f.write('this is a album file!')
                    count += 1
                    step_count = int(100 / folder_count * count)
                    progress.update(step_count, 'Making "{}" an Issue'.format(folder_name))
                
    progress.close()
    xbmcgui.Dialog().notification('NewsStand', '{} folders were defined as albums.'.format(count), xbmcgui.NOTIFICATION_WARNING, 5)
    
def insert_text():
    
    cover = path
    big_image = Image.open(cover)
    big_image.thumbnail((1000, 1500))
    big_image.save(folder + 'folder.jpg')
    
    title = xbmcgui.Dialog().yesno('NewsStand', 'Do you want to add a title in Folder Image?')
    if not title:
        xbmcgui.Dialog().ok('NewsStand', 'Folder."ext" Saved on "{}".'.format(folder))
        return        
    img = Image.open(folder + 'folder.jpg')
    text_title = xbmcgui.Dialog().input('Set the folder Title')
    font_size = xbmcgui.Dialog().input('Set the folder Title', '125', xbmcgui.INPUT_NUMERIC)
    
    font_file = xbmcgui.Dialog().browseSingle(1, 'Select the font file', 'local', '.ttf|.otf', True, False, 'C:\\Windows\\Fonts\\')
    
    text_size = int(font_size)
    text_font = ImageFont.truetype(font_file, text_size)       
    
    image_title = ImageDraw.Draw(img)
    
    image_width = img.width
    image_height = img.height      
    text_width, text_heigth  = image_title.textsize(text_title, font=text_font)        
    center_width, center_heigth = (image_width - text_width) / 2, (image_height - text_heigth) / 2

    image_title.text((center_width + 5, 6), text_title, font=text_font, fill=(0, 0, 0))
    image_title.text((center_width, 1), text_title, font=text_font, fill=(255, 255, 255))
    img.save(folder + 'folder.jpg')
    
    xbmcgui.Dialog().ok('NewsStand', 'Folder."ext" Saved on "{}".'.format(folder))

def make_folder_cover(): 

    if not os.path.exists(folder + 'folder.jpg'):    
        insert_text()
    else:
        ret = xbmcgui.Dialog().yesno('NewsStand', 'Folder image already saved on "{}". Do you want to replace?'.format(folder))
        if not ret:
            return        
        insert_text()

# --- Script Entry Point ---#
if ( __name__ == "__main__" ):
    if len(sys.argv[ 1 ]) > 0:
        if sys.argv[1] == "issue_file":
            make_issue_file()
        elif sys.argv[1] == "issue_folder":
            make_issue_folder()    
        elif sys.argv[1] == "all_folder":
            make_all_folder() 
        elif sys.argv[1] == "make_folder_cover":
            make_folder_cover() 