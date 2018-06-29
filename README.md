# Air-Pen
Requirements: The program is written is "Python"(version 2.7 or higher will work). You will need OpenCV and NumPy libraries.

Description: This algorithm analyzes sequential frames and tracks movement of object. The object should be of blue color of a particular size and with a clear background, would give a better accuracy. In this algorithm, at first the frame is read and filtered and then contour is detected which helps in tracking the object. A minimum enclosing circle is formed and its center's locations are stored in a deque. This simple algorithm is used for tracking object movement.

Execution: To run the code, type python airpen.py
