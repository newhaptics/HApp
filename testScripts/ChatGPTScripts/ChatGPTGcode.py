import DisplaySerial as ds
import time

serialPort = ds.DisplaySerial("COM4", 57600, 3)
serialPort.getSize()
rowArray = serialPort.getRowValveArray()
columnArray = serialPort.getColumnValveArray()

serialPort.setColumnValveArrayAssignment(columnArray)
serialPort.setRowValveArrayAssignment(rowArray)
print(serialPort.getColumnValveArray())
print(serialPort.getRowValveArray())

def stateArrayToBytearray(state_array):
    bit_string = ''.join(map(str, state_array))
    num_full_bytes = len(bit_string) // 8
    num_remaining_bits = len(bit_string) % 8

    bytearray_result = bytearray(int(bit_string[i:i+8], 2) for i in range(0, num_full_bytes * 8, 8))

    if num_remaining_bits > 0:
        last_byte = int(bit_string[-num_remaining_bits:] + '0' * (8 - num_remaining_bits), 2)
        bytearray_result.append(last_byte)

    return bytearray_result

rowValveStateArray = [0] * 19
columnValveStateArray = [0] * 41

row_bytearray = stateArrayToBytearray(rowValveStateArray)
column_bytearray = stateArrayToBytearray(columnValveStateArray)

serialPort.setRowValveStateArray(list(row_bytearray))
serialPort.setColumnValveStateArray(list(column_bytearray))


time.sleep(1)

for i in range(0,len(columnValveStateArray)):
    columnValveStateArray[i] = 1
    column_bytearray = stateArrayToBytearray(columnValveStateArray)
    serialPort.setColumnValveStateArray(list(column_bytearray))
    time.sleep(0.2)

rowValveStateArray = [1] * 19
columnValveStateArray = [0] * 41

row_bytearray = stateArrayToBytearray(rowValveStateArray)
column_bytearray = stateArrayToBytearray(columnValveStateArray)

serialPort.setRowValveStateArray(list(row_bytearray))
time.sleep(1)
serialPort.setColumnValveStateArray(list(column_bytearray))


for i in range(0,len(rowValveStateArray)):
    rowValveStateArray[i] = 0
    row_bytearray = stateArrayToBytearray(rowValveStateArray)
    serialPort.setRowValveStateArray(list(row_bytearray))
    time.sleep(0.2)


Using the above code as an example create a python library which uses Gcode commands for turning on and off valves in the rowValveStateArrays and columnValveStateArrays and executes serialPort.setRowValveStateArray and serialPort.setColumnValveStateArray.
Gcode commands:
r - sets rows low
R - sets rows high
C - sets columns high
c - sets columns low
~R - inverts row values (0 to 1, 1 to 0)
~C - inverts column values (0 to 1, 1 to 0)

Every command should be able to specify the indices of the that need to be changed
r[i:j]- sets rows i through j low
R[i:j]- sets rows i through j high
c[i:j]- sets columns i through j low
C[i:j]- sets columns i through j high
~R[i:j]- sets rows i through j to inverse (0 to 1, 1 to 0)
~C[i:j]- sets columns i through j to inverse (0 to 1, 1 to 0)

Example Gcode script:
r //set all rows low
c //set all rows high
C[1:13] //set columns 1 through 13 high
R // set all rows high
~R[10:19] // set rows 10 through 19 inverse (low)
