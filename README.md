# From Prompt to Program: Coding with AI

**County College of Morris**  
**Professor Amjed Hedhli**

No programming experience needed. Today you will use AI to help create a funny Python story, run it, and make it your own.

## Our project: Silly Campus News

Imagine arriving at CCM with a talking penguin and opening a restaurant that serves only tacos. Your program turns three answers into a silly news story.

You only need **one Python file: my_project.py**.

Example:

```text
Enter a made-up name: Captain Noodle
Enter an animal: penguin
Enter a food: tacos

BREAKING NEWS FROM CCM!
Captain Noodle arrived on campus with a talking penguin
They opened a restaurant that serves only tacos
The college president ordered 100 plates!
```

The story is fictional. There is no right or wrong funny answer.

## What does From Prompt to Program mean?

A **prompt** is a request you give AI. A **program** is code you run on your computer.

You describe the story you want in Copilot Chat. Copilot suggests Python code. You run the code and see whether the story matches your idea.

**Your job today:** choose the idea, try the program, and tell AI what you want to change.

## 1. Clone the workshop repository

Follow along with the facilitator:

1. Open **VS Code**.
2. Press **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac.
3. Select **Git: Clone**.
4. Paste this address and press Enter:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

5. Choose a folder on your computer.
6. Select **Open** when cloning finishes.

Cloning copies the workshop files to your computer. Everyone uses this same repository. Ask the facilitator for help with setup.

## 2. Play with the starter story

1. Open **my_project.py** in the file list on the left.
2. Click **Run Python File in Terminal** at the top right. If asked, select the Python interpreter provided for the session.
3. Click in the **terminal** at the bottom of VS Code.
4. Type an answer to each question and press **Enter**.
5. Read your silly news story!

Run it again with different answers. Compare your story with a partner.

## 3. Give AI your idea

Choose a new setting:

- A restaurant on the moon.
- A zoo run by students.
- A superhero's first day at CCM.
- Your own silly idea.

Open **GitHub Copilot Chat** and paste this prompt, replacing the words in brackets:

> I have never programmed before. Change my_project.py into a short, funny story about [my idea]. Keep the three questions about a made-up name, an animal, and a food. Use only input(), variables, and print(). Use separate print() arguments with commas, not f-strings. Keep the program under 12 lines. Explain the changes in simple language.

If Copilot suggests an edit, review and apply it. If it displays code only in chat, copy just the Python code into **my_project.py**. Save the file.

**Prompts go in Copilot Chat. Answers to the story questions go in the terminal.**

## 4. Run your new story

Run **my_project.py** again and answer the questions.

Check:
- Does the story use the name, animal, and food you typed?
- Does it use your chosen setting?

If it does not, tell Copilot what you wanted and what actually happened.

## 5. The funny ending challenge

Ask your partner to suggest a surprising ending. Then ask Copilot:

> Change only the last line of my story to [our funny ending]. Keep the code simple and use commas in print().

Save and run again. Share your favorite story with the room!

## Three things to recognize

| In the code | What it does |
|---|---|
| input() | Asks a question |
| A variable, such as name | Remembers an answer |
| print() | Displays the story |

For example:

```python
print("Welcome,", name)
```

This displays the word Welcome followed by the answer stored in name. You do not need to memorize the code today.

## If you get stuck

- **The program seems to stop:** it may be waiting for your answer in the terminal.
- **Your new story does not appear:** save and make sure you are running my_project.py.
- **You see an error:** ask the facilitator, or copy your code and full error into Copilot Chat:

> I am a beginner. Here is my code and error: [paste both]. Explain the problem simply and help me fix it. Keep the program short.

## Before you leave

Save **my_project.py** to your own approved storage so you keep it after leaving the training account. You do not need to create a new repository or push to the instructor's repository.

**You succeeded if you ran a story, asked AI for one change, and checked the result.**

## Session plan

| Time | Activity |
|---|---|
| 0–5 minutes | Audience supplies funny answers for a live demo |
| 5–15 minutes | Clone the repository and run the starter story |
| 15–30 minutes | Choose a setting and ask Copilot to change the program |
| 30–40 minutes | Swap answers with a partner and check the story |
| 40–50 minutes | Create a surprising ending |
| 50–60 minutes | Share stories and save your work |

The facilitator will help with Git, Python, and Copilot access. No extra Python packages are needed. More copyable prompts are in PROMPTS.md.
