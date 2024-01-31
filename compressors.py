# Compressor Framework
import gzip
import bz2
import lzma
# from PIL.PngImagePlugin import getchunks
# from PIL import Image
import sys
from tqdm import tqdm
import torch.nn.functional as F


import io


class DefaultCompressor:
    """for non-neural-based compressor"""
    def __init__(self, compressor, typ='text'):
        if compressor == 'gzip':
            self.compressor = gzip
        elif compressor == 'bz2':
            self.compressor = bz2
        elif compressor == 'lzma':
            self.compressor = lzma
        else:
            raise RuntimeError("Unsupported compressor")
        self.type = typ
    def get_compressed_len(self, x):
        if self.type == 'text':
            print("Encoded Sequence:")
            print(x.encode('utf-8'))
            print("Another Encoded Sequence form:")
            encoded_seq = x.encode('utf-8')
            print(encoded_seq.decode('utf-8'))
            print("Compressed Sequence:")
            print(self.compressor.compress(x.encode('utf-8')))
            return len(self.compressor.compress(x.encode('utf-8')))
        else:
            print("encoded bytes:")
            print(np.array(x).tobytes())
            print("Compressed byte Sequence:")
            print(self.compressor.compress(np.array(x).tobytes()))
            return len(self.compressor.compress(np.array(x).tobytes()))
    def get_bits_per_char(self, original_fn):
        with open(original_fn) as fo:
            data = fo.read()
            print("Encoded Sequence:")
            print(data.encode('utf-8'))
            compressed_str = self.compressor.compress(data.encode('utf-8'))
            print("Compressed Sequence:")
            print(compressed_str)
            return len(compressed_str)*8/len(data)



"""Test Compressors"""
# comp = DefaultCompressor('gzip')
# print(comp.get_compressed_len('Hello world'))
