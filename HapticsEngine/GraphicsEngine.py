# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:18:00 2020

@author: Derek Joslin

"""

""" this is the new graphics engine which performs operations on a matrix and changes the values inside """

import numpy as np
import cairo
import Brailler as br
import FeatureMetadata as fm
from PIL import Image
import math

class GraphicsEngine(fm.FeatureMetadata):
    def __init__(self, dimensions):
        super().__init__()
        self.dimensions = dimensions

        # round to nearest 20 multiple because cairo likes multiples of 20 for some reason
        self.cairoDimensions = (20*math.ceil(self.dimensions[0]/20), 20*math.ceil(self.dimensions[1]/20))

    def drawFeatures(self):
        self.img = cairo.ImageSurface(cairo.FORMAT_A8, self.cairoDimensions[0], self.cairoDimensions[1])
        self.ctx = cairo.Context(self.img)
        # Iterate through the features_metadata and draw each feature
        for featureId, featureMetadata in self.featuresMetadata.items():
            featureMetadata._drawFeature(self.ctx)

        # Update the matrix with the drawn features
        buf = self.img.get_data()
        self.matrix = np.ndarray(shape=(self.cairoDimensions[1], self.cairoDimensions[0]), dtype=np.uint8, buffer=buf)

    def retrieveList(self):
        subMatrix = self.matrix[0:self.dimensions[1], 0:self.dimensions[0]]
        return subMatrix.tolist()
        
    def showImage(self):
        # Display the image using the PIL Image.show() method
        self.img = Image.fromarray(self.matrix)
        self.img.show()