# -*- coding:utf-8 -*-
import os
from word_renderer import WordRenderer, FontState, ColourState, RandomCorpus, FillImageState
from PIL import Image
import numpy as n
from multiprocessing import Process, Queue, Pool
import time

def gen_one(WR,folder_id):
    QUALITY = [80, 10]
    num_in_folder=0
    while True:
        data = WR.generate_sample(substring_crop=0, random_crop=True, char_annotations=True)
        if data is not None:
            folder='gen/'+'{:03d}/'.format(folder_id)
            if not os.path.exists(folder):
                os.makedirs(folder)
            quality = min(80, max(0, int(QUALITY[1] * n.random.randn() + QUALITY[0])))
            img = Image.fromarray(data['image'])
            if img.mode != 'RGB':
                img = img.convert('RGB')
            imfn = 'gen/'+'{:03d}/'.format(folder_id)+'{:03d}_'.format(num_in_folder)+data['text']+'.jpg'
            img.save(imfn, 'JPEG', quality=quality)
            img.close()
            num_in_folder += 1
            if num_in_folder==1000:
                break
    return

def gen(WR,processes=10):
    start_time = time.time()
    pool = Pool(processes)
    for i in range(0,1000):
        pool.apply_async(gen_one, (WR, i))
    pool.close()
    pool.join()
    end_time = time.time()
    print('用时:%s秒' % (end_time - start_time))



if __name__ == "__main__":

    fillimstate = FillImageState()
    fs = FontState()
    corpus = RandomCorpus({'min_length': 1, 'max_length': 10})
    # init renderer
    sz = (800, 200)
    WR = WordRenderer(sz=sz, fontstate=fs, corpus=corpus,colourstate=ColourState, fillimstate=fillimstate)

    gen(WR, processes=10)
    print('finished')
    '''
    start_time = time.time()
    QUALITY = [80, 10]
    folder_id = 0
    num_in_folder = 0
    while True:
        data = WR.generate_sample(substring_crop=0, random_crop=True, char_annotations=True)
        if data is not None:
            folder='gen/'+'{:03d}/'.format(folder_id)
            if not os.path.exists(folder):
                os.makedirs(folder)
            quality = min(80, max(0, int(QUALITY[1] * n.random.randn() + QUALITY[0])))
            img = Image.fromarray(data['image'])
            if img.mode != 'RGB':
                img = img.convert('RGB')
            imfn = 'gen/'+'{:03d}/'.format(folder_id)+'{:03d}_'.format(num_in_folder)+data['text']+'.jpg'
            img.save(imfn, 'JPEG', quality=quality)
            img.close()
            num_in_folder += 1
            if num_in_folder==20:
                folder_id +=1
                num_in_folder=0
            if folder_id==10:
                break
    end_time = time.time()
    print('用时:%s秒' % (end_time - start_time))
    '''
