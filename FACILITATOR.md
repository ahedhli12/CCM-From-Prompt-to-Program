# From Prompt to Program facilitator guide

## Final activity
Save the Ball: prevent one moving ball from touching any boundary by clicking it. A hit gives one point, returns it to the center and chooses a new direction at the same slow speed. A miss does nothing. Any boundary contact ends the game. Play Again resets score, position and original speed.

This is a single 55-minute session for adults who have never programmed. Keep my_project.py empty. Participants create their code with GitHub Copilot using the participant guide and PROMPTS.md.

## Before the session
Test Git, GitHub Copilot access, the Python extension, desktop Python/Tkinter and the separate game window on the actual lab image and accounts.
Make your own tested demo separately. Do not put completed code in the participant starting file.
Confirm that applying edits, running, closing and rerunning work. No pip packages, assets or sound files are needed.

## Delivery
Start by playing your demo with the room. Explain the goal and show where to type a prompt in GitHub Copilot Chat.
Guide participants through cloning, opening the empty file, creating the initial moving ball, adding hit scoring and adding Play Again.
Then let them choose colors or difficulty, swap with a partner, request one improvement and share.
The participant handout has no task timings or fill-in blanks. Keep the pace flexible within 55 minutes and leave time to save.
Explain only what they need to do next. They do not need to understand functions, Canvas, after() or all generated code. Technical terms belong in your support notes rather than their required prompts.

## Checks
- Without clicks, any part of the ball reaching any of the four boundaries triggers Game Over.
- Clicking inside the circle during play adds exactly one point and recenters it.
- Background clicks and all clicks after Game Over add no points.
- One ball remains throughout; clicks do not spawn additional balls.
- Play Again resets the score and speed, with only one animation timer running.
- Color and size changes preserve visibility, accurate hit detection and boundary checks.
- The window stays responsive and closes normally.

## Support
Missing Tk/_tkinter or display problems require setup help rather than repeated code rewrites.
For GitHub Copilot access trouble, pair with a working account. Use your local demo for recovery if needed.
Keep participant work in my_project.py. Save to personal approved storage outside temporary training accounts. No push to your repository is required.
