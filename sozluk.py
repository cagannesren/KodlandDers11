meme_dict = {
            "CREEPY": "korkunç bir şey",
            "ROFL" : "bir şakaya karşılık cevap",
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
  print(meme_dict[word])
else:
    print("YANLIŞ GİRDİNİZ")
