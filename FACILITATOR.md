# From Prompt to Program facilitator guide

## Goal
A 55-minute workshop for adults who have never programmed. Participants CREATE an app from the empty my_project.py through three prompts. Do not distribute a completed app as their starting file.

## Setup
Test desktop Python with Tk support, Git, VS Code Python extension and Copilot using the actual training image/accounts. No pip packages are needed. Confirm a Tk window opens and closes. Keep credentials separate.

## 55 minutes
0–5: Demonstrate the completed reference from instructor/event_budget_reference.py on your screen only. Explain the goal: describe an app, run it, check it, improve it.
5–12: Clone the repository and open the empty my_project.py. Do not ask them to run it before generating code.
12–27: Use prompt 1 to create only attendees, food cost and Calculate. Apply the code and run it. Check 20 times 10 equals $200.
27–37: Use prompt 2 to add supplies. Check 20 times 10 plus 50 equals $250.
37–47: Personalize title/colors, then pair up to plan for 20 people with $300. The required app does not have a budget field; partners compare the total to $300 themselves.
47–55: Share apps briefly and save my_project.py to personal approved storage.

## Teaching
Prompts go in Copilot Chat; numbers go in app fields. A button callback means the instructions that run when clicked. Explain one relevant line at a time. Let AI provide code and learners choose behavior and check results. Use short adult-appropriate encouragement. No robot or turtle activities.

## Backup
The instructor/event_budget_reference.py is a completed reference with supplies and budget-limit features. It is for your demo or recovery only and is not the staged assignment starting point. If AI access fails, pair participants with a working account. Use the reference only if needed, and explain that it has more features than the first-stage task.
If someone already edited a previous clone, use a fresh folder instead of discarding their work.

## Check
Stage 1: 20 attendees, $10 food gives $200.
Stage 2: add $50 supplies for $250; $80 supplies gives $280.
Try blank, word, negative or non-finite costs and zero attendees. Expect helpful feedback.
Do not require a budget-limit feature, cost per person, or Clear button. Available-budget feedback is optional only if time remains.
