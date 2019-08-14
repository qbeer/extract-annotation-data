import os
import json
import numpy as np

karolinska_to_elte = {
    'CRC_LN_SU_2016_001': '08301_16_I_10_HE',
    'CRC_LN_SU_2016_002': '08301_16_I_16_HE',
    'CRC_LN_SU_2016_003': '08509_16_14_HE',
    'CRC_LN_SU_2016_004': '08901_16_I_14_HE',
    'CRC_LN_SU_2016_005': '08965_16_09_HE',
    'CRC_LN_SU_2016_006': '08965_16_16_HE',
    'CRC_LN_SU_2016_007': '08965_16_22_HE',
    'CRC_LN_SU_2016_008': '09224_16_09_HE',
    'CRC_LN_SU_2016_009': '09224_16_12_HE',
    'CRC_LN_SU_2016_010': '09224_16_13_HE',
    'CRC_LN_SU_2016_011': '09436_16_9_HE',
    'CRC_LN_SU_2016_012': '09483_16_I_09_HE',
    'CRC_LN_SU_2016_013': '09483_16_I_10_HE',
    'CRC_LN_SU_2016_014': '09676_16_33_HE',
    'CRC_LN_SU_2016_015': '09864_16_8_HE',
    'CRC_LN_SU_2016_016': '09910_16_10_HE',
    'CRC_LN_SU_2016_017': '10100_16_18_HE',
    'CRC_LN_SU_2016_018': '10102_16_12_HE',
    'CRC_LN_SU_2016_019': '10222_16_I_10_HE',
    'CRC_LN_SU_2016_020': '10222_16_I_13_HE',
    'CRC_LN_SU_2016_021': '10424_16_8_HE',
    'CRC_LN_SU_2016_022': '10424_16_9_HE',
    'CRC_LN_SU_2016_023': '10947_16_8_HE',
    'CRC_LN_SU_2016_024': '10947_16_11_HE',
    'CRC_LN_SU_2016_025': '10996_16_10_HE',
    'CRC_LN_SU_2016_026': '11418_16_12_HE',
    'CRC_LN_SU_2016_027': '11418_16_13_HE',
    'CRC_LN_SU_2016_028': '11418_16_16_HE',
    'CRC_LN_SU_2016_029': '11636_16_21_HE',
    'CRC_LN_SU_2016_030': '11636_16_23_HE',
    'CRC_LN_SU_2016_031': '11636_16_24tm_HE',
    'CRC_LN_SU_2016_032': '11654_16_12_HE',
    'CRC_LN_SU_2016_033': '11654_16_14_HE',
    'CRC_LN_SU_2016_034': '12234_16_10_HE',
    'CRC_LN_SU_2016_035': '12470_16_I_11_HE',
    'CRC_LN_SU_2016_036': '12808_16_10_HE',
    'CRC_LN_SU_2016_037': '12871_16_10_HE',
    'CRC_LN_SU_2016_038': '12871_16_13_HE',
    'CRC_LN_SU_2016_039': '13339_16_15_HE',
    'CRC_LN_SU_2016_040': '13339_16_16_HE',
    'CRC_LN_SU_2016_041': '13339_16_30_HE',
    'CRC_LN_SU_2016_042': '13612_16_10_HE',
    'CRC_LN_SU_2016_043': '13805_16_11_HE',
    'CRC_LN_SU_2016_044': '13805_16_12_HE',
    'CRC_LN_SU_2016_045': '14015_16_15_HE',
    'CRC_LN_SU_2016_046': '14015_16_16_HE',
    'CRC_LN_SU_2016_047': '14015_16_18_HE',
    'CRC_LN_SU_2016_048': '14016_16_9_HE',
    'CRC_LN_SU_2016_049': '14016_16_11_HE',
    'CRC_LN_SU_2016_050': '14016_16_13_HE',
    'CRC_LN_SU_2016_051': '14335_16_I_7_HE',
    'CRC_LN_SU_2017_001': '01101_17_11_HE',
    'CRC_LN_SU_2017_002': '01190_17_15_HE',
    'CRC_LN_SU_2017_003': '01190_17_19_HE',
    'CRC_LN_SU_2017_004': '02222_17_8_HE',
    'CRC_LN_SU_2017_005': '02286_17_8',
    'CRC_LN_SU_2017_006': '02396_17_II_15_HE',
    'CRC_LN_SU_2017_007': '02396_17_II_17_HE',
    'CRC_LN_SU_2017_008': '02492_17_15_HE',
    'CRC_LN_SU_2017_009': '02626_17_9_HE',
    'CRC_LN_SU_2017_010': '02626_17_12_HE',
    'CRC_LN_SU_2017_011': '02704_17_13_HE',
    'CRC_LN_SU_2017_012': '02704_17_14_HE',
    'CRC_LN_SU_2017_013': '02704_17_15_HE',
    'CRC_LN_SU_2017_014': '02749_17_7_HE',
    'CRC_LN_SU_2017_015': '02817_17_10_HE',
    'CRC_LN_SU_2017_016': '02912_17_II_7_HE',
    'CRC_LN_SU_2017_017': '02912_17_II_9_HE',
    'CRC_LN_SU_2017_018': '03023_17_I_9_HE',
    'CRC_LN_SU_2017_019': '03023_17_I_11_HE',
    'CRC_LN_SU_2017_020': '03117_17_I_12_HE',
    'CRC_LN_SU_2017_021': '03117_17_I_16_HE',
    'CRC_LN_SU_2017_022': '03117_17_I_19_HE',
    'CRC_LN_SU_2017_023': '03182_17_6_HE',
    'CRC_LN_SU_2017_024': '03182_17_7_HE',
    'CRC_LN_SU_2017_025': '03330_17_10_HE',
    'CRC_LN_SU_2017_026': '03330_17_11_HE',
    'CRC_LN_SU_2017_027': '03331_17_12_HE',
    'CRC_LN_SU_2017_028': '03331_17_13_HE',
    'CRC_LN_SU_2017_029': '03331_17_17_HE',
    'CRC_LN_SU_2017_030': '04127_17_2_HE',
    'CRC_LN_SU_2017_031': '05197_17_I_6_HE',
    'CRC_LN_SU_2017_032': '05198_17_I_14_HE',
    'CRC_LN_SU_2017_033': '05198_17_I_22_HE',
    'CRC_LN_SU_2017_034': '05493_17_10_HE',
    'CRC_LN_SU_2017_035': '05498_17_8_HE',
    'CRC_LN_SU_2017_036': '05498_17_9_HE',
    'CRC_LN_SU_2017_037': '05498_17_12_HE',
    'CRC_LN_SU_2017_038': '05601_17_21_HE',
    'CRC_LN_SU_2017_039': '05601_17_23_HE',
    'CRC_LN_SU_2017_040': '05601_17_25_HE',
    'CRC_LN_SU_2017_041': '05679_17_I_7_HE',
    'CRC_LN_SU_2017_042': '06408_17_9_HE',
    'CRC_LN_SU_2017_043': '06409_17_I_8_HE',
    'CRC_LN_SU_2017_044': '06409_17_I_13_HE',
    'CRC_LN_SU_2017_045': '07234_17_3_HE',
    'CRC_LN_SU_2017_046': '07234_17_12_HE',
    'CRC_LN_SU_2017_047': '07355_17_8_HE',
    'CRC_LN_SU_2017_048': '07355_17_9_HE',
    'CRC_LN_SU_2017_049': '07355_17_10_HE',
    'CRC_LN_SU_2017_050': '07511_17_9_HE',
    'CRC_LN_SU_2017_051': '7511_17_14_HE',
    'CRC_LN_SU_2017_052': '8190_17_15_HE',
    'CRC_LN_SU_2017_053': '08299_17_16_HE',
    'CRC_LN_SU_2017_054': '08299_17_18_HE',
    'CRC_LN_SU_2017_055': '08299_17_21_HE',
    'CRC_LN_SU_2017_056': '8398_17_10_HE',
    'CRC_LN_SU_2017_057': '8398_17_11_HE',
    'CRC_LN_SU_2017_058': '8398_17_12_HE',
    'CRC_LN_SU_2017_059': '8618_17_10_HE',
    'CRC_LN_SU_2017_060': '8620_17_8_HE',
    'CRC_LN_SU_2017_061': '8620_17_12_HE',
    'CRC_LN_SU_2017_062': '8621_17_I_11_HE',
    'CRC_LN_SU_2017_063': '8621_17_I_13_HE',
    'CRC_LN_SU_2017_064': '8621_17_I_14_HE',
    'CRC_LN_SU_2017_065': '09155_17_I_14_HE',
    'CRC_LN_SU_2017_066': '09155_17_I_15_HE',
    'CRC_LN_SU_2017_067': '09155_17_I_16_HE',
    'CRC_LN_SU_2017_068': '10336_17_11_HE',
    'CRC_LN_SU_2017_069': '10336_17_12_HE',
    'CRC_LN_SU_2017_070': '10336_17_25_HE',
    'CRC_LN_SU_2017_071': '10500_17_11_HE',
    'CRC_LN_SU_2017_072': '10791_17_16_HE',
    'CRC_LN_SU_2017_073': '10791_17_17_HE',
    'CRC_LN_SU_2017_074': '11228_17_11_HE',
    'CRC_LN_SU_2017_075': '11228_17_12_HE',
    'CRC_LN_SU_2017_076': '11492_17_15_HE',
    'CRC_LN_SU_2017_077': '11492_17_17_HE',
    'CRC_LN_SU_2017_078': '11591_17_22_HE',
    'CRC_LN_SU_2017_079': '11591_17_23_HE',
    'CRC_LN_SU_2017_080': '11591_17_25_HE',
    'CRC_LN_SU_2017_081': '11727_17_10_HE',
    'CRC_LN_SU_2017_082': '11956_17_11_HE',
    'CRC_LN_SU_2017_083': '11967_17_11_HE',
    'CRC_LN_SU_2017_084': '11967_17_14_HE',
    'CRC_LN_SU_2017_085': '11967_17_23_HE',
    'CRC_LN_SU_2017_086': '12142_17_12_HE',
    'CRC_LN_SU_2017_087': '12142_17_13_HE',
    'CRC_LN_SU_2017_088': '12142_17_17_HE',
    'CRC_LN_SU_2017_089': '12391_17_I_13',
    'CRC_LN_SU_2017_090': '12603_17_13_HE',
    'CRC_LN_SU_2017_091': '12603_17_20_HE',
    'CRC_LN_SU_2017_092': '13627_17_9_HE',
    'CRC_LN_SU_2017_093': '13627_17_10_HE',
    'CRC_LN_SU_2017_094': '15867_17_11_HE',
    'CRC_LN_SU_2017_095': '16026_17_15_HE',
    'CRC_LN_SU_2017_096': '16026_17_29_HE',
    'CRC_LN_SU_2017_097': '16114_17_II_7_HE',
    'CRC_LN_SU_2017_098': '16491_17_10_HE',
    'CRC_LN_SU_2017_099': '16491_17_12_HE',
    'CRC_LN_SU_2017_100': '18177_17_II_6_HE',
    'CRC_LN_SU_2017_101': '18269_17_7_HE',
    'CRC_LN_SU_2017_102': '18269_17_11_HE',
    'CRC_LN_SU_2017_103': '18269_17_13_HE',
    'CRC_LN_SU_2017_104': '18269_17_17_HE',
    'CRC_LN_SU_2017_105': '19044_17_I_11_HE',
    'CRC_LN_SU_2017_106': '19479_17_11_HE',
    'CRC_LN_SU_2017_107': '19479_17_12_HE',
    'CRC_LN_SU_2017_108': '19699_17_23_HE',
    'CRC_LN_SU_2017_109': '19699_17_25_HE',
    'CRC_LN_SU_2017_110': '19798_17_10_HE',
    'CRC_LN_SU_2018_01': '86_18_II_18_HE',
    'CRC_LN_SU_2018_02': '276_18_18_HE',
    'CRC_LN_SU_2018_03': '563_18_24_HE',
    'CRC_LN_SU_2018_04': '1791_18_11_HE',
    'CRC_LN_SU_2018_05': '2076_18_9_HE',
    'CRC_LN_SU_2018_06': '2142_18_9_HE',
    'CRC_LN_SU_2018_07': '2142_18_10_HE',
    'CRC_LN_SU_2018_08': '2450_18_7_HE',
    'CRC_LN_SU_2018_09': '2452_18_I_12_HE',
    'CRC_LN_SU_2018_10': '2452_18_I_14_HE',
    'CRC_LN_SU_2018_11': '2452_18_I_16_HE',
    'CRC_LN_SU_2018_12': '02667_18_14_HE',
    'CRC_LN_SU_2018_13': '02667_18_15_HE',
    'CRC_LN_SU_2018_14': '02667_18_17_HE',
    'CRC_LN_SU_2018_15': '02731_18_I_19_HE',
    'CRC_LN_SU_2018_16': '02731_18_I_20_HE',
    'CRC_LN_SU_2018_17': '3050_18_11_HE',
    'CRC_LN_SU_2018_18': '3050_18_12_HE',
    'CRC_LN_SU_2018_19': '3051_18_I_12',
    'CRC_LN_SU_2018_20': '3051_18_I_13',
    'CRC_LN_SU_2018_21': '3051_18_I_14',
    'CRC_LN_SU_2018_22': '3608_18_13_HE',
    'CRC_LN_SU_2018_23': '3774_18_9_HE',
    'CRC_LN_SU_2018_24': '3774_18_12_HE',
    'CRC_LN_SU_2018_25': '3774_18_21_HE',
    'CRC_LN_SU_2018_26': '4289_18_7_HE',
    'CRC_LN_SU_2018_27': '4717_18_I_16_HE',
    'CRC_LN_SU_2018_28': '4717_18_I_18_HE',
    'CRC_LN_SU_2018_29': '4717_18_I_19_HE',
    'CRC_LN_SU_2018_30': '6332_18_II_18_HE',
    'CRC_LN_SU_2018_31': '6727_18_14_HE',
    'CRC_LN_SU_2018_32': '6769_18_10_HE',
    'CRC_LN_SU_2018_33': '6769_18_11_HE',
    'CRC_LN_SU_2018_34': '6769_18_29_HE',
    'CRC_LN_SU_2018_35': '6928_18_13_HE',
    'CRC_LN_SU_2018_36': '6928_18_17_HE',
    'CRC_LN_SU_2018_37': '6937_18_16_HE',
    'CRC_LN_SU_2018_38': '7503_18_I_16_HE',
    'CRC_LN_SU_2018_39': '7944_18_10_HE',
    'CRC_LN_SU_2018_40': '7944_18_14_HE',
    'CRC_LN_SU_2018_41': '7944_18_16_HE',
    'CRC_LN_SU_2018_42': '8147_18_17_HE',
    'CRC_LN_SU_2018_43': '8984_18_6_HE',
    'CRC_LN_SU_2018_44': '10873_18_9_HE',
    'CRC_LN_SU_2018_45': '10873_18_11_HE',
    'CRC_LN_SU_2018_46': '13046_18_I_15',
    'CRC_LN_SU_2018_47': '13866_18_II_10'
}


def acquire_image_ids(image_metadata_path=os.getcwd() +
                      '/src/data/images.json'):

    id_to_karolinska = dict()

    with open(image_metadata_path, 'r') as read_file:
        images_metadata = json.load(read_file)
    for metadata in images_metadata:
        ID = int(metadata['id'])
        karolinska_name = metadata['filename'].split('/')[-1]
        id_to_karolinska[ID] = karolinska_name.replace('.mrxs', '')

    return id_to_karolinska


def acquire_annotation_ids(annotation_path=os.getcwd() +
                           '/src/data/annotations.dat'):

    image_id_to_annotations_ids = dict()

    with open(annotation_path, 'r') as read_file:
        for line in read_file.readlines():
            splitted_line = line.split('|')
            splitted_on_double_dot = [tag.split(':') for tag in splitted_line]
            image_id = int(splitted_on_double_dot[1][1].strip())
            image_id_to_annotations_ids[image_id] = []

    with open(annotation_path, 'r') as read_file:
        for line in read_file.readlines():
            splitted_line = line.split('|')
            splitted_on_double_dot = [tag.split(':') for tag in splitted_line]
            annotation_id = int(splitted_on_double_dot[0][1].strip())
            image_id = int(splitted_on_double_dot[1][1].strip())
            image_id_to_annotations_ids[image_id].append(annotation_id)

    return image_id_to_annotations_ids


def acquire_annotation_polygons(json_annotation_path=os.getcwd() +
                                '/src/data/user-annotation-collection.json'):

    annotation_id_to_polygon = dict()

    with open(json_annotation_path, 'r') as read_file:
        annotations_data = json.load(read_file)

    for annotation in annotations_data:
        ID = int(annotation['id'])
        if 'MULTIPOLYGON' not in annotation['location']:
            polygon = annotation['location'].replace('POLYGON ((', '').replace(
                '))', '').replace(',', '').replace(')',
                                                   '').replace('(',
                                                               '').split(' ')
            polygon = list(map(round, map(float, polygon)))
            annotation_id_to_polygon[ID] = [polygon]
        else:
            polygons_ = annotation['location'].replace('MULTIPOLYGON (((',
                                                       '').split(')), ((')
            polygons = []
            for ind, polygon in enumerate(polygons_):
                polygon = polygon.replace(')))', '').replace(')', '').replace(
                    '(', '').replace(',', '').split(' ')
                polygon = list(map(round, map(float, polygon)))
                polygons.append(polygon)
            annotation_id_to_polygon[ID] = polygons

    return annotation_id_to_polygon


def acquire_terms(json_term_path=os.getcwd() +
                  '/src/data/term-collection.json'):

    term_id_to_label = dict()

    with open(json_term_path, 'r') as read_file:
        term_data = json.load(read_file)
    for term in term_data:
        ID = int(term['id'])
        label = term['name'].lower()
        term_id_to_label[ID] = label

    return term_id_to_label


def acquire_annotation_id_to_term_id(
        json_annotation_path=os.getcwd() +
        '/src/data/user-annotation-collection.json'):

    annotation_id_to_terms = dict()

    with open(json_annotation_path, 'r') as read_file:
        annotation_data = json.load(read_file)
    for annotation in annotation_data:
        ID = int(annotation['id'])
        terms = annotation['term']
        annotation_id_to_terms[ID] = terms

    return annotation_id_to_terms


def acquire_annotations(json_annotation_path=os.getcwd() +
                        '/src/data/user-annotation-collection.json'):

    id_to_karolinska = acquire_image_ids()
    image_id_to_annotation_ids = acquire_annotation_ids()
    term_id_to_label = acquire_terms()

    annotation_id_to_polygon = acquire_annotation_polygons()
    annotation_id_to_term_ids = acquire_annotation_id_to_term_id()

    elte_with_polygon_meta_data = dict()

    for elte_name in karolinska_to_elte.values():
        elte_with_polygon_meta_data[elte_name] = dict()

    for image_id in image_id_to_annotation_ids.keys():
        polygon_metadata = dict()
        for annotation_id in image_id_to_annotation_ids[image_id]:
            try:
                karolinska_name = id_to_karolinska[image_id]
            except KeyError:
                print('\nKeyErrror : ', image_id, '\n')
                continue
            elte_name = karolinska_to_elte[karolinska_name]
            polygons = annotation_id_to_polygon[annotation_id]
            term_ids = annotation_id_to_term_ids[annotation_id]
            if len(polygons) > 0 and len(term_ids) == 0:
                print(
                    '\n# of terms should not be zero if polygons are present!')
                print(karolinska_name, elte_name, annotation_id, len(polygons),
                      len(term_ids), '\n')
                continue
            labels = [term_id_to_label[t_id] for t_id in term_ids]
            if len(labels) < len(polygons) and len(labels) == 1:
                labels = [labels[0]] * len(polygons)
            if len(polygons) < len(labels) and len(polygons) == 1:
                polygons = [polygons[0]] * len(labels)
                print('\n', elte_name,
                      ' has multi-labeled polygon with labels ', labels, '\n')
            for lab in labels:
                polygon_metadata[lab] = []
            for ind, lab in enumerate(labels):
                polygon_metadata[lab].append(polygons[ind])
        try:
            karolinska_name = id_to_karolinska[image_id]
            elte_name = karolinska_to_elte[karolinska_name]
            elte_with_polygon_meta_data[elte_name] = polygon_metadata
        except KeyError:
            continue

    return elte_with_polygon_meta_data