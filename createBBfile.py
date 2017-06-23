import os
import csv

""" Convert the notations form the following datasets to be used with Keras-frcnn in the simple data reader mode
the 3D bounding boxes form VehicleReI dinto a front and a back bounding box. """

PATH_VEHICLEREID = "/disk/ml/datasets/VehicleReId/"
PATH_CITYSCAPES = "/disk/ml/datasets/cityscapes/"
PATH_BOXCARS = "/disk/ml/datasets/BoxCars21k/"

OUTPUT_FILE = "Output/mergedBB.txt"
with open(OUTPUT_FILE) as outfile:
    fieldnames = ["filepath", "x1", "y1", "x2", "y2", "class_name"]
    csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',')
#   csvwriter = csv.DictWriter(outfile, delimiter=',')
    csvwriter.writeheader()
    for shot_name in ["1A", "1B", "2A", "2B", "3A", "3B", "4A", "4B", "5A", "5B"]:
        with open(PATH_VEHICLEREID + shot_name, 'rb') as file:
            csvreader = csv.reader(file, delimiter=',')
            for line in csvreader:
                (carid, frame,
                 upperPointShort_x, upperPointShort_y,
                 upperPointCorner_x, upperPointCorner_y,
                 upperPointLong_x, upperPointLong_y,
                 crossCorner_x, crossCorner_y,
                 shortSide_x, shortSide_y,
                 corner_x, corner_y,
                 longSide_x, longSide_y,
                 lowerCrossCorner_x, lowerCrossCorner_y) = line
                outfile.writerow({
                    "filepath": shot_name + "__" + "%05d"% frame + ".jpg",
                    "x1":
                                  })
