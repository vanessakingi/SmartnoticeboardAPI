import urllib.request, string, random, os, shutil
from PIL import Image
from django.core.files.storage import FileSystemStorage
from mimetypes import guess_extension
from urllib.request import urlretrieve
from django.conf import settings


def base64decoding(pictures, file_type):
    print(pictures)
    url = """data:image/"""+file_type+""";base64,"""+pictures
    filename, m = urlretrieve(url)
    size=10
    chars=string.ascii_uppercase + string.digits
    newName = ''.join(random.choice(chars) for _ in range(size))
    newName_thumb = ''.join(random.choice(chars) for _ in range(size))+'_thumb'+'.png'
    new_name = shutil.copy(filename, settings.MEDIA_ROOT+'/'+newName+'.'+file_type)
    print()
    data = {
        "newName":newName+'.'+file_type,
        "newName_thumb": newName_thumb,
    }

    return data

def find(Name):
    for root, dirs, files in os.walk(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))):
        if Name in files:
            return os.path.join(root, Name)