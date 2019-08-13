from src import acquire_image_ids, acquire_annotations
import json

elte_id_with_polygon_data = acquire_annotations()

with open('annotations.json', 'w+') as final_annotations_file:
    json.dump(elte_id_with_polygon_data, final_annotations_file)

print('Written to file!')