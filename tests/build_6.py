from pynimations import blinker

print("------ Blinker Animation Test ------")
b1 = blinker.Animator()
b2 = blinker.Animator(label="Blinking with label")
b3 = blinker.Animator(label="Blinking with label and iteration", iterations=2)
b4 = blinker.Animator(label="Blinking with all args", iterations=5, interval=100)

b1.animate()
print()
b2.animate()
print()
b3.animate()
print()
b4.animate()
print()
