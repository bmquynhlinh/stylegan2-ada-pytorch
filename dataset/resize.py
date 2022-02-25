import os

import PIL

def main():
    list = []
    for (dirpath, dirnames, filenames) in os.walk('./pokemon_jpg'):
        for file in filenames:
            list += ['./pokemon_jpg/' + file]
    print(list)

    for link in list:
        image = PIL.Image.open(link)
        image.resize((512,512))
        image.save(link.replace('pokemon_jpg','pokemon512'))

    pass

if __name__=="__main__":
    main()