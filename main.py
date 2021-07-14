import shutil
import os
from ext_list import pictures_ext, video_ext, software_ext, documents_ext, audio_ext

# Set paths for the different folders where files will be sent
software_path = "/home/gaurav/Software/moved_by_python"
music_path = "/home/gaurav/Music/moved_by_python"
picture_path = "/home/gaurav/Pictures/moved_by_python"
video_path = "/home/gaurav/Videos/moved_by_python"
documents_path = "/home/gaurav/Documents/moved_by_python"

# Create empty lists (same # as # of paths) to store extensions strings from nested dictionaries
pictures, music, documents, video, software = ([] for i in range(5))

# set the source (can leave dest empty. filled here for testing purposes)
source = "/home/gaurav/Downloads"
destination = "/home/gaurav/Desktop/projects/file_mover/destination"

# grab all the files within the source folder
files = os.listdir(source)

# store the values from the dictionaries within a list
def listify(dic):
    l = []
    for dictionary in dic.values():
        for item in dictionary:
            l.append(item)
    return l

# get lists
pictures = listify(pictures_ext)
software = listify(software_ext)
video = listify(video_ext)
music = listify(audio_ext)
documents = listify(documents_ext)

for file in files:
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]

    if file_extension in pictures:
        destination = picture_path
        print("Image: ")
    elif file_extension in video:
        print("Video: ")
        destination = video_path
    elif file_extension in software:
        print("Software: ")
        destination = software_path
    elif file_extension in documents:
        print("Document: ")
        destination = documents_path
    elif file_extension in music:
        print("Audio: ")
        destination = music_path
    else:
        continue

    new_path = shutil.move(f"{source}/{file}", destination)
    print (new_path)
