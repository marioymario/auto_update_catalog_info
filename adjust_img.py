import os
from PIL import Image

def transforma(rotation, new_size, ext, in_loc, out_loc):

    rotation = rotation
    new_size = new_size
    in_loc = in_loc
    out_loc = out_loc
    new_ext = ext
    counter = 0

    for filename in os.listdir(in_loc):
        if not filename.endswith('.tiff'):
            continue
        ##
        in_path = os.path.join(in_loc, filename)

        # Opening and adjusting the image.
        im = Image.open(in_path)
        new_img = im.rotate(rotation).resize(new_size).convert('RGB')
        # Saving image at proper location
        out_path = os.path.join(out_loc, filename[:-4] + new_ext)
        new_img.save(str(out_path))
        counter +=1
    print(counter)

