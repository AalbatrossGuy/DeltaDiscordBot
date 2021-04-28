from PIL import Image, ImageDraw, ImageFilter, ImageFont
import requests


# print(image.size)
# print(image.format)
# print(image.show())


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)

    return result


img1 = Image.open(r"Pictures/WelcomeMsg.png")

draw = ImageDraw.Draw(img1)
print(img1.size)
font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)

draw.text((400, 100), f"Welcome to Test Server", (0, 0, 0), font=font)
draw.text((350, 500), f"You are member no. #20000", (0, 0, 0), font=font)
# # Opening the secondary image (overlay image)
img2 = Image.open(r"Pictures/test.png")
#
# # Pasting img2 image on top of img1
# # starting at coordinates (0, 0)
img1.paste(img2, (469, 180), mask=img2)
#
# # Displaying the image
img1.show()

img1 = Image.open(r"Pictures/WelcomeImg.jpg")

draw = ImageDraw.Draw(img1)
print(img1.size)
font = ImageFont.truetype(r"Fonts/ZenDots-Regular.ttf", 30)

draw.text((400, 100), f"Welcome to Test Server", (0, 0, 0), font=font)
draw.text((350, 500), f"You are member no. #20000", (0, 0, 0), font=font)
# # Opening the secondary image (overlay image)
img2 = Image.open(r"Pictures/test.png")
#
# # Pasting img2 image on top of img1
# # starting at coordinates (0, 0)
img1.paste(img2, (469, 180), mask=img2)

# Displaying the image
img1.show()


def _add_corners(im, rad=100):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, "white")
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


im = _add_corners(img1)


# print(im.show())

"""This is a test for a movie based api command. The command is not complete yet."""


def test_for_api(query: str):
    url = f"https://www.omdbapi.com/?t={query}&apikey=706a1bfd"
    print(url)
    response = requests.request("GET", url=url)
    data = response.json()
    print(data)
    title = data['Title']
    year = data['Year']
    rated = data['Rated']
    released = data['Released']
    length = data['Runtime']
    genre = data['Genre']
    director = data['Director']
    writer = data['Writer']
    actors = data['Actors']
    language = data['Language']
    country = data['Country']
    awards = data['Awards']
    Poster_Img = data['Poster']
    rating = data['imdbRating']
    votes = data['imdbVotes']
    type = data['movie']
    boxoffice = data['BoxOffice']


# Test Query
test_for_api("Moana")
