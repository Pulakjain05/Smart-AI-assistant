# Door_and_handles
Door and Door Handle Dataset For Object Detection is a dataset that contains 1334 images of various doors and their respective handles.

(The images and their annotations are provided in this repository. Annotation and labeling was done via Roboflow)

# 1- Sample Images
The images were taken from UAEU's campus to include the variations of door structures (Glass Doors, Wooden Doors, ... etc), in addition to the variation of door handles.

https://user-images.githubusercontent.com/117348725/205496253-26556230-cdcd-4b4e-9c19-52ce13935ebf.jpg

https://user-images.githubusercontent.com/117348725/205496278-c23522b4-2e78-4243-b2b6-4b9293b8ab52.jpg

https://user-images.githubusercontent.com/117348725/205496285-2b5397de-dc77-42ee-bfcc-5c8d5111ddfc.jpg

In addition to using images from the repositories:

1- https://github.com/MiguelARD/DoorDetect-Dataset (Cleaned from fridges and cabinets images, with tighter bounding boxes to doors and their handles)

2- https://github.com/Joechencc/Handle_detection (Used images of the training data)

# 2- Dataset Labels
The labels we are interested in detecting are: door, handle.

Annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:

* Auto-orientation of pixel data (with EXIF-orientation stripping)

and no image augmentation techniques were applied.


The object location is specified by the coordinates of its bounding box. Boxes were marked using Yolo_mark. 
In the train, test, and valid files, there will be images and labels files where there is a .txt file for each image under the same name.


# 3- Dataset Usage
This dataset of door images is completely annotated with proper bouding boxes to enable training for object detection models such as Yolo.
