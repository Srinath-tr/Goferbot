import os

fpath = 'G:\Python27\Faces\gos1'
if not os.path.exists(fpath):
    os.makedirs(fpath)
else:
    print 'folder already exists in this path'
