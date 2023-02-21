import colorgram

colors = colorgram.extract("images/wrong.png", 6)
for i in range(len(colors)):
    first_color = colors[i]
    rgb = first_color.rgb
    rgb = tuple([rgb[n] for n in range(3)])

    print(rgb)

