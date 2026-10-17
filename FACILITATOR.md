# Make It Move facilitator guide

## Purpose
From Prompt to Program is a 55-minute workshop for adults with no coding experience. They create an interactive Python animation from the empty my_project.py using Copilot. The goal is to describe behavior, inspect output, and improve requests. They do not need to understand every animation command.

## Setup before the session
Test Git, VS Code Python extension, Copilot access, and desktop Python Tkinter using the actual training computers and accounts. A graphical display and Tk are required. No pip packages or external assets are needed.
Prepare your own small demo separately before participants arrive. Verify all four boundaries, click-to-add, responsiveness, and closing/restarting. Do not prefill their my_project.py.
If they have an older clone, use a fresh folder rather than discarding their work.

## 55 minutes
0–5: Show one moving ball, click to add another, then take a specific audience suggestion. Ask: "What should happen when we click?"
5–12: Clone and open the empty file. Participants sketch or describe a calming display, visual playground or optional reaction game.
12–25: Guide their own prompt for one bouncing ball using Tkinter Canvas and after(). Apply generated code and test all four boundaries.
25–33: Add click-to-create interaction with a 30-ball limit. Check one initial ball plus three clicks produces four and that edge clicks stay visible.
33–38: Choose two personal changes to colors, size, speed, title or Pause/Resume.
38–48: Partners use each other's apps without initial coaching, report one issue, and request and test one improvement.
48–55: Short showcases and save my_project.py to personal approved storage. No push is required.

## Keep it manageable
Use only my_project.py for participant code. The required activity is animation and click interaction, not a full physics engine. Ball-to-ball collisions, gravity and scoring are not required.
Small functions, event bindings and animation loops scheduled with after() are appropriate. Do not carry over earlier bans on functions and loops.
Explain Canvas as the drawing area, after() as scheduling the next movement, and a callback as what runs after a click. Avoid a syntax lecture.
If a participant chooses a reaction game, use one target and click-to-score after the basic animation works. Explicitly replace the click-to-add action.

## Checks
All four edges: the full ball remains visible, does not stick or disappear.
Three clicks: exactly three extra balls appear, moving independently.
Edge click: the new ball is positioned inside the canvas.
Resizing: either use a fixed-size drawing area or update the bounce boundaries to the actual canvas size.
Pause/Resume, if added: movement pauses and resumes without duplicate timers or sudden speed changes.
Limit reached: no unlimited object creation or confusing crash.
Window stays responsive and closes normally.

## Support and fallback
For AI access problems, pair with a working account or demonstrate while participants design prompts and predict results. Have your tested local demo available for recovery.
Missing Tk/display is an environment problem, not an animation bug. Use a computer known to work. Never claim the lab is ready until tested there.
If timing is tight, skip optional game features and focus on one working interaction and partner feedback.
