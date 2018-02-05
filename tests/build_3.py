import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../code/'))
from pynimations import casetoggle
print("------ CaseToggle Animation Testing ------")

c1 = casetoggle.Animator()
c1.animate()
print()
c2 = casetoggle.Animator(label="Test with label")
c2.animate()
print()
c3 = casetoggle.Animator(label="Test with label and interval", interval=200)
c3.animate()
print()
c4 = casetoggle.Animator(label="Test with all arguments", interval=50, iteration=10)
c4.animate()
print()
