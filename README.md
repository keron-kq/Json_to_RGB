# Json_to_RGB
Convert Json file to RGB trainable file
The json_to_dataset.py file that comes with labelme can only convert a single json file at a time, which is very troublesome to use for large samples. Since the training process uses a lot of original images and label images, a polyline is drawn based on the location information and label category of the label points in the json file, and the internal area of ​​the polyline is filled with the same color as the polyline to generate a label image.
However, a Unicode decoding error occurred when trying to load the JSON file. This may be because the characters contained in the JSON file cannot be decoded using the default GB2312 or GBK encoding, so the JSON file is specified to be opened in UTF-8 encoding. The specific code is as follows. You can understand the libraries and functions used by yourself. It is relatively simple and can be modified if you have further requirements.

Polyline fills use the draw.polygon method which is used to draw the filled area.
