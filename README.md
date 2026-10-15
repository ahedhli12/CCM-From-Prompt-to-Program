# From Prompt to Coding: Coding with AI

**County College of Morris • Professor Amjed Hedhli**

## What is this session about?

You will learn how to describe a program to AI, run the Python code it creates, and check whether it works. No previous coding experience is required.

Our practice project is **Rock, Paper, Scissors**. You choose a move, the computer chooses a move at random, and the program announces the result. The game is a small example you can play and change during the session.

**Copilot helps write the code. Python runs the game. You decide what the game should do and check the result.** The computer's random move is not an AI prediction.

## The game rules

- Rock beats scissors.
- Scissors beats paper.
- Paper beats rock.
- Matching choices produce a tie.

Example:

```text
Choose rock, paper, or scissors: rock
You chose rock
The computer chose scissors
You win!
```

## Our 60-minute session

| Time | What we will do |
|---|---|
| 0–5 minutes | Play a live demonstration together |
| 5–15 minutes | Clone the repository and run a tiny welcome program |
| 15–25 minutes | Describe the game to Copilot and review its code |
| 25–40 minutes | Run your game and check the results with a partner |
| 40–50 minutes | Ask AI for one small change and test it |
| 50–60 minutes | Share your game and save your work |

## 1. Clone this repository

1. Open **VS Code**.
2. Press **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac.
3. Select **Git: Clone**.
4. Paste this address and press Enter:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

5. Choose a folder on your computer.
6. Select **Open** when cloning finishes.

Everyone clones the instructor's repository. You do not need to create another repository or push to this one. Ask the facilitator for help if Git, Python, or Copilot is unavailable.

## 2. Your first small success

Open **hello.py** and click **Run Python File in Terminal** at the top right. Select the provided Python interpreter if prompted.

Click in the terminal at the bottom, enter your name, and press Enter. Change the welcome message, save, and run again.

We use commas to display text and variables:

```python
print("Welcome,", name)
```

## 3. Ask AI to create your game

Open **GitHub Copilot Chat** and copy this prompt:

> I am new to Python. Create a short Rock, Paper, Scissors game in my_project.py. Ask for rock, paper, or scissors. Use random.choice() to choose for the computer. Show both choices and say whether I win, lose, or tie. Show a helpful message for an invalid choice. Use simple if/elif/else and print() with separate arguments joined by commas. Do not use f-strings, functions, classes, or loops in this first version. Explain each section in plain language.

Review the suggested code. Apply the suggested edit to **my_project.py**, or copy only the Python code from chat into that file. Save and run **my_project.py**.

**Type requests to AI in Copilot Chat. Type your game choice in the terminal.**

You can open **rock_paper_scissors.py** for a working example if you get stuck. You do not need to type the whole game from memory.

## 4. Play and check

Take turns with a partner. Play three rounds by running the file again after each round. For each round, compare the displayed choices against the rules above. Random choices mean you may not see every possible result in three rounds.

Then type **banana** as your choice. Does the game explain which choices are allowed?

If a result looks wrong, tell Copilot what you entered, what the computer chose, and what the correct result should have been. Run again after the fix.

## 5. Request one small change

Choose one:
- Add your name to the winning message.
- Make the winning and losing messages funny.
- Accept uppercase answers such as ROCK.

Prompt:

> Add [my chosen change] to my game. Keep it simple. Use comma-separated print() arguments, not f-strings. Explain what changed and give me a test to try.

Save, run, and check the change. A score counter or play-again loop is optional only if time remains.

## 6. Share and save

Show your partner one change and explain one line of code in your own words. Save **my_project.py** to your own approved storage before leaving the training account.

## A few Python words

| Term | Meaning in our game |
|---|---|
| input() | Asks you to type a move |
| Variable | Remembers a move |
| random.choice() | Selects one move at random |
| if / elif / else | Checks which result to display |
| print() | Displays the choices and result |

## Help

If nothing happens, check whether the terminal is waiting for your answer. If changes do not appear, save and confirm you are running the correct file.

For errors, ask Copilot:

> Here is my code and the full error: [paste both]. Explain the problem in simple language and suggest the smallest fix.

The lab needs Git, Python 3, the VS Code Python extension, and Copilot access. No extra Python packages are required. Keep account credentials out of prompts and repository files.

**Workshop files:** hello.py is your warm-up, my_project.py is your workspace, rock_paper_scissors.py is a working example, and PROMPTS.md contains prompts to copy. FACILITATOR.md contains the instructor's session guide.
