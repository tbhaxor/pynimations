import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../code/'))
from pynimations import rotator
print("------ Rotator Animation Testing ------")

r1 = rotator.Animator()
r1.animate()
print()
r2 = rotator.Animator(label="Test with label")
r2.animate()
print()
r3 = rotator.Animator(label="Test with label and interval", interval=500)
r3.animate()
print()
r4 = rotator.Animator(label="Test with all arguments", interval=300, iteration=2)
r4.animate()
print()