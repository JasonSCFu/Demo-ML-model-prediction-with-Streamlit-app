import imageio

def create_gif(image_list, gif_name, duration = 1.0):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration = duration)
    return

image_list = ['img1.png','img2.png','img3.png','img4.png','img5.png','img6.png']
gif_name = 'GIF.gif'
duration = 1
create_gif(image_list, gif_name, duration)