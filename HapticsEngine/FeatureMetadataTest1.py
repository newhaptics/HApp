# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 17:34:50 2023

@author: Derek Joslin

"""
from FeatureMetadata import *
import numpy as np

# Instantiate the FeatureMetadata object
feature_metadata = FeatureMetadata()

# Add a point
feature_metadata.addPoint((1, 1))

# Add a line
feature_metadata.addLine((0, 0), (5, 5), 2)

# Add a curve
feature_metadata.addCurve([(1, 2), (3, 4), (5, 6)], 2)

# Add a triangle
feature_metadata.addTriangle([(0, 0), (1, 1), (0, 1)], 1)

# Add a circle
feature_metadata.addCircle((5, 5), 3, 1)

# Add an ellipse
feature_metadata.addEllipse((10, 10), 5, 3, 0, 1)

# Add an arc
feature_metadata.addArc((15, 15), 5, 0, np.pi, 1)

# Add a polygon
feature_metadata.addPolygon([(2, 2), (4, 2), (4, 4), (2, 4)], 1)

# Add a rectangle
feature_metadata.addRectangle((6, 6), (8, 8), 1)

# Add a quadrilateral
feature_metadata.addQuadrilateral([(10, 10), (12, 10), (12, 12), (10, 12)], 1)

# Print initial featuresMetadata
print("Initial featuresMetadata:")
for feature_id, feature in feature_metadata.featuresMetadata.items():
    print(f"{feature_id}: {feature.type}")

# Sort features by width in descending order
feature_metadata.sortFeatures('width', ascending=False)

# Print featuresMetadata after sorting
print("\nFeaturesMetadata after sorting by width (descending):")
for feature_id, feature in feature_metadata.featuresMetadata.items():
    print(f"{feature_id}: {feature.type} (width: {feature.width})")

# Update the width of a feature
feature_id_to_update = list(feature_metadata.featuresMetadata.keys())[0]
feature_metadata.updateFeature(feature_id_to_update, {"width": 5})

# Print featuresMetadata after updating a feature
print("\nFeaturesMetadata after updating a feature:")
for feature_id, feature in feature_metadata.featuresMetadata.items():
    print(f"{feature_id}: {feature.type} (width: {feature.width})")