import os
import json
import numpy as np
from PIL import Image, ImageDraw


def make_masks():

    with open(os.getcwd() + '/annotations.json', 'r') as annotations_file:
        annotations = json.load(annotations_file)

    for image_id in annotations:
        print("Processing : ", image_id)
        for label in annotations[image_id].keys():
            polygons = annotations[image_id][label]
            for polygon in polygons:
                filename = image_id + "_" + label + "_("
                polygon = np.array(polygon)
                x_coords = polygon[::2]
                y_coords = polygon[1::2]
                min_x, max_x = np.min(x_coords), np.max(x_coords)
                min_y, max_y = np.min(y_coords), np.max(y_coords)
                width = max_x - min_x
                height = max_y - min_y
                downsampling_factor = get_downsampling_factor(width, height)
                filename += "%.2f," % downsampling_factor
                filename += "%d," % min_x
                filename += "%d," % min_y
                filename += "%d," % width
                filename += "%d)-mask.png" % height
                if width < 50 and height < 50:
                    print("Not saving polygon since it is too small : ",
                          filename)
                    continue
                print(filename)
                ds_width, ds_height = int(round(
                    width // downsampling_factor)), int(
                        round(height // downsampling_factor))
                ds_polygon = polygon
                ds_polygon[::2] = ds_polygon[::2] - min_x
                ds_polygon[1::2] = ds_polygon[1::2] - min_y
                ds_polygon = np.array(ds_polygon // downsampling_factor,
                                      dtype=int)
                img = Image.new('L', (ds_width, ds_height))
                draw = ImageDraw.Draw(img).polygon((ds_polygon.tolist()),
                                                   outline='white',
                                                   fill='white')
                img.save(os.getcwd() + "/exported_images/" + filename)


def get_downsampling_factor(width, height):
    if width > 60_000 and height > 60_000:
        return 16.0
    elif width > 20_000 and height > 20_000:
        return 8.0
    else:
        return 4.0