NodalIdentity
=============

Inspired by MIT Media Lab identity this project was created. This software creates visual represtation for each node in a tree-like dataset while being aestheticaly pleasing. Each visual representaiton will carry full information about the node position in the dataset and comparison between nodal representations will reveal inter-relationship sbetween the nodes inside the tree-like dataset.

The program
-----------
It's yet to be integrated, the software is written in two parts. One part is in Python, and the other part is written with Processing. The end rendering part is done with Processing and the parsing of data in term of the visual representation is done in Python. The Python program accepts the data in CSV tabular format.

Such as,
```
Slytherin, Sophomore
Gryffindor, Senior, Ron Weasley
Gryffindor, Senior, Harry Potter
Gryffindor
```

In the CSV data format, each line corresponds to a node. And nodes can have arbitrary depths, which will be reflected in the final rendition. Such as, one can have single image for Gyrffindor house, and also have Gryffindor Seniors as another different image with similarities. And each node will have an unique image.

The Python program should be ran first followed by the Processing Sketch.

The python program ```parser.py``` will generate a few files. In the ```ID_plotter``` folder there will ```data.txt``` and ```params.txt```. Both will be used by the Processing sketch to generate the image later in a ```Images/``` folder. There will be another file generated, named ```names.txt```. This file will contain the same information as the data file. The line numbers of this file will correspond to the ```image*.png``` in the ```/Images``` folder.

Instructions
------------
The Python program asks for the data file filename. One can simply press ENTER and let the sample dataset work. There is also Python program to generate a sample data-set with all possible combinations. Then one has to run the Processing sketch.

Requirements
------------
Python 2.7.1 or higher
Processing 2.0b1 or higher (One can simply change a single line (Line 39) in the Processing sketch to make in compatible with Processing 1.5). The change is to remove the last argument from the ```rect()``` function.

TODO
----
1. Add accomodation feature for adding more entities in the future while preserving the old map.
2. Integrating both programs.
3. Add browser based GUI.

Feel free to fork and hack the code. It's not well commented yet.

A detailed blog post will be available soon.