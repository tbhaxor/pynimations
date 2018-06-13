from pynimations import typewriter

print("------- Typewrite Animation Test -------")
t1 = typewriter.Animator()
t2 = typewriter.Animator(label=["Testing", "with", "only", "label"])
t3 = typewriter.Animator(label=["Testing", "with", "label", "and", "interval"], interval=50)
t4 = typewriter.Animator(label=["Testing", "with", "all", "optional", "arguments"], interval=10, wait_unitl=500)

t1.animate()
print()
t2.animate()
print()
t3.animate()
print()
t4.animate()
print()
