You are an advanced AI language model that understands G-code commands for valve control in a row and column array system. The G-code commands available are:

r - Sets all rows low (Example: r)
R - Sets all rows high (Example: R)
c - Sets all columns low (Example: c)
C - Sets all columns high (Example: C)
~R - Inverts all row values (Example: ~R)
~C - Inverts all column values (Example: ~C)
r[i:j] - Sets rows low (Example: r[1:4])
R[i:j] - Sets rows high (Example: R[1:4])
c[i:j] - Sets columns low (Example: c[1:4])
C[i:j] - Sets columns high (Example: C[1:4])
~R[i:j] - Inverts row values (Example: ~R[1:4])
~C[i:j] - Inverts column values (Example: ~C[1:4])
To create a .gcode file, simply list the G-code commands, one per line. Each command can be followed by an optional index range in the format [i:j], where 'i' is the starting index (inclusive) and 'j' is the ending index (exclusive).

Please create a .gcode file that performs the following experiment:

Set all rows low and all columns high.
Set columns 10 to 41 low.
Invert the state of all columns.
set rows 2 to 15 high
set all columns low
