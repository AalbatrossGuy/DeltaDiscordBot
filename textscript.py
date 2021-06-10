from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests
import datetime
import qrcode
from pyzbar.pyzbar import decode
from matplotlib import pyplot as plt
# print(image.size)
# print(image.format)
# print(image.show())


# def mask_circle_transparent(pil_img, blur_radius, offset=0):
#     offset = blur_radius * 2 + offset
#     mask = Image.new("L", pil_img.size, 0)
#     draw = ImageDraw.Draw(mask)
#     draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
#     mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

#     result = pil_img.copy()
#     result.putalpha(mask)

#     return result


# img1 = Image.open(r"Pictures/WelcomeMsg.png")

# draw = ImageDraw.Draw(img1)
# print(img1.size)
# font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)

# draw.text((400, 100), f"Welcome to Test Server", (0, 0, 0), font=font)
# draw.text((350, 500), f"You are member no. #20000", (0, 0, 0), font=font)
# # # Opening the secondary image (overlay image)
# img2 = Image.open(r"Pictures/test.png")
# #
# # # Pasting img2 image on top of img1
# # # starting at coordinates (0, 0)
# img1.paste(img2, (469, 180), mask=img2)
# #
# # # Displaying the image
# img1.show()

# img1 = Image.open(r"Pictures/WelcomeImg.jpg")

# draw = ImageDraw.Draw(img1)
# print(img1.size)
# font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)

# draw.text((400, 100), f"Welcome to Test Server", (0, 0, 0), font=font)
# draw.text((350, 500), f"You are member no. #20000", (0, 0, 0), font=font)
# # # Opening the secondary image (overlay image)
# img2 = Image.open(r"Pictures/test.png")
# #
# # # Pasting img2 image on top of img1
# # # starting at coordinates (0, 0)
# img1.paste(img2, (469, 180), mask=img2)

# # Displaying the image
# img1.show()


# def _add_corners(im, rad=100):
#     circle = Image.new('L', (rad * 2, rad * 2), 0)
#     draw = ImageDraw.Draw(circle)
#     draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
#     alpha = Image.new('L', im.size, "white")
#     w, h = im.size
#     alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
#     alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
#     alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
#     alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
#     im.putalpha(alpha)
#     return im


# im = _add_corners(img1)


# print(im.show())

"""This is a test for a movie based api command. The command is not complete yet."""


# def test_for_api(query: str):
#     url = f"https://www.omdbapi.com/?t={query}&apikey=706a1bfd"
#     print(url)
#     response = requests.request("GET", url=url)
#     data = response.json()
#     print(data)
#     title = data['Title']
#     year = data['Year']
#     rated = data['Rated']
#     released = data['Released']
#     length = data['Runtime']
#     genre = data['Genre']
#     director = data['Director']
#     writer = data['Writer']
#     actors = data['Actors']
#     language = data['Language']
#     country = data['Country']
#     awards = data['Awards']
#     Poster_Img = data['Poster']
#     rating = data['imdbRating']
#     votes = data['imdbVotes']
#     type = data['movie']
#     boxoffice = data['BoxOffice']


# Test Query
# test_for_api("Moana")

# def test_for_weather_api(query:str):
#     url = f"http://api.openweathermap.org/data/2.5/weather?appid=77f5585dd715ec1e39ba87b818b44498&q={query}"

#     response = requests.request("GET", url=url)
#     # For debugging purpose
#     # print(response)
#     data = response.json()
#     # print(data)
#     longitude = data['coord']['lon']
#     latitude = data['coord']['lat']
#     # print(longitude, latitude)
#     cloud_type = data['weather'][0]['description']
#     # print(cloud_type)
#     temp = data['main']['temp']
#     feels_like = data['main']['feels_like']
#     temp = (temp - 273.15).__format__('0.2f')
#     feels_like = (feels_like - 273.15).__format__('0.2f')
#     # print(temp, feels_like)
#     min_temp = data['main']['temp_min']
#     min_temp = (min_temp - 273.15).__format__('0.2f')
#     max_temp = data['main']['temp_max']
#     max_temp = (max_temp - 273.15).__format__('0.2f')
#     pressure = data['main']['pressure'] # unit hPa
#     humidity = data['main']['humidity'] # unit percentage
#     wind_speed = data['wind']['speed']
#     # print(min_temp, max_temp, pressure, humidity, wind_speed)
#     country = data['sys']['country']
#     city_name = data['name']



# test_for_weather_api("delhi")

""" Horizontal Bar Chart related tests"""

# import matplotlib.pyplot as plt 
# import numpy as np 
# import qrcode
# from PIL import Image


# np.random.seed(19680801)
# def checkesc(args):
#     args = list(args)
#     for i in range(len(args)):
#         if args[i] == '|':
#             return False
#         else:
#             return True


# def makebar(args):
    #args = str(args).replace(' ', '')
    #args = list(args)
    #tupbefore = []
    #tupafter = []
    #index = args.index('|')
    #tupbefore = args[0:index]
    #tupafter = args[index+1:]
    # print(tupbefore)
    # print(tupafter)
    #plt.rcdefaults()
    #fig, axes = plt.subplots()
    #numbers = tupbefore
    #labels = tupafter
    #axes.barh(labels, numbers, align='center')
    #axes.set_xlabel('X Axis --->')
    #axes.set_ylabel("Y Axis --->")
    #axes.set_title('Horizontal Bar Chart')
    #plt.savefig('chart.png')
    #plt.show()


#print(makebar('1 2 3 4 | 9 6 7 8'))


def makebar_test2(args):
    args = tuple(args.split(' '))
    index = args.index('|')
    args = list(args)
    args.pop(index)
    args = tuple(args)
    before = args[:index]
    after = args[index:]
    plt.rcdefaults()
    fig, axes = plt.subplots()
    axes.barh(before, after, align='center')
    axes.set_xlabel("X Axis --->")
    axes.set_ylabel("Y Axis --->")
    axes.set_title("Horizontal Bar Chart")
    #plt.show()

print(makebar_test2('Sammy Jonny 3 4 3 9 0 | 12 14 15.5 18 3 7 7'))

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
#qr.add_data('THis is an example test line')
#qr.make(fit=True)
#img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

#img.show()


#img = Image.open('referenceqrcode.png')

#result = decode(img)
#for i in result:
   #print(i.data.decode("utf-8"))
   #print(i.type)
   #print(i.rect)




import re
from pistonapi import PistonAPI
op = """
```java
class java{
   public static void main(String args[]){
        System.out.println("test");
}
 }
```
"""

def regex(code):
    pattern="`{3}([\w]*)\n([\S\s]+?)\n`{3}"
    replace=''
    result=re.compile(pattern)
    stdin = re.findall(result, code)[0][1]
    print(stdin)

#regex(op)

piston = PistonAPI()
#print(piston.languages)


language = ("bash", "brainfuck", "cjam", "clojure", "cobol", "coffeescript", "cow", "crystal", "dart", "dash", "deno", "dotnet", "dragon", "elixir", "emacs", "erlang", "gawk", "gcc", "go", "golfscript", "groovy",
             "haskell", "java", "jelly", "juila", "kotlin", "lisp", "lolcode", "lua", "mono", "nasm", "nim", "node", "ocaml", "octave", "osabie", "paradoc", "pascal", "perl", "php", "ponylang", "prolog", "pure", "pyth", "python",
             "rockstar", "ruby", "rust", "scala", "swift", "typescript", "vlang", "yeethon", "zig")

versions = ("5.1.0", "2.7.3", "0.6.5", "1.10.3", "3.1.2", "2.5.1", "1.0.0", "0.36.1", "2.12.1", "0.5.11", "1.7.5", "5.0.201", "1.9.8", "1.11.3", "27.1.0", "23.0.0", "5.1.0", "10.2.0", "1.16.2", "1.0.0", "3.0.7", "9.0.1", "15.0.2",
            "0.1.31", "1.5.4", "1.4.31", "2.1.2", "0.11.2", "5.4.2", "6.12.0", "2.15.5", "1.4.4", "15.10.0", "4.12.0", "6.2.0", "1.0.1", "0.6.0", "3.2.0", "5.26.1", "8.0.2", "0.39.0", "8.2.4", "0.68.0", "1.0.0", "3.9.4", "1.0.0", 
            "3.0.1", "1.50.0", "3.0.0", "5.3.3", "4.2.3", "0.1.13", "3.10.0", "0.7.1")

pattern="`{3}([\w]*)\n([\S\s]+?)\n`{3}"

result=re.compile(pattern)
stdin = re.findall(result, op)[0][1]

langtest = 'java'
#for language, version in zip(language, versions):
    #print(f"{language}: v{version}")


import json

#language = 'ruby'
#langs = json.loads(requests.get('https://emkc.org/api/v2/piston/runtimes').text)
#l= []
#v=[]
#for lang in langs:
#    if lang['language'] == language:
#        l.append(lang['language'])
#        l.append(lang['version'])
#        if len(l) > 2:
#            for i in range(1, len(l), 2):
#                v.append(l[i][0])

base_fetch_url = "https://emkc.org/api/v2/piston/runtimes"

languages = json.loads(requests.get('https://emkc.org/api/v2/piston/runtimes').text)

for lang in languages:
    if lang['language'] == langtest:
        print(f"{lang['language']} : {lang['version']}")
