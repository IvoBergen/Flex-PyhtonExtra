from PIL import Image, ImageFont, ImageDraw
afbeelding = Image.open("meme_image.jpg")



breedte = afbeelding.width
hoogte = afbeelding.height
print('De afbeelding is ' + str(breedte) + " pixels breed en" + str(hoogte) + " pixels hoog")
print(afbeelding.format, afbeelding.size, afbeelding.mode)


lettertype = ImageFont.truetype("impact.ttf", 20)

tekengebied = ImageDraw.Draw(afbeelding)


tekst = "Imagine having a \n Windoge"

tekst_breedte, tekst_hoogte = tekengebied.textsize(tekst, font= lettertype)

print('tekstbreedte= ' + str(tekst_breedte) +', teksthoogte= ' + str(tekst_hoogte))

tekst_x = (breedte - tekst_breedte) / 2
tekst_y = (hoogte - tekst_hoogte) / 2

tekengebied.multiline_text((10,10), tekst, font = lettertype, fill=(0,0,0))
tekengebied.multiline_text((10-2, 10-2), tekst, font=lettertype, fill=(255,255,255))


afbeelding.show()
afbeelding.save("meme_image_tekst.jpg")

