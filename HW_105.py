import os
import cv2

Images_Path = "Images"

Images = []

for image in os.listdir(Images_Path):
    name, extension = os.path.splitext(image)
    print(name)
    print(extension)
    if extension in ['.gif', '.jpg', '.jpeg', '.png', '.jfif']:
        image_name = Images_Path+'/'+image
        print(image_name)
        Images.append(image_name)

count = len(Images)
print(count)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height) 
Friendship_Album = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*"DIVX"), 4, size)

for i in range (0, count):
    frame = cv2.imread(Images[i])
    Friendship_Album.write(frame)

Friendship_Album.release()
print("Done!")
