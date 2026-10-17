# Make It Move: prompt starters

Write your own requests. Include what should happen and what should stay unchanged. Use one request at a time in the same Copilot conversation.

## Create • one bouncing ball
Start: "Help me create a Python animation that…"

Include Python Tkinter Canvas, one moving ball, bouncing off all four edges, your colors, and my_project.py. Use only the standard library. Request after() scheduling so the window remains responsive.

Check all four edges before adding features.

## Interact • clicks add balls
Start: "When I click inside the drawing area, I want…"

Describe a new moving ball near the click, all balls staying inside the canvas, and a limit such as 30 balls.

Check: one starting ball plus three clicks gives four balls. Try an edge click.

## Personalize • choose two
Start: "Change… while keeping…"

Choose colors, size, speed, title, or Pause/Resume. Make one request at a time. Explain exactly what the change should do.

## Partner feedback
Start: "My partner noticed… Please change…"

Preserve the features that already work. Run and check the improvement.

## Fix
Start: "I expected… but I saw…"

Include relevant code and the full error if any. Ask for the smallest fix.

## Understand
"Explain the part that moves the ball in everyday language. Do not change the code."

## Optional game direction
Start: "Turn this into a click-the-target game…"

Define hits and misses, score behavior, and whether the target moves after a hit. Replace click-to-add behavior with click-to-score rather than leaving conflicting click actions. Keep it to one target initially.
