# From Prompt to Coding: Coding with AI

A beginner-friendly Python workshop for students and faculty at County College of Morris.  
**Facilitator: Professor Amjed Hedhli**

No coding experience is needed. You will use GitHub Copilot to create a short program that introduces you in a funny way. Then you will change it and share your result.

## 1. Clone the repository

Everyone will clone the same workshop repository. You do not need to create a new repository, fork it, or use a template.

1. Open **Visual Studio Code**.
2. Press **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac.
3. Type **Git: Clone** and select it.
4. Paste this address and press **Enter**:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

5. Select a folder on your computer where you want to save the project.
6. When VS Code finishes cloning, select **Open** to open the project.

If you cannot find **Git: Clone**, ask the facilitator for help. The workshop computers need Git, Python 3, and the VS Code Python extension.

## 2. Run your first program

1. Open **hello.py** from the file list on the left.
2. Click the **Run Python File** triangle at the top right. If asked, select the Python interpreter provided for the session.
3. The program will ask for your name in the **terminal** at the bottom of VS Code.
4. Click in the terminal, type your name, and press **Enter**.
5. Read the message the program displays.

**Your first small change:** change the welcome message in the code. Save the file and run it again.

## 3. Create a funny introduction with AI

### What your program should do

Ask the user three questions:

- What is your name?
- What is your favorite food?
- What superpower would you like to have?

Then display a funny introduction using those answers.

**Example**

```text
What is your name? Amjed
What is your favorite food? Pizza
What superpower would you like to have? Teleportation

Meet Amjed! Fueled by Pizza and gifted with Teleportation,
Amjed is ready to save the campus!
```

Your wording can be different. The goal is to include all three answers in the introduction.

### Your prompt

Open **GitHub Copilot Chat** in VS Code and enter:

> I am new to coding. Help me create a short Python program in my_project.py. Ask for my name, favorite food, and a superpower I would like to have. Then print a funny introduction using all three answers. Use only input(), variables, and print(). Do not use loops, if statements, or external libraries. Explain the code in simple language.

1. Review the code Copilot suggests.
2. If Copilot offers an edit to **my_project.py**, review and apply it. If it only displays code in chat, copy the Python code into **my_project.py** without the surrounding code-block markers.
3. Save **my_project.py**.
4. Run the file, answer the questions in the terminal, and read your introduction.

**Where do I type?** Type requests to AI in Copilot Chat. Type answers to your running Python program in the terminal.

## 4. Make it your own

Choose **one** small change:

- Make the introduction sound like a superhero announcement.
- Change it into a funny two-line poem.
- Add a question about a favorite animal and include the answer.

Use this follow-up prompt:

> Change my program to [describe your idea]. Keep it simple, using only input(), variables, and print(). Explain what changed.

Save and run the program again. Check whether it does what you requested.

## 5. Try it with a partner

1. Run the program with your answers.
2. Run it again with your partner's answers.
3. Check that the introduction uses the new answers instead of repeating the old ones.
4. Show your partner one line of code and explain what you think it does.

**Share with the room:** read your funniest introduction and describe one change you made.

## If you get stuck

- **Nothing happens:** check whether the program is waiting for an answer in the terminal.
- **Your changes do not appear:** save the file and make sure you are running the correct file.
- **You see an error:** copy the full error into Copilot Chat with this prompt:

> I am new to Python. Here is my code and the error message: [paste both]. Explain what went wrong in simple language and help me make the smallest fix.

You can also ask the facilitator or work with a partner.

## Before you leave

- Save your completed **my_project.py** file.
- Copy it to your own approved storage so you can keep it after leaving the training account.
- You do not need to push changes to the instructor's repository.

## A few Python words

| Python term | What it means |
|---|---|
| `input()` | Asks a question and receives what you type |
| Variable | A name that holds a value, such as your favorite food |
| `print()` | Displays a message |
| Run | Starts the program |

## Workshop note

Follow the activity and prompts on **this page** for the introductory session. The adventure example and earlier adventure-based prompts, slides, and handout are optional materials for a later activity.

Use made-up information if you prefer. Review the code AI suggests and check the result by running it.
