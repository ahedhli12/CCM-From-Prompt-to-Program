# From Prompt to Program event app workshop

## Audience and purpose
Adults with no programming experience. One 55-minute session. Participants use Copilot to create or modify a small graphical Event Budget Planner. They learn to describe behavior, run code, check a result and request one improvement. They do not need to learn all of Tkinter.

## Before the session
On the actual training computers and accounts, confirm Git, Python 3, the VS Code Python extension and Copilot. Run my_project.py and check that its Tkinter window opens, calculates and closes. Python needs Tk and a graphical display. No pip packages are needed. Keep credentials separate. Have the working repository example available as a fallback.

## Agenda
0–5: Demo a $300 event for 20 people. Let the room choose food costs.
5–15: Guide Git: Clone, open my_project.py and run the working example.
15–25: Explain prompt, program and app. Use the main prompt to generate a version in the same file. Say clearly that the file already has a working example and applying AI's edit replaces or modifies it.
25–35: Check the known examples, then a blank field or a word.
35–45: Each participant requests one change: event title/colors, cost per attendee, or Clear button.
45–55: Partners plan a 20-person event within $300, share briefly, and save their file outside temporary training accounts.

## Known calculations
20 people, $10 food/person, $50 supplies, $300 budget: $250 total, $50 remaining.
20 people, $15 food/person, $50 supplies, $300 budget: $350 total, $50 over.
20 people, $12.50 food/person, $50 supplies, $300 budget: $300 total, $0 remaining.
Blank, nonnumeric, negative or infinite costs should show a helpful message. Zero attendees should be rejected.

## Teaching
Say: "You choose what the app does. Copilot helps write the code. We check the result."
Explain fields as input, Calculate as an action, and the result label as output. A small function is necessary to handle a button click; explain it as the instructions the button runs. Do not forbid functions or expect participants to memorize them.
Prompts go in Copilot Chat. Numbers go in app fields. Save and close the old window before running again.

## Fallback
If AI access fails, use the working app and guide a title or color change. For Tk/display problems, use a computer already tested rather than trying repeated code rewrites. Keep additions small. No turtle or robot activities are part of this session.
