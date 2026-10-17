# From Prompt to Program: Coding with AI

## Make It Move
**A 55-minute creative workshop with Prof. Hedhli • County College of Morris**

Create a Python animation that responds to your mouse. Start with one bouncing ball, add click interaction, then design your own visual experience.

No coding experience needed. You describe what you want to GitHub Copilot, run the program, and check what it does.

**Your starting file is my_project.py. It is intentionally empty. You create the program during the session.**

## 1 Plan and set up • 0–12 minutes

Watch the instructor's demonstration, then choose a direction:
- A calming display with slow movement and soft colors.
- A lively visual playground with bright colors and different sizes.
- A reaction challenge where clicking a moving target earns points.

Start with the same basic bouncing ball before adding your personal direction.

Clone the workshop:
1. Open VS Code.
2. Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (Mac).
3. Choose **Git: Clone** and paste:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

4. Choose a folder and select **Open**.
5. Open **my_project.py**. Do not run it until you have generated code.

If you have an earlier version of this workshop, ask the facilitator to help you clone into a fresh folder so your previous work is preserved.

## 2 Create one moving ball • 12–25 minutes

Write your own prompt in **GitHub Copilot Chat**. Include:
- Python Tkinter Canvas, using only the standard library.
- A window containing one ball that moves and bounces off every edge.
- Continuous smooth movement while the window stays responsive.
- All code in **my_project.py**.

Starter: **“Help me create a Python animation that…”**

Explain the colors and look you want. Ask Copilot to use Tkinter's after() scheduling for movement rather than a blocking animation loop.

Review and apply Copilot's edit. If it shows code only in chat, copy just the Python code into my_project.py. Save, then choose **Run Python File in Terminal**. Select the provided Python interpreter if asked.

**Check:** watch the ball reach the left, right, top and bottom edges. Does it bounce without disappearing? Can you still move or close the window?

## 3 Make it respond • 25–33 minutes

Ask Copilot to make a click inside the drawing area add another moving ball near that spot. Each ball should remain inside the canvas.

Starter: **“When I click inside the drawing area, I want…”**

**Check:** click three times. You should now see four moving balls. Click near an edge: does the new ball stay inside? Prevent unlimited spawning with a sensible limit, such as 30 balls.

## 4 Give it your style • 33–38 minutes

Choose TWO changes and describe them yourself:
- Background and ball colors.
- Ball sizes or movement speed.
- A title that fits your theme.
- A Pause/Resume button.

Keep the movement and mouse interaction working. Make one change at a time, then save and test.

**Optional direction:** turn the animation into a reaction game with one target and a score. Tell Copilot that clicking should score a hit rather than add another ball. Make this request only after the basic animation works.

## 5 Partner challenge • 38–48 minutes

Let a partner use your creation before explaining it. Switch roles.

Ask:
- What did you expect a click to do?
- Can you understand how to use it?
- Did anything disappear, freeze or behave unexpectedly?

Use their feedback to request ONE improvement from Copilot. Check the result.

**Try a specific prompt:** replace “make it better” with the exact behavior you want. For example, explain how much faster you want the ball to move and what should remain unchanged.

## 6 Show and save • 48–55 minutes

Give a 20-second demonstration: your idea, one request you made, and one thing you checked.

- [ ] I created my animation from the empty file.
- [ ] My ball bounces off every edge.
- [ ] My app responds to clicks.
- [ ] I made two personal changes.
- [ ] My partner tested it and I improved something.
- [ ] I saved my_project.py to my own approved storage.

No new repository or push to the instructor's repository is required.

## Help

After each edit: **save, close the old app window, run again, and check**. The drawing window may open behind VS Code.

Prompt starter: **“I expected… but I saw… Here is my code and the error. Help me make the smallest fix.”**

For missing Tk/_tkinter or display errors, ask the facilitator. This workshop needs desktop Python with Tk and a graphical display. No pip packages, image downloads or sound files are required.

## Files

- **my_project.py:** empty participant workspace
- **PROMPTS.md:** short prompt starters and checks
- **FACILITATOR.md:** 55-minute delivery and setup notes
- **.github/copilot-instructions.md:** friendly workshop coaching
- **.vscode:** editor setup

Earlier budget and robot handouts do not apply to this animation workshop.
