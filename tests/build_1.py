from pynimations import progressbar

p = progressbar.Animator("Test 1", 200, 50, style="ascii")
p.animate()

P = progressbar.Animator("Test 2", 200, 50, style="pip")
P.animate()

