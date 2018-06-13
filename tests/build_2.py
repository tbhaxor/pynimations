from pynimations import rotator

print("------ Rotator Animation Testing ------")
r1 = rotator.Animator()
r2 = rotator.Animator(label="Test with label")
r3 = rotator.Animator(label="Test with label and interval", interval=500)
r4 = rotator.Animator(label="Test with all arguments", interval=300, iteration=2)

r1.animate()
print()
r2.animate()
print()
r3.animate()
print()
r4.animate()
print()
