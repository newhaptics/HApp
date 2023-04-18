# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:22:45 2023

@author: Derek Joslin

"""


from GraphicsEngine import *
import TactileDisplay as td
import Features as f
import numpy as np
import math

display = td.TactileDisplay("test")
display.connect("COM3")
engine = GraphicsEngine((display.com.nColumns, display.com.nRows))

engine.addLine((0,0), (display.com.nColumns, display.com.nRows), 3)

engine.drawFeatures()
engine.showImage()
toState = engine.retrieveList()
display.set_desiredState(toState)
display.push_desiredState()
# =============================================================================
# # Calculate and add points for the sinusoidal wave with a 90-degree phase shift and decreased amplitude
# wave_points = []
# amplitude = 4  # Decrease the amplitude from 8 to 4
# for x in range(83):
#     y = 9.5 + amplitude * math.sin(4 * math.pi * x / 83 + math.pi / 2)  # Phase shift by 90 degrees
#     wave_points.append((x, y))
#     engine.addPoint((x, y))
# 
# # Draw the axes
# x_axis_start = (0, 9.5)
# x_axis_end = (83, 9.5)
# y_axis_start = (0, 0)
# y_axis_end = (0, 19)
# engine.addLine(x_axis_start, x_axis_end, 1)
# engine.addLine(y_axis_start, y_axis_end, 1)
# =============================================================================
# =============================================================================
# # Calculate and add points for the sinusoidal wave
# wave_points = []
# for x in range(83):
#     y = 9.5 + 8 * math.sin(2 * math.pi * x / 83)
#     wave_points.append((x, y))
#     engine.addPoint((x, y))
# 
# # Draw the axes
# x_axis_start = (0, 9.5)
# x_axis_end = (83, 9.5)
# y_axis_start = (0, 0)
# y_axis_end = (0, 19)
# engine.addLine(x_axis_start, x_axis_end, 1)
# engine.addLine(y_axis_start, y_axis_end, 1)
# =============================================================================


# =============================================================================
# # Calculate and add points for the sinusoidal wave with doubled frequency
# wave_points = []
# for x in range(83):
#     y = 9.5 + 8 * math.sin(4 * math.pi * x / 83)  # Multiply 2 * math.pi by 2 to double the frequency
#     wave_points.append((x, y))
#     engine.addPoint((x, y))
# 
# # Draw the axes
# x_axis_start = (0, 9.5)
# x_axis_end = (83, 9.5)
# y_axis_start = (0, 0)
# y_axis_end = (0, 19)
# engine.addLine(x_axis_start, x_axis_end, 1)
# engine.addLine(y_axis_start, y_axis_end, 1)
# =============================================================================

# Add labels for the axes (assuming addText method is implemented in the GraphicsEngine class)
# =============================================================================
# engine.addText((83, 9), "x")
# engine.addText((0, 0), "y")
# 
# =============================================================================
# =============================================================================
# # Draw the Tetris game board
# board_start = (1, 1)
# board_end = (81, 18)
# engine.addRectangle(board_start, board_end, 1)
# 
# # Add Tetris blocks
# # Block 1: T-shape
# block1 = [(11, 1), (11, 3), (13, 3), (15, 3), (15, 1)]
# engine.addPolygon(block1, 1)
# 
# # Block 2: L-shape
# block2 = [(21, 1), (21, 5), (23, 5), (23, 3), (25, 3), (25, 1)]
# engine.addPolygon(block2, 1)
# 
# # Block 3: S-shape
# block3 = [(31, 1), (31, 3), (33, 3), (33, 5), (35, 5), (35, 3), (37, 3), (37, 1)]
# engine.addPolygon(block3, 1)
# 
# # Block 4: O-shape
# block4 = [(41, 1), (41, 3), (43, 3), (43, 1)]
# engine.addPolygon(block4, 1)
# 
# # Block 5: I-shape
# block5 = [(51, 1), (51, 5), (53, 5), (53, 1)]
# engine.addPolygon(block5, 1)
# 
# =============================================================================

# =============================================================================
# #engine.addLine((0,0), (83,19), 3)
# # Head
# head_center = (41, 4)
# head_radius = 3
# engine.addCircle(head_center, head_radius, 1)
# 
# # Eyes
# left_eye_center = (39, 3)
# left_eye_radius = 0.5
# engine.addCircle(left_eye_center, left_eye_radius, 1)
# 
# right_eye_center = (43, 3)
# right_eye_radius = 0.5
# engine.addCircle(right_eye_center, right_eye_radius, 1)
# 
# # Mouth
# mouth_start = (39, 5)
# mouth_end = (43, 5)
# engine.addLine(mouth_start, mouth_end, 1)
# 
# # Body
# body_start = (41, 7)
# body_end = (41, 12)
# engine.addLine(body_start, body_end, 1)
# 
# # Left arm
# left_arm_start = (41, 9)
# left_arm_end = (37, 11)
# engine.addLine(left_arm_start, left_arm_end, 1)
# 
# # Right arm
# right_arm_start = (41, 9)
# right_arm_end = (45, 11)
# engine.addLine(right_arm_start, right_arm_end, 1)
# 
# # Left leg
# left_leg_start = (41, 12)
# left_leg_end = (37, 18)
# engine.addLine(left_leg_start, left_leg_end, 1)
# 
# # Right leg
# right_leg_start = (41, 12)
# right_leg_end = (45, 18)
# engine.addLine(right_leg_start, right_leg_end, 1)
# =============================================================================


#engine.showImage()