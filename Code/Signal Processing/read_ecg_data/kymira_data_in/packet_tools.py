"""
Handles the marshaling of ECG data to and from the database.

"""
import zlib
import json
from numpyencoder import NumpyEncoder
from base64 import b64decode, b64encode


def compress_samples(packed_dict):
    packet_str = json.dumps(packed_dict, cls=NumpyEncoder)
    encoded_str = packet_str.encode('utf-8')
    compressed_str = zlib.compress(encoded_str)
    out_b64 = b64encode(compressed_str)
    return out_b64.decode('ascii')


def uncompress_samples(b64_str):
    try:
        compressed_str = b64decode(b64_str)
        encoded_str = zlib.decompress(compressed_str)
        packed_dict = json.loads(encoded_str)
    except Exception as e:
        print(e)
    else:
        return packed_dict


def packed_dict_to_list(packed_dict):
    list_samples = []
    list_keys = list(packed_dict.keys())
    if (type(packed_dict[list_keys[0]]) == str):
        for key in list_keys:
            packed_dict[key] = json.loads(packed_dict[key])
    num_samples = len(list(packed_dict.values())[0])

    for i in range(0, num_samples):
        sample = {}
        for key in list_keys:
            sample[key] = packed_dict[key][i]
        list_samples += [sample]

    return list_samples


def list_to_packed_dict(input_list):
    packed_dict = {}
    for key in input_list[0].keys():
        packed_dict[key] = []

    for sample in input_list:
        for key in sample.keys():
            packed_dict[key] += [float("{0:.4g}".format(sample[key]))]
    return packed_dict
