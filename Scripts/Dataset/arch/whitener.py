from PIL import Image
  
img = Image.open('out.jpg')
rgba = img.convert("RGBA")
datas = rgba.getdata()
  
newData = []

for item in datas:
    if (item[0] == 0 and item[1] == 0 and item[2] == 0) or (item[0] == 1 and item[1] == 1 and item[2] == 1):
        newData.append((0, 255, 0))
    else:
        #print(item)
        newData.append(item)  # other colours remain unchanged
  
rgba.putdata(newData)
rgba.save("whitened2.png", "PNG")
