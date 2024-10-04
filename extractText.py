import matplotlib.pyplot as plt
from PIL import Image


def onclick(event):
  
    print(f'Clicked coordinates: x={event.xdata:.2f}, y={event.ydata:.2f}')


image_path = "image.png" 
image = Image.open(image_path)


fig, ax = plt.subplots()
ax.imshow(image)
ax.axis('off')  


cid = fig.canvas.mpl_connect('button_press_event', onclick)


plt.title("Click on the Image to Get Coordinates")
plt.show()
