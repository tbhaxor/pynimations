from pynimations import progressbar

print("------ Progressbar Animation Testing ------")
p1 = progressbar.Animator()
p2 = progressbar.Animator(label="Test With Label")
p3 = progressbar.Animator(label="Test With Label and Interval", interval=50)
p4 = progressbar.Animator(label="Test With Label, Interval and length", interval=50, length=60)
p5 = progressbar.Animator(label="Test With All Arguments", interval=50, length=60, style="ascii")

p1.animate()
print()
p2.animate()
print()
p3.animate()
print()
p4.animate()
print()
p5.animate()
