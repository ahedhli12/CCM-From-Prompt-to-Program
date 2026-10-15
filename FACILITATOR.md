# From Prompt to Program robot workshop

## Purpose
First-time programmers describe a robot to Copilot, run Python to see the result, and check small changes. Success means a visible robot with chosen colors and one personal detail. Participants use only my_project.py.

## Required setup check
On the actual lab image and training accounts, run my_project.py in local desktop VS Code. Confirm that the turtle/Tk window opens, the robot appears, and closing the window allows another run. Check Git, Python extension, Copilot access and the selected interpreter. No pip packages are needed, but Python must include Tk and a graphical display. If graphics fails, resolve it before the workshop or pair participants at a working computer. Do not substitute a terminal-only or notebook runner without checking turtle support.

## 60 minute flow
0–5: Show the starter robot. Ask what colors or funny details the audience would choose.
5–15: Clone your repository together. Open my_project.py, run it, and find the drawing window.
15–25: Use prompt 1 in PROMPTS.md to create a robot with AI. Review and apply the edit, save, run, and compare the image against the requested parts.
25–35: Use prompt 2 with chosen colors. Explain that participants control the design. Show color() as one small readable command.
35–45: Add one detail with prompt 3. Keep requests small and inspect the result.
45–55: Partners request one surprise change, then share a 20-second robot introduction.
55–60: Complete the handout checklist and save my_project.py to personal approved storage. No push to your repository is needed.

## Teaching notes
Explain prompt as a request and program as runnable instructions. AI generates code, and turtle draws from that code. The picture is a Python drawing, not an AI-generated image. Distinguish Copilot Chat, the editor and the separate drawing window. Close the drawing window before rerunning. Avoid requiring participants to memorize coordinates, loops or syntax.

The provided robot is a working fallback if AI access fails. Participants can change color names directly with guidance. Ask for the exact error before debugging. Restrict additions to a hat, antenna, balloon or similarly small detail. Keep turtle.done() last and penup() before repositioning without a line.

## Assignment
A visible robot, a color change, one fun detail, a check against the prompt, and a saved Python file. Let participants say a robot name aloud instead of adding text to code.
