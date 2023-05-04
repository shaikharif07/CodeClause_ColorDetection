#  CodeClause_Color_Detection

Name of Project- Color Detection from an image

Description- How many times has it occurred to you that even after seeing you don't remember the name of the color? There can be 16 million colors based on the different RGB color values but we only remember a few. So in this project we are going to build an interactive app that will detect the selected color from any image. To implement this we will need a labeled data of all the known colors then we will calculate which color resembles the most with the selected color value.

Programming Languages- Python

Dataset- https://www.kaggle.com/datasets/adityabhndari/color-detection-data-set

Approch-
A csv file with labeled data(865 colors and their RGB value) is provided along with a sample image with mutiple colors as the algorithm used in the project is a distance-based matching algorithm, where the distance between the RGB values of the selected pixel and the RGB values of each color in the CSV file is calculated using the sum of absolute differences (SAD) of the three color channels (Red, Green, and Blue). The color name corresponding to the color with the smallest SAD is then returned as the detected color.



