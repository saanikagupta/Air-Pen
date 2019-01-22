# Air-Pen
## Requirements: 
The program is written in Python (version 2.7 or higher will work). You will need OpenCV and NumPy libraries.

## Description: 
This algorithm analyzes sequential frames and tracks movement of object. The object should be of blue color and of a particular size, with a clear background. This would give a better accuracy. In this algorithm, at first the frame is read and filtered and then contour is detected, which helps in tracking the object. A minimum enclosing circle is formed and its center's location is stored in a deque. This simple algorithm is used for tracking object movement.

## Execution: 
```python airpen.py```
