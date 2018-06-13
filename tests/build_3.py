from pynimations import casetoggle

print("------ CaseToggle Animation Testing ------")
c1 = casetoggle.Animator()
c2 = casetoggle.Animator(label="Test with label")
c3 = casetoggle.Animator(label="Test with label and interval", interval=200)
c4 = casetoggle.Animator(label="Test with all arguments", interval=50, iteration=10)

c1.animate()
print()
c2.animate()
print()
c3.animate()
print()
c4.animate()
print()
