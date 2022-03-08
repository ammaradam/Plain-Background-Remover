import cv2
import numpy as np
import argparse

def display_img(image, image_name='Image'):
    cv2.imshow(image_name, image)
    cv2.waitKey(-1)
    cv2.destroyAllWindows()

def resize_img(image, dim):
    if isinstance(dim, int):
        assert (dim > 0 and dim <=100), 'Use dimension value in range [0 < dim <= 100]'
        width = int(image.shape[1] * dim / 100)
        height = int(image.shape[0] * dim / 100)
        dim = (width, height)
    
    if isinstance(dim, tuple):
        return cv2.resize(image, dim, interpolation = cv2.INTER_AREA), dim
    else:
        return image, dim

def get_bg(image):
    unq, count = np.unique(image.reshape(-1,3), axis=0, return_counts=True)
    bg_color = unq[count.argmax()]
    return bg_color

def replace_bg(image, bg_image):
    # resize background image to match input image
    if image.shape != bg_image.shape:
        bg_image, _ = resize_img(bg_image, dim=image.shape[0:2])

    bg_region = np.all(image == tuple(get_bg(image)), axis=-1)
    image[bg_region] = bg_image[bg_region]
    return image

def main(image, bg_image):
    # read in image
    ori_image = cv2.imread(image_path)
    bg_image = cv2.imread(bg_image_path)

    # resize image for display
    ori_image, dim = resize_img(ori_image, dim=20)
    display_img(ori_image, image_name='Ori Image')

    # auto-replace background with background image
    out_image = replace_bg(ori_image, bg_image)

    display_img(out_image, image_name='Out Image')



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, default='images/cat3.png', help='Path to original image')
    parser.add_argument('--bg_image', type=str, default='images/background.jpg', help='Path to background image')
    arg = parser.parse_args()

    # image_path = 'images/cat3.png'
    # bg_image_path = 'images/background.jpg'

    image_path = arg.image
    bg_image_path = arg.bg_image

    assert image_path, "Please enter image path"
    assert bg_image_path, "Please enter background image path"

    main(image_path, bg_image_path)