import DisplaySerial as ds
import re
import time

class GCodeController:
    def __init__(self, serial_port):
        self.serial_port = serial_port
        self.row_valve_state_array = [0] * 19
        self.column_valve_state_array = [0] * 41

    def state_array_to_bytearray(self, state_array):
        bit_string = ''.join(map(str, state_array))
        num_full_bytes = len(bit_string) // 8
        num_remaining_bits = len(bit_string) % 8

        bytearray_result = bytearray(int(bit_string[i:i + 8], 2) for i in range(0, num_full_bytes * 8, 8))

        if num_remaining_bits > 0:
            last_byte = int(bit_string[-num_remaining_bits:] + '0' * (8 - num_remaining_bits), 2)
            bytearray_result.append(last_byte)

        return bytearray_result

    def update_valve_state_arrays(self):
        row_bytearray = self.state_array_to_bytearray(self.row_valve_state_array)
        column_bytearray = self.state_array_to_bytearray(self.column_valve_state_array)

        self.serial_port.setRowValveStateArray(list(row_bytearray))
        self.serial_port.setColumnValveStateArray(list(column_bytearray))

    def process_gcode(self, gcode):
# =============================================================================
#         command_pattern = re.compile(r'([rRcC~][RrCc])\[(\d+)?:(\d+)?\]|([rRcC])|(d(\d+(\.\d+)?))')
#         commands = command_pattern.findall(gcode)
# =============================================================================
        command_pattern = re.compile(r'([rRcC~][RrCc]|([rRcC]))(\[(\d+)?:(\d+)?\])?')
        commands = command_pattern.findall(gcode)
    
        for command in commands:
            cmd, single_cmd, listThing, i, j = command
            if listThing == '':
                cmd = single_cmd
                i = 0
                j = -1
            else:
                i = int(i) if i else 0
                j = int(j) + 1 if j else -1
    
            if cmd == "r":
                self.row_valve_state_array[i:j] = [0] * len(self.row_valve_state_array[i:j])
            elif cmd == "R":
                self.row_valve_state_array[i:j] = [1] * len(self.row_valve_state_array[i:j])
            elif cmd == "c":
                self.column_valve_state_array[i:j] = [0] * len(self.column_valve_state_array[i:j])
            elif cmd == "C":
                self.column_valve_state_array[i:j] = [1] * len(self.column_valve_state_array[i:j])
            elif cmd == "~R":
                self.row_valve_state_array[i:j] = [1 - x for x in self.row_valve_state_array[i:j]]
            elif cmd == "~C":
                self.column_valve_state_array[i:j] = [1 - x for x in self.column_valve_state_array[i:j]]
    
            self.update_valve_state_arrays()
            time.sleep(0.5)
