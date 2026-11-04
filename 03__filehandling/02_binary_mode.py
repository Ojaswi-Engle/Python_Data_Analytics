with open(b"C:\Users\Mohit\Downloads\wp8861355-positive-quotes-desktop-wallpapers.jpg",'rb') as f:
    data=f.read()
    print(data)
with open(b"C:\Users\Mohit\Downloads\wallpaper.jpg",'wb') as f_:
    f_.write(data)
