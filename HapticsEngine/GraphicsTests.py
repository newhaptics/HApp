# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:02:53 2023

@author: Derek Joslin

"""

from GraphicsEngine import *
import Features as f
import numpy as np

icon_engine = GraphicsEngine((83, 19))
        
icon_engine.addFeature(f.VerticalScrollbar((0,0),12))

icon_engine.addFeature(f.HorizontalScrollbar((0,17),50))



for i in range(0,20):
    list(icon_engine.featuresMetadata.values())[0].setPosition(0.05*i)
    list(icon_engine.featuresMetadata.values())[1].setPosition(0.05*i)
    icon_engine.drawFeatures()   
    mat = icon_engine.retrieveList()
    print("num: {}".format(i))
    print('---------------------------\n')
    print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
                     for row in icon_engine.retrieveList()]))
    print('---------------------------\n')
    
    
# =============================================================================
# class LeftDiagonalScrollbar(f.Polygon):
#     def __init__(self, startPoint):
#         width = 2
#         height = 12
#         vertices = [
#             startPoint,
#             (startPoint[0] + width, startPoint[1]),
#             (startPoint[0], startPoint[1] + height),
#             (startPoint[0] - width, startPoint[1] + height)
#         ]
#         super().__init__(vertices, 1)
#         self.type = "left_diagonal_scrollbar"
# 
# class RightDiagonalScrollbar(f.Polygon):
#     def __init__(self, startPoint):
#         width = 2
#         height = 12
#         vertices = [
#             startPoint,
#             (startPoint[0] + width, startPoint[1]),
#             (startPoint[0] + width * 2, startPoint[1] + height),
#             (startPoint[0] + width, startPoint[1] + height)
#         ]
#         super().__init__(vertices, 1)
#         self.type = "right_diagonal_scrollbar"
# 
# class RoundedRectangleScrollbar(f.Feature):
#     def __init__(self, startPoint):
#         super().__init__(1)
#         self.startPoint = startPoint
#         self.width = 2
#         self.height = 12
#         self.type = "rounded_rectangle_scrollbar"
# 
#     def _drawFeature(self, ctx):
#         x1, y1 = self.startPoint
#         x2, y2 = x1 + self.width, y1 + self.height
#         radius = 1
# 
#         ctx.set_line_width(self.width)
#         ctx.arc(x1 + radius, y1 + radius, radius, np.pi, 3 * np.pi / 2)
#         ctx.arc(x2 - radius, y1 + radius, radius, 3 * np.pi / 2, 2 * np.pi)
#         ctx.arc(x2 - radius, y2 - radius, radius, 0, np.pi / 2)
#         ctx.arc(x1 + radius, y2 - radius, radius, np.pi / 2, np.pi)
#         ctx.close_path()
#         ctx.stroke()
# =============================================================================

# =============================================================================
# class ScrollBarDesign1(f.Feature):
#     def __init__(self, width):
#         super().__init__(width)
#         self.type = "scroll_bar_design_1"
#         
#     def _drawFeature(self, ctx):
#         pattern = [
#             [1, 0, 0, 1],
#             [0, 1, 1, 0],
#             [1, 0, 0, 1],
#             [0, 1, 1, 0],
#             [1, 0, 0, 1],
#             [0, 1, 1, 0],
#             [1, 0, 0, 1],
#             [0, 1, 1, 0],
#             [1, 0, 0, 1],
#             [0, 1, 1, 0],
#             [1, 0, 0, 1],
#             [0, 1, 1, 0]
#         ]
#         ctx.set_line_width(self.width)
#         for y, row in enumerate(pattern):
#             for x, cell in enumerate(row):
#                 if cell:
#                     ctx.rectangle(x, y, 1, 1)
#         ctx.stroke()
# =============================================================================

# =============================================================================
# class ScrollBarDesign2(f.Feature):
#     def __init__(self, width):
#         super().__init__(width)
#         self.type = "scroll_bar_design_2"
#         
#     def _drawFeature(self, ctx):
#         pattern = [
#             [1, 1, 1, 1],
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [1, 0, 0, 1],
#             [1, 1, 1, 1],
#             [1, 0, 0, 1]
#         ]
#         ctx.set_line_width(self.width)
#         for y, row in enumerate(pattern):
#             for x, cell in enumerate(row):
#                 if cell:
#                     ctx.rectangle(x, y, 1, 1)
#         ctx.stroke()
# 
# class ScrollBarDesign3(f.Feature):
#     def __init__(self, width):
#         super().__init__(width)
#         self.type = "scroll_bar_design_3"
#         
#     def _drawFeature(self, ctx):
#         pattern = [
#             [1, 1, 1, 1],
#             [1, 1, 1, 1],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [0, 1, 1, 0],
#             [1, 1, 1, 1],
#             [1, 1, 1, 1]
#         ]
#         ctx.set_line_width(self.width)
#         for y, row in enumerate(pattern):
# =============================================================================



# =============================================================================
# icon_engine = GraphicsEngine((60, 20))
# 
# def create_icon1():
#     icon_engine.addLine((1, 1), (2, 2), 1)
#     icon_engine.drawFeatures()
# 
# #create_icon1()
# 
# def create_icon2():
#     icon_engine.addPoint((1, 1))
#     icon_engine.addPoint((2, 2))
#     icon_engine.drawFeatures()
# 
# #create_icon2()
# 
# def create_icon3():
#     icon_engine.addLine((0, 0), (3, 0), 1)
#     icon_engine.addLine((3, 0), (3, 2), 1)
#     icon_engine.drawFeatures()
# 
# #create_icon3()
# 
# def create_icon4():
#     icon_engine.addRectangle((0, 0), (3, 2), 1)
#     icon_engine.drawFeatures()
# 
# #create_icon4()
# 
# def create_icon5():
#     icon_engine.addLine((1, 0), (0, 2), 1)
#     icon_engine.addLine((1, 0), (3, 2), 1)
#     icon_engine.drawFeatures()
# 
# #create_icon5()
# 
# def create_icon6():
#     icon_engine.addLine((0, 0), (3, 2), 1)
#     icon_engine.addLine((3, 0), (0, 2), 1)
#     icon_engine.drawFeatures()
# 
# #create_icon6()
# 
# def create_icon7():
#     icon_engine.addTriangle([(0, 0), (3, 0), (1, 2)], 1)
#     icon_engine.drawFeatures()
# 
# #create_icon7()
# 
# def create_icon8():
#     icon_engine.addArc((1, 1), 1, 0, 180, 1)
#     icon_engine.drawFeatures()
# 
# #create_icon8()
# 
# def create_icon9():
#     icon_engine.addEllipse((1, 1), 1, 0.5, 45, 1)
#     icon_engine.drawFeatures()
# 
# #create_icon9()
# 
# def create_icon10():
#     icon_engine.addCircle((1, 1), 1, 1)
#     icon_engine.drawFeatures()
# 
# #create_icon10()
# 
# # Example usage:
# create_icon6()
# icon_engine.showImage()
# 
# =============================================================================



# =============================================================================
# def draw_cursor(cursor_num):
#     engine = GraphicsEngine((60, 20))
# 
#     if cursor_num == 1:
#         # Arrow
#         engine.addPolygon([(1, 19), (19, 1), (11, 9), (1, 19)], 1)
#     elif cursor_num == 2:
#         # Crosshair
#         engine.addLine((10, 10), (50, 10), 1)
#         engine.addLine((30, 0), (30, 20), 1)
#     elif cursor_num == 3:
#         # Hand
#         engine.addPolygon([(5, 10), (5, 19), (55, 19), (55, 10), (35, 5)], 1)
#         engine.addCircle((5, 10), 5, 1)
#     elif cursor_num == 4:
#         # I-beam
#         engine.addRectangle((25, 0), (35, 20), 1)
#         engine.addLine((10, 0), (50, 0), 1)
#         engine.addLine((10, 20), (50, 20), 1)
#     elif cursor_num == 5:
#         # Hourglass
#         engine.addTriangle([(10, 0), (30, 10), (50, 0)], 1)
#         engine.addTriangle([(10, 20), (30, 10), (50, 20)], 1)
#     elif cursor_num == 6:
#         # Magnifying glass
#         engine.addCircle((15, 15), 9, 1)
#         engine.addLine((20, 20), (40, 0), 1)
#     elif cursor_num == 7:
#         # Four-pointed star
#         engine.addPolygon([(30, 0), (40, 20), (30, 10), (20, 20)], 1)
#     elif cursor_num == 8:
#         # Double-headed arrow
#         engine.addPolygon([(1, 19), (19, 1), (11, 9), (1, 19)], 1)
#         engine.addPolygon([(59, 1), (41, 19), (49, 11), (59, 1)], 1)
#     elif cursor_num == 9:
#         # Circle with a dot in the center
#         engine.addCircle((30, 10), 9, 1)
#         engine.addCircle((30, 10), 1, 1)
#     elif cursor_num == 10:
#         # Diamond
#         engine.addPolygon([(30, 0), (60, 10), (30, 20), (0, 10)], 1)
# 
#     engine.drawFeatures()
#     engine.showImage()
# 
# for i in range(1, 11):
#     draw_cursor(i)
# =============================================================================

# =============================================================================
# # Initialize the GraphicsEngine
# engine = GraphicsEngine((600, 200))
# 
# # Draw app icons (represented as circles)
# app_radius = 20
# app_spacing = 60
# app_y = 60
# 
# for i in range(5):
#     app_center = (30 + i * app_spacing, app_y)
#     engine.addCircle(app_center, app_radius, 2)
# 
# # Draw a scroll bar on the right-hand side
# scroll_bar_start = (580, 10)
# scroll_bar_end = (590, 190)
# engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
# 
# # Draw a context menu at the bottom
# menu_height = 20
# menu_start = (0, 180)
# menu_end = (600, 200)
# engine.addRectangle(menu_start, menu_end, 2)
# 
# # Draw buttons in the context menu
# button_width = 60
# button_spacing = 10
# 
# for i in range(5):
#     button_start = (10 + i * (button_width + button_spacing), 183)
#     button_end = (button_start[0] + button_width, 197)
#     engine.addRectangle(button_start, button_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# 
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((100, 20))
# 
# # Background
# for i in range(5):
#     vertices = [(20 * i, 20), (10 + 20 * i, 0), (20 + 20 * i, 20)]
#     engine.addTriangle(vertices, 1)
# 
# # Loading progress
# for i in range(3):
#     vertices = [(20 * i, 20), (10 + 20 * i, 0), (20 + 20 * i, 20)]
#     engine.addTriangle(vertices, 6)
# 
# engine.drawFeatures()
# engine.showImage()
# 
# =============================================================================

# =============================================================================
# import os
# 
# def draw_scrollbar(engine, thumb_position, x_offset):
#     scroll_bar_width = 20
#     scroll_bar_start = (x_offset, icon_margin)
#     scroll_bar_end = (x_offset + scroll_bar_width, 200 - icon_margin)
#     thumb_height = 30
#     thumb_start = (x_offset, thumb_position)
#     thumb_end = (x_offset + scroll_bar_width, thumb_position + thumb_height)
# 
#     # Design 1: Simple rectangle
#     engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
#     engine.addRectangle(thumb_start, thumb_end, 2)
# 
# icon_margin = 20
# 
# output_dir = 'scrollbar_animation'
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
# 
# num_frames = 10
# for i in range(num_frames):
#     engine = GraphicsEngine((1000, 200))
#     thumb_position = icon_margin + (200 - 2 * icon_margin - 30) * i / (num_frames - 1)
#     draw_scrollbar(engine, thumb_position, icon_margin)
#     engine.drawFeatures()
#     engine.showImage()#saveImage(os.path.join(output_dir, f'scrollbar_frame_{i:02d}.png'))
# =============================================================================


# =============================================================================
# # Assuming the GraphicsEngine has an addText() method
# def draw_scrollbar(engine, design_num, x_offset):
#     scroll_bar_width = 20
#     scroll_bar_start = (x_offset, icon_margin)
#     scroll_bar_end = (x_offset + scroll_bar_width, 200 - icon_margin)
#     thumb_height = 30
#     thumb_start = (x_offset, icon_margin)
#     thumb_end = (x_offset + scroll_bar_width, icon_margin + thumb_height)
# 
#     if design_num == 1:
#         # Design 1: Simple rectangle
#         engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
#         engine.addRectangle(thumb_start, thumb_end, 2)
#     elif design_num == 2:
#         # Design 2: Rounded rectangle
#         engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
#         engine.addEllipse((thumb_start[0] + scroll_bar_width / 2, thumb_start[1] + thumb_height / 2), scroll_bar_width / 2, thumb_height / 2, 0, 2)
#     elif design_num == 3:
#         # Design 3: Circle with line
#         engine.addCircle((thumb_start[0] + scroll_bar_width / 2, thumb_start[1] + thumb_height / 2), thumb_height / 2, 2)
#         engine.addLine(scroll_bar_start, scroll_bar_end, 2)
#     elif design_num == 4:
#         # Design 4: Triangle with line
#         triangle_vertices = [(thumb_start[0] + scroll_bar_width / 2, thumb_start[1]), (thumb_start[0], thumb_start[1] + thumb_height), (thumb_end[0], thumb_end[1])]
#         engine.addPolygon(triangle_vertices, 2)
#         engine.addLine(scroll_bar_start, scroll_bar_end, 2)
#     elif design_num == 5:
#         # Design 5: Ellipse with line
#         engine.addEllipse((thumb_start[0] + scroll_bar_width / 2, thumb_start[1] + thumb_height / 2), scroll_bar_width / 2, thumb_height / 4, 0, 2)
#         engine.addLine(scroll_bar_start, scroll_bar_end, 2)
# 
# icon_margin = 20
# 
# engine = GraphicsEngine((1000, 200))
# 
# for i in range(1, 6):
#     draw_scrollbar(engine, i, icon_margin + (i - 1) * (20 + icon_margin))
# 
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((1000, 200))
# 
# # App icons
# icon_size = 50
# icon_margin = 20
# num_icons = 5
# 
# for i in range(num_icons):
#     icon_start = (icon_margin + i * (icon_size + icon_margin), icon_margin)
#     icon_end = (icon_start[0] + icon_size, icon_start[1] + icon_size)
#     engine.addRectangle(icon_start, icon_end, 2)
# 
# # Scroll bar
# scroll_bar_width = 20
# scroll_bar_start = (1000 - scroll_bar_width - icon_margin, icon_margin)
# scroll_bar_end = (1000 - icon_margin, 150 - icon_margin)
# engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
# 
# # Scroll bar thumb
# thumb_height = 30
# thumb_start = (1000 - scroll_bar_width - icon_margin, icon_margin)
# thumb_end = (1000 - icon_margin, icon_margin + thumb_height)
# engine.addRectangle(thumb_start, thumb_end, 2)
# 
# # Context menu
# menu_height = 40
# menu_start = (0, 200 - menu_height)
# menu_end = (1000, 200)
# engine.addRectangle(menu_start, menu_end, 2)
# 
# # Menu buttons
# num_buttons = 3
# button_width = (1000 - icon_margin * (num_buttons + 1)) / num_buttons
# 
# for i in range(num_buttons):
#     button_start = (icon_margin + i * (button_width + icon_margin), 200 - menu_height)
#     button_end = (button_start[0] + button_width, 200)
#     engine.addRectangle(button_start, button_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((1000, 200))
# 
# # App icons
# icon_size = 50
# icon_margin = 20
# num_icons = 5
# 
# for i in range(num_icons):
#     icon_start = (icon_margin + i * (icon_size + icon_margin), icon_margin)
#     icon_end = (icon_start[0] + icon_size, icon_start[1] + icon_size)
#     engine.addRectangle(icon_start, icon_end, 2)
# 
# # Scroll bar
# scroll_bar_width = 20
# scroll_bar_start = (1000 - scroll_bar_width - icon_margin, icon_margin)
# scroll_bar_end = (1000 - icon_margin, 160 - icon_margin)
# engine.addRectangle(scroll_bar_start, scroll_bar_end, 2)
# 
# # Scroll bar thumb
# thumb_height = 30
# thumb_start = (1000 - scroll_bar_width - icon_margin, icon_margin)
# thumb_end = (1000 - icon_margin, icon_margin + thumb_height)
# engine.addRectangle(thumb_start, thumb_end, 2)
# 
# # Context menu
# menu_height = 40
# menu_start = (0, 200 - menu_height)
# menu_end = (700, 200)
# engine.addRectangle(menu_start, menu_end, 2)
# 
# # Menu buttons
# num_buttons = 3
# button_width = (800 - icon_margin * (num_buttons + 1)) / num_buttons
# 
# for i in range(num_buttons):
#     button_start = (icon_margin + i * (button_width + icon_margin), 200 - menu_height)
#     button_end = (button_start[0] + button_width, 200)
#     engine.addRectangle(button_start, button_end, 2)
# 
# # Tabs
# num_tabs = 3
# tab_width = 60
# tab_height = 40
# tab_margin = 10
# 
# for i in range(num_tabs):
#     tab_start = (1000 - (i + 1) * (tab_width + tab_margin), 200 - tab_height)
#     tab_end = (tab_start[0] + tab_width, 200)
#     engine.addRectangle(tab_start, tab_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================


# =============================================================================
# engine = GraphicsEngine((83, 19))
# 
# # Scroll bar background
# scrollbar_start = (0, 0)
# scrollbar_end = (30, 15)
# engine.addRectangle(scrollbar_start, scrollbar_end, 1)
# 
# # =============================================================================
# # # Scroll bar handle
# # handle_start = (71, 6)
# # handle_end = (78, 11)
# # engine.addRectangle(handle_start, handle_end, 1)
# # =============================================================================
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# 
# =============================================================================
# =============================================================================
# def create_app_grid(engine, rows, cols, start_x, start_y, icon_size, padding):
#     for row in range(rows):
#         for col in range(cols):
#             x = start_x + col * (icon_size + padding)
#             y = start_y + row * (icon_size + padding)
#             icon_start = (x, y)
#             icon_end = (x + icon_size, y + icon_size)
#             engine.addRectangle(icon_start, icon_end, 1)
#             #engine.addText((x + icon_size / 2, y + icon_size + 2), f"App{row * cols + col + 1}")
# 
# engine = GraphicsEngine((100, 20))
# 
# rows = 3
# cols = 5
# start_x = 0
# start_y = 0
# icon_size = 6
# padding = 2
# 
# create_app_grid(engine, rows, cols, start_x, start_y, icon_size, padding)
# 
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((100, 20))
# 
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
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# 
# 
# =============================================================================
# =============================================================================
# engine = GraphicsEngine((83, 19))
# 
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
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# def create_sinusoidal_points(num_points, amplitude, frequency, phase_shift):
#     x_values = np.linspace(0, 2 * math.pi * frequency, num_points)
#     y_values = amplitude * np.sin(x_values + phase_shift)
#     return [(x, y) for x, y in zip(x_values, y_values)]
# 
# engine = GraphicsEngine((83, 19))
# 
# num_points = 30
# amplitude = 1
# frequency = 1
# phase_shift = 0
# 
# sin_points = create_sinusoidal_points(num_points, amplitude, frequency, phase_shift)
# 
# for i in range(len(sin_points) - 1):
#     start_point = sin_points[i]
#     end_point = sin_points[i + 1]
#     engine.addLine(start_point, end_point, 1)
# 
# engine.drawFeatures()
# engine.showImage()
# 
# =============================================================================


# =============================================================================
# # Instantiate the GraphicsEngine object
# dimensions = (2200, 500)
# graphics_engine = GraphicsEngine(dimensions)
# 
# # Add a point
# graphics_engine.addPoint((10, 10))
# 
# # Add a line
# graphics_engine.addLine((50, 50), (100, 100), 5)
# 
# # Add a curve
# graphics_engine.addCurve([(150, 150), (200, 200), (250, 150)], 5)
# 
# # Add a triangle
# graphics_engine.addTriangle([(300, 300), (350, 350), (300, 350)], 5)
# 
# # Add a circle
# graphics_engine.addCircle((400, 400), 30, 5)
# 
# # Add an ellipse
# graphics_engine.addEllipse((150, 400), 50, 30, 0, 5)
# 
# # Add an arc
# graphics_engine.addArc((400, 150), 50, 0, np.pi, 5)
# 
# # Add a polygon
# graphics_engine.addPolygon([(50, 250), (100, 250), (100, 300), (50, 300)], 5)
# 
# # Add a rectangle
# graphics_engine.addRectangle((200, 200), (450, 500), 5)
# 
# # Add a quadrilateral
# graphics_engine.addQuadrilateral([(350, 200), (400, 200), (400, 250), (350, 250)], 5)
# 
# # Draw features and display the image
# graphics_engine.drawFeatures()
# graphics_engine.showImage()
# =============================================================================


# =============================================================================
# engine = GraphicsEngine((1000, 1000))
# 
# # Robot
# 
# # Head
# robot_head_center = (200, 200)
# robot_head_radius = 50
# engine.addCircle(robot_head_center, robot_head_radius, 2)
# 
# # Body
# robot_body_start = (150, 250)
# robot_body_end = (250, 450)
# engine.addRectangle(robot_body_start, robot_body_end, 2)
# 
# # Arms
# robot_left_arm_start = (100, 250)
# robot_left_arm_end = (150, 350)
# engine.addRectangle(robot_left_arm_start, robot_left_arm_end, 2)
# 
# robot_right_arm_start = (250, 250)
# robot_right_arm_end = (300, 350)
# engine.addRectangle(robot_right_arm_start, robot_right_arm_end, 2)
# 
# # Legs
# robot_left_leg_start = (150, 450)
# robot_left_leg_end = (200, 600)
# engine.addRectangle(robot_left_leg_start, robot_left_leg_end, 2)
# 
# robot_right_leg_start = (200, 450)
# robot_right_leg_end = (250, 600)
# engine.addRectangle(robot_right_leg_start, robot_right_leg_end, 2)
# 
# # Dragon
# 
# # Body
# dragon_body_start = (450, 400)
# dragon_body_end = (750, 600)
# engine.addEllipse(dragon_body_start, 300, 100, 0, 2)
# 
# # Head
# dragon_head_center = (800, 450)
# dragon_head_radius = 60
# engine.addCircle(dragon_head_center, dragon_head_radius, 2)
# 
# # Legs
# dragon_leg_start = (450, 600)
# dragon_leg_end = (500, 700)
# engine.addRectangle(dragon_leg_start, dragon_leg_end, 2)
# 
# dragon_right_leg_start = (700, 600)
# dragon_right_leg_end = (750, 700)
# engine.addRectangle(dragon_right_leg_start, dragon_right_leg_end, 2)
# 
# # Wings
# dragon_wing_start = (600, 350)
# dragon_wing_end = (700, 150)
# engine.addPolygon([(450, 400), dragon_wing_start, dragon_wing_end], 2)
# 
# dragon_right_wing_start = (600, 350)
# dragon_right_wing_end = (700, 150)
# engine.addPolygon([(750, 400), dragon_right_wing_start, dragon_right_wing_end], 2)
# 
# # Tail
# dragon_tail_start = (450, 400)
# dragon_tail_end = (300, 700)
# engine.addPolygon([dragon_tail_start, dragon_tail_end, (350, 650)], 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# # Create a GraphicsEngine instance with a 300x300 matrix
# GraphicsEngine = GraphicsEngine((300, 300))
# 
# # Add features to the GraphicsEngine
# GraphicsEngine.addLine((50, 50), (250, 50),2)
# GraphicsEngine.addCurve([(100, 100), (150, 200), (200, 100)], 2)
# GraphicsEngine.addCircle((150, 150), 50, 3)
# GraphicsEngine.addPolygon([(250, 250), (200, 200), (300, 200)], 5)
# GraphicsEngine.addRectangle((50, 200), (100, 50), 4)
# 
# # Draw the features on the matrix
# GraphicsEngine.drawFeatures()
# 
# # Display the resulting image
# GraphicsEngine.showImage()
# =============================================================================


# =============================================================================
# # Create a GraphicsEngine instance with a 300x300 matrix
# graphics_engine = GraphicsEngine((300, 300))
# 
# # Add features to the GraphicsEngine to create a face
# # Draw head (circle)
# graphics_engine.addCircle((150, 150), 100, 1)
# 
# # Draw eyes (two smaller circles)
# graphics_engine.addCircle((110, 120), 15, 1)
# graphics_engine.addCircle((190, 120), 15, 1)
# 
# # Draw nose (polygon)
# graphics_engine.addPolygon([(140, 150), (150, 160), (160, 150)], 1)
# 
# # Draw mouth (bezier curve)
# graphics_engine.addBezierCurve([(100, 190), (150, 210), (200, 190)], 1)
# 
# # Draw the features on the matrix
# graphics_engine.drawFeatures()
# 
# # Display the resulting image
# graphics_engine.showImage()
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((800, 800))
# 
# # Ocean
# ocean_start = (0, 400)
# ocean_end = (800, 800)
# engine.addRectangle(ocean_start, ocean_end, 2)
# 
# # Boat base
# boat_base_start = (300, 300)
# boat_base_end = (500, 350)
# engine.addRectangle(boat_base_start, boat_base_end, 2)
# 
# # Mast
# mast_start = (400, 100)
# mast_end = (400, 300)
# engine.addLine(mast_start, mast_end, 2)
# 
# # Sail left
# sail_left_start = (400, 100)
# sail_left_end = (300, 300)
# engine.addLine(sail_left_start, sail_left_end, 2)
# 
# # Sail right
# sail_right_start = (400, 100)
# sail_right_end = (500, 300)
# engine.addLine(sail_right_start, sail_right_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================
# =============================================================================
# engine = GraphicsEngine((500, 500))
# 
# # Head
# head_center = (250, 150)
# head_radius = 75
# engine.addCircle(head_center, head_radius, 2)
# 
# # Body
# body_start = (200, 225)
# body_end = (300, 325)
# engine.addRectangle(body_start, body_end, 2)
# 
# # Left arm
# left_arm_start = (150, 225)
# left_arm_end = (200, 275)
# engine.addRectangle(left_arm_start, left_arm_end, 2)
# 
# # Right arm
# right_arm_start = (300, 225)
# right_arm_end = (350, 275)
# engine.addRectangle(right_arm_start, right_arm_end, 2)
# 
# # Left leg
# left_leg_start = (200, 325)
# left_leg_end = (230, 425)
# engine.addRectangle(left_leg_start, left_leg_end, 2)
# 
# # Right leg
# right_leg_start = (270, 325)
# right_leg_end = (300, 425)
# engine.addRectangle(right_leg_start, right_leg_end, 2)
# 
# # Nose
# nose_center = (250, 175)
# nose_radius = 25
# engine.addCircle(nose_center, nose_radius, 2)
# 
# # Left eye
# left_eye_center = (225, 125)
# left_eye_radius = 10
# engine.addCircle(left_eye_center, left_eye_radius, 2)
# 
# # Right eye
# right_eye_center = (275, 125)
# right_eye_radius = 10
# engine.addCircle(right_eye_center, right_eye_radius, 2)
# 
# # Mouth
# mouth_start = (225, 200)
# mouth_end = (275, 220)
# mouth_control_points = [(225, 200), (250, 240), (275, 220)]
# engine.addCurve(mouth_control_points, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# engine = GraphicsEngine((2000, 2000))
# 
# # Braille display background
# bg_start = (50, 50)
# bg_end = (100, 1450)
# engine.addRectangle(bg_start, bg_end, 2)
# 
# # Braille cells
# cell_width = 10
# cell_height = 50
# cell_spacing = 10
# num_rows = 5
# num_columns = 28
# 
# for row in range(num_rows):
#     for col in range(num_columns):
#         cell_start = (50 + cell_spacing * (col + 1) + cell_width * col,
#                       50 + cell_spacing * (row + 1) + cell_height * row)
#         cell_end = (cell_start[0] + cell_width, cell_start[1] + cell_height)
#         engine.addRectangle(cell_start, cell_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================
# Initialize GraphicsEngine with dimensions (500,500)
# =============================================================================
# engine = GraphicsEngine((500,500))
# 
# # Body
# body_start = (200, 300)
# body_end = (400, 400)
# engine.addRectangle(body_start, body_end, 2)
# 
# # Head
# head_center = (300, 250)
# head_radius = 50
# engine.addCircle(head_center, head_radius, 2)
# =============================================================================

# =============================================================================
# # Ears
# left_ear_start = (260, 190)
# left_ear_end = (290, 220)
# engine.addTriangle(head_center, left_ear_start, left_ear_end, 2)
# 
# right_ear_start = (310, 190)
# right_ear_end = (340, 220)
# engine.addTriangle(head_center, right_ear_start, right_ear_end, 2)
# =============================================================================

# =============================================================================
# # Eyes
# left_eye_center = (280, 240)
# left_eye_radius = 10
# engine.addCircle(left_eye_center, left_eye_radius, 2)
# 
# right_eye_center = (320, 240)
# right_eye_radius = 10
# engine.addCircle(right_eye_center, right_eye_radius, 2)
# 
# # Pupils
# left_pupil_center = (280, 240)
# left_pupil_radius = 5
# engine.addCircle(left_pupil_center, left_pupil_radius, 2)
# 
# right_pupil_center = (320, 240)
# right_pupil_radius = 5
# engine.addCircle(right_pupil_center, right_pupil_radius, 2)
# 
# # Nose
# nose_center = (300, 260)
# nose_radius = 5
# engine.addCircle(nose_center, nose_radius, 2)
# 
# # Mouth
# mouth_start = (280, 280)
# mouth_end = (320, 280)
# engine.addLine(mouth_start, mouth_end, 2)
# 
# # Legs
# left_leg_start = (210, 400)
# left_leg_end = (230, 450)
# engine.addRectangle(left_leg_start, left_leg_end, 2)
# 
# right_leg_start = (370, 400)
# right_leg_end = (390, 450)
# engine.addRectangle(right_leg_start, right_leg_end, 2)
# 
# # Draw features and show image
# engine.drawFeatures()
# engine.showImage()
# =============================================================================

# =============================================================================
# 
# class GraphicsEngine:
# 
#     def __init__(self, dimensions):
#         # create a matrix based on the input dimensions
#         
#         #first figure out the dimensions of the given matrix
#         newMat = np.array(matrix)
#         dim = newMat.shape
#         newDim = (math.ceil(dim[0]/20)*20, math.ceil(dim[1]/20)*20)
#         self.data = np.zeros((newDim[0],newDim[1]), dtype=np.uint8)
#         self.__oldDim = dim
#         #copy data from the input matrix to internal data
#         self.data[0:dim[0],0:dim[1]] = newMat
#         self.data[self.data == 1] = 255
#         self.state = matrix
#         surface = ca.ImageSurface.create_for_data(self.data, ca.FORMAT_A8, newDim[1], newDim[0])
#         self.__ct = ca.Context(surface)
#         self.__ct.set_operator(ca.OPERATOR_SOURCE)
#         self.__output = 1
#         self.test = 1
#         
#         #create the brailler
#         self.Brailler = br.Brailler(self.data, self.state)
# 
#     def read_matrix(self, matrix):
#         #create the graphics
#         #first figure out the dimensions of the given matrix
#         newMat = np.array(matrix)
#         dim = newMat.shape
#         newDim = (math.ceil(dim[0]/20)*20, math.ceil(dim[1]/20)*20)
#         self.data = np.zeros((newDim[0],newDim[1]), dtype=np.uint8)
#         self.__oldDim = dim
#         #copy data from the input matrix to internal data
#         self.data[0:dim[0],0:dim[1]] = newMat
#         self.data[self.data == 1] = 255
#         dim = self.data.shape
#         self.state = matrix
#         surface = ca.ImageSurface.create_for_data(self.data, ca.FORMAT_A8, newDim[0], newDim[1])
#         self.__ct = ca.Context(surface)
# 
# 
#     def set_output(self,val):
#         """ sets the output value of all pycairo commands """
#         self.__output = val
# 
# 
#     def select_element(self, coord):
#         """ selects a single element to change """
#         if self.__output:
#             self.data[coord[0], coord[1]] = 255
#         else:
#             self.data[coord[0], coord[1]] = 0
# 
#         self.state[coord[0]][coord[1]] = self.__output
# 
# 
#     def select_cell(self, coord):
#         
#         xPosition = int(coord[0]/4) * 4
#         yPosition = int(coord[1]/3) * 3
#         
#         topRight = (xPosition, yPosition)
#         bottomLeft = (xPosition + 2, yPosition + 1)
#         
#         self.make_rectangle(topRight, bottomLeft, 1, 0)
#         
#         
#     def make_line(self, start, end, width):
#         """ takes in two tuples that represent coordinates of the
#         start and end locations of the line """
#         #use offset if width is odd
#         if (width % 2) == 0:
#             offset = 0
#         else:
#             offset = 0.5
# 
#         #add .5 to the start and end
#         startY = start[0] + offset
#         startX = start[1] + offset
#         endY = end[0] + offset
#         endX = end[1] + offset
#         self.__ct.move_to(startX,startY)
#         self.__ct.line_to(endX,endY)
#         self.__ct.set_line_width(width)
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         self.__ct.stroke()
#         self.__save_data()
# 
# 
#     def make_bezierCurve(self, start, c1, c2, end, width):
#         """ takes in a start point and end point as well as two curve points
#         it produces a line that bends to all the points """
#         startY = start[0]
#         startX = start[1]
#         endY = end[0]
#         endX = end[1]
#         self.__ct.move_to(startX,startY)
#         self.__ct.curve_to(c1[1], c1[0], c2[1], c2[0], endX, endY)
#         self.__ct.set_line_width(width)
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         self.__ct.stroke()
#         self.__save_data()
# 
#     def make_circle(self, center, radius, width, fill):
#         """ take in a center and radius and fill or stroke depending on selection"""
#         self.__ct.arc(center[1], center[0], radius, 0, 2*math.pi)
#         self.__ct.set_line_width(width)
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         if fill:
#             self.__ct.fill()
#         else:
#             self.__ct.stroke()
#         self.__save_data()
# 
#     def make_polygon(self, start, points, width, fill):
#         """ take in multiple points and string them all together """
#         #use offset if width is odd
#         if (width % 2) == 0:
#             offset = 0
#         else:
#             offset = 0.5
# 
#         startY = start[0] + offset
#         startX = start[1] + offset
# 
#         self.__ct.move_to(startX,startY)
#         for point in points:
#             self.__ct.line_to(point[1] + offset, point[0] + offset)
#         self.__ct.line_to(startX, startY)
#         self.__ct.set_line_width(width)
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         if fill:
#             self.__ct.fill()
#         else:
#             self.__ct.stroke()
#         self.__save_data()
# 
# 
# 
#     def make_rectangle(self, corner1, corner2, width, fill):
#         """ take in two corners of a rectangle and string together to make the correct shape """
#         #use offset if width is odd
#         if (width % 2) == 0:
#             offset = 0
#         else:
#             offset = 0.5
# 
#         startY = corner1[0] + offset
#         startX = corner1[1] + offset
#         endY = corner2[0] + offset
#         endX = corner2[1] + offset
#         X1 = endX
#         Y1 = startY
#         X2 = startX
#         Y2 = endY
#         self.__ct.move_to(startX,startY)
#         self.__ct.line_to(X1,Y1)
#         self.__ct.line_to(endX,endY)
#         self.__ct.line_to(X2,Y2)
#         self.__ct.line_to(startX,startY)
#         self.__ct.set_line_width(width)
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         if fill:
#             self.__ct.fill()
#         else:
#             self.__ct.stroke()
#         self.__save_data()
# 
#     def write_latin(self, start, displayString, font, size):
#         """ takes in starting point for font and string to write
#         naturally fills up the screen as you type """
#         startY = start[0]
#         startX = start[1]
#         #move to start point
#         self.__ct.move_to(startX,startY)
# 
#         #select the braille font
#         self.__ct.select_font_face(font, ca.FONT_SLANT_NORMAL, ca.FONT_WEIGHT_BOLD)
#         self.__ct.set_font_size(size)
# 
# 
#         #type out the text
#         self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         self.__ct.show_text(displayString)
#         self.__save_data()
# 
#     def write_braille(self, start, brailleString):
#         #first clear all spaces in the braille string
# # =============================================================================
# #         startY = start[0] + 3
# #         startX = start[1]
# #         curCol = startX
# #         curRow = startY
# #         dim = self.__oldDim
# #         dimRow = dim[0]
# #         dimCol = dim[1]
# #         self.set_output(False)
# #         for letter in brailleString:
# #             if letter == '\n':
# #                 if curRow + 3 < dimRow:
# #                     curCol = 0
# #                     curRow = curRow + 4
# #                 else:
# #                     break
# # # =============================================================================
# # #             elif letter == ' ':
# # #                 if curCol == 0:
# # #                     pass
# # # =============================================================================
# #             else:
# #                 if (letter.isupper() or letter.isdigit()) and curCol + 5 < dimCol:
# #                     self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 5), 2, 1)
# #                     curCol = curCol + 5
# #                 elif not (letter.isupper() or letter.isdigit()) and curCol + 3 < dimCol:  #if the letter is a lower case make room plus a space
# #                     self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 3), 2, 1)
# #                     curCol = curCol + 3
# #                 elif curRow + 3 < dimRow: #if the end of the line is reached start a new line
# #                     if not (letter.isupper() or letter.isdigit()) and curCol + 2 <= dimCol:   
# #                         self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 3), 2, 1)
# #                         curRow = curRow + 4
# #                         curCol = startX
# #                     elif (letter.isupper() or letter.isdigit()) and curCol + 4 <= dimCol:
# #                         self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 5), 2, 1)
# #                         curRow = curRow + 4
# #                         curCol = startX
# #                     else:    
# #                         curRow = curRow + 4
# #                         curCol = startX
# #                         self.__ct.move_to(curCol,curRow)
# #                         if not (letter.isupper() or letter.isdigit()) and curCol + 3 < dimCol:
# #                             self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 3), 2, 1)
# #                             curCol = curCol + 3
# #                         elif (letter.isupper() or letter.isdigit()) and curCol + 5 < dimCol:
# #                             self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 5), 2, 1)
# #                             curCol = curCol + 5
# #                         
# #                 elif not (letter.isupper() or letter.isdigit()) and curCol + 2 <= dimCol:
# #                     self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 3), 2, 1)
# #                 elif (letter.isupper() or letter.isdigit()) and curCol + 4 <= dimCol:
# #                     self.make_rectangle((curRow, curCol), (curRow - 3, curCol + 5), 2, 1)
# #                 else: #end of the string
# #                     break
# #             self.__ct.move_to(curCol,curRow)
# #         self.__save_data()
# #         self.set_output(True)
# #         #write the braille string
# # =============================================================================
#         self.__braillePrinter(start, brailleString)
# 
#     def __braillePrinter(self, start, brailleString):
#         """ takes in starting point for font and string to write
#         naturally fills up the screen as you type """
#         
#         startY = start[0]
#         startX = start[1]
#         #move to start point
#         #self.state
#         #print(self.state)
#         
#         #self.__ct.move_to(startX,startY)
# 
#         #select the braille font
#         #self.__ct.select_font_face("Braille Regular", ca.FONT_SLANT_NORMAL, ca.FONT_WEIGHT_NORMAL)
#         #self.__ct.set_font_size(3)
# 
# 
#         #type out the text
#         #self.__ct.set_source_rgba(self.__output, self.__output, self.__output, self.__output)
#         #xy locations of typing the letters and dimensions to know where to stop
#         curCol = startX
#         curRow = startY
#         dim = self.__oldDim
#         dimRow = dim[0]
#         dimCol = dim[1]
#         for letter in brailleString:
#             if letter == '\n':
#                 if curRow + 3 < dimRow:
#                     curCol = 0
#                     curRow = curRow + 4
#                 else:
#                     break
# # =============================================================================
# #             elif letter == ' ':
# #                 if curCol == 0:
# #                     pass
# # =============================================================================
#             else:
#                 if curCol + 2 <= dimCol:
#                     self.Brailler.printCharacter([curCol,curRow],letter)
#                     curCol = curCol + 3
#                 elif curRow < (dimRow - 4):
#                     curCol = startX
#                     curRow = curRow + 4
#                     self.Brailler.printCharacter([curCol,curRow],letter)
#                 else:
#                     pass
# 
#     def clear(self):
#         self.data[:,:] = 0
#         self.__save_data()
# 
#     def __save_data(self):
#         #print('---------------------------\n\r')
#         #print('\n'.join([' '.join(['{:4}'.format(item) for item in row])
#         # for row in self.data]))
#         self.data[self.data > 115] = 255
#         self.data[self.data != 255] = 0
#         dim = np.array(self.state).shape
#         self.state.clear()
#         self.state.extend((self.data[0:dim[0],0:dim[1]] == 255).tolist())
# 
# 
# 
# =============================================================================