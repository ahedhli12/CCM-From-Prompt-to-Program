# From Prompt to Program: Coding with AI

**Design Your Own Robot**  
County College of Morris • Professor Amjed Hedhli

No programming experience needed. Give GitHub Copilot an idea, run the Python program, and watch your robot appear in a drawing window.

**Your mission:** create a robot, choose its colors, and add one fun detail. Everyone works in one file: **my_project.py**.

## 1. Clone the repository

Follow the facilitator:

1. Open **VS Code**.
2. Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (Mac).
3. Select **Git: Clone** and paste:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

4. Choose a folder and select **Open** after cloning.

Cloning copies the workshop to your computer. You do not need to create another repository.

## 2. See a robot first

Open **my_project.py** and choose **Run Python File in Terminal** at the top right. Select the provided Python interpreter if asked.

A separate window should show a blue-headed robot with an orange body. You do not need to understand every line yet.

**Close the drawing window before running the file again.** If no drawing window appears, ask the facilitator for help.

## 3. Your first prompt

Open **GitHub Copilot Chat** and copy:

> I have never programmed before. In my_project.py, use Python turtle to draw a friendly robot with a square head, a rectangular body, two eyes, arms, and legs. Use simple turtle commands and named colors. Keep the whole robot inside a 700 by 600 window. Do not use external packages, loops, custom functions, or classes. Finish with turtle.done() so the window stays open. Explain how to run it in VS Code and briefly explain the drawing sections.

Review and apply Copilot's suggested edit to **my_project.py**. If it only shows code in chat, copy only the Python code into that file. Save, then run it.

**Check:** can you see a head, body, two eyes, arms, and legs?

A prompt is your request to AI. The program is the Python code you run. Copilot helps write the instructions, and Python draws the picture.

## 4. Your colors

Copy this prompt and replace the colors if you like:

> Change only my robot's head to purple and body to orange. Keep the other parts and the drawing window the same. Explain which lines changed.

Save, close the old drawing window, and run again. Did both colors change as requested?

## 5. One fun detail

Choose **one**: a hat, an antenna, or a balloon.

> Add [a small hat / one antenna / a balloon] to my robot. Keep the existing robot and fit everything inside the window. Use simple turtle commands. Keep turtle.done() at the very end. Explain what changed.

Replace the bracketed choices with your selection. Save and run again. Can you see your new detail and the original robot?

## 6. The partner surprise

Ask your partner to suggest one small change, such as red shoes or a green hat. Describe it to Copilot in your own words. Run your code and compare the picture with the request.

Give your robot a name and introduce it in a 20-second gallery showcase. You may simply say its name aloud.

## Your assignment checklist

- [ ] I ran a robot drawing.
- [ ] I used a prompt to change its colors.
- [ ] I added one fun detail.
- [ ] I checked that the drawing matches my requests.
- [ ] I shared my robot and saved my file.

Save **my_project.py** to your own approved storage before leaving the training account. No push to the instructor repository is needed.

## If you get stuck

- Close the old drawing window before running again.
- Save and confirm you are running **my_project.py**.
- A drawing window may open behind VS Code.
- For a small drawing problem or error, ask:

> I asked for [describe my idea], but I see [describe what happened]. Here is my code and any error: [paste]. Help me make the smallest fix. Explain it in plain language.

If you see **No module named _tkinter**, **no display**, or a similar graphics setup error, ask the facilitator. You do not need to install anything yourself.

## A few drawing words

| Command | Meaning |
|---|---|
| color() | Chooses a color |
| goto() | Moves to a place in the window |
| penup() | Moves without drawing a line |
| pendown() | Draws while moving |
| stamp() | Leaves a copy of a shape |
| done() | Keeps the drawing window open |

You do not need to memorize commands. Ask Copilot to explain one line at a time. If you use print(), separate text and variables with commas rather than f-strings.

## Workshop files

- **my_project.py**: your robot and all your changes
- **PROMPTS.md**: prompts you can copy
- **FACILITATOR.md**: setup and session guide for the instructor
- **handouts/CCM-Robot-Workshop-Handout.docx**: printable participant instructions

**Setup for the facilitator:** test Python turtle and its Tk drawing window on the actual workshop computers before the session. Use local desktop Python in VS Code. This activity needs a graphical display and Tk support. It uses the Python standard library and needs no pip packages.
