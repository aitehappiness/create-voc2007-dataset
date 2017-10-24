# labelx2voc
## 转换labelx json数据格式为voc格式

## Usage
### input format
labelx jsonlist file
### output format
same with voc(2007/2012) datasets
```
<vocdirname>
├── Annotations
│   ├── 000000.xml
│   ├── 000001.xml
│   ├── 000002.xml
│   └── ...
├── ImageSets
│   ├── Main
│   │   ├── test.txt
│   │   ├── train.txt
│   │   ├── trainval.txt
│   │   └── val.txt
├── JPEGImages
│   ├── 000000.jpg
│   ├── 000001.jpg
│   ├── 000002.jpg
│   └── ...
```


### step 1
```python
cd <labelx2voc>/cvt2voc

python cvt2labelbyline.py jsonlist_file
```


### step 2
```python
cd <labelx2voc>/cvt2voc

python labelbyline2xml.py --classmap <test.classmap> --vocpath <vocpath> --labelbyline <labelbyline_file>
```

### step 3
```python
cd <labelx2voc>/cvt2voc

python gen_imagesets.py
```