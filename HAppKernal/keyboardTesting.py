# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:01:40 2023

@author: derek
"""
# =============================================================================
# 
# import pywinusb.hid as hid
# 
# def on_data(data):
#     print(f"Data received: {data}")
# 
# def find_keyboards():
#     all_devices = hid.find_all_hid_devices()
#     keyboards = []
#     for device in all_devices:
#         if device.vendor_id == VENDOR_ID and device.product_id == PRODUCT_ID:
#             keyboards.append(device)
#     return keyboards
# 
# if __name__ == "__main__":
#     VENDOR_ID = 0x413C  # Replace with the correct vendor ID
#     PRODUCT_ID = 0x2113  # Replace with the correct product ID
# 
# # =============================================================================
# #     VENDOR_ID = 0x413C  # Replace with the correct vendor ID
# #     PRODUCT_ID = 0x30  # Replace with the correct product ID
# # =============================================================================
# 
#     keyboards = find_keyboards()
#     for keyboard in keyboards:
#         print(f"Keyboard found: {keyboard.vendor_name} {keyboard.product_name}")
#         keyboard.open
#
# =============================================================================
# =============================================================================
# import pywinusb.hid as hid
# 
# def on_data(keyboard_id, data):
#     # The second byte of data contains the keycode
#     keycode = data[2]
# 
#     # Ignore 'no event' indication (keycode == 0)
#     if keycode != 0:
#         key_pressed = data[0] in (1, 2)  # Check if a key is pressed
# 
#         if key_pressed:
#             print(f"Key pressed: {keycode} on keyboard {keyboard_id}")
#             on_press(keyboard_id, keycode)
#         else:
#             print(f"Key released: {keycode} on keyboard {keyboard_id}")
#             on_release(keyboard_id, keycode)
# 
# def on_press(keyboard_id, keycode):
#     # Implement your logic for key press events here
#     pass
# 
# def on_release(keyboard_id, keycode):
#     # Implement your logic for key release events here
#     pass
# 
# def find_keyboards():
#     all_devices = hid.find_all_hid_devices()
#     keyboards = []
#     for device in all_devices:
#         if "keyboard" in device.product_name.lower():
#             keyboards.append(device)
#     return keyboards
# 
# if __name__ == "__main__":
#     keyboards = find_keyboards()
# 
# =============================================================================
