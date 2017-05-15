# word-render
- word renderer to generate training data for text recognition
- using pygame to render the image
- multi-threads to accerate

## requirement
- numpy
- PIL
- pygame
recommend to install Anaconda

## usage
```shell
python generate.py
```
Also. you can change the threads you wants in generate.py, default is 10 
this will generate a image with 18 characters, includeing 0~9 and X 
which is the character used in id card number in china. 

## demo image
![img](/gen/000/000_50859213323710528X.jpg)


