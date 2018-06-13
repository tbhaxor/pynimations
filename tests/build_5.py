from pynimations import scroll

print("------ Scoll Text Animation Test ------")
s1 = scroll.Animator()
s2 = scroll.Animator(label="Loading with text")
s3 = scroll.Animator(label="Loading with text and iteration", iteration=1)
s4 = scroll.Animator(label="Loading with text, iteration and interval", iteration=1, interval=50)
s5 = scroll.Animator(label="Loading with all args", iteration=1, interval=1, length=-1)

s1.animate()
print()
s2.animate()
print()
s3.animate()
print()
s4.animate()
print()
s5.animate()
print()
