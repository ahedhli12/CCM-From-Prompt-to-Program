# From Prompt to Program: Coding with AI

**A 55-minute workshop with Prof. Hedhli • County College of Morris**

## Build a real app window

Create an **Event Budget Planner** with text fields, a Calculate button, and a result that shows whether your event fits your budget.

No programming experience needed. You will describe an app to GitHub Copilot, run the Python code, check its answer, and request one improvement. You do not need to understand every line.

**The challenge: plan an event for 20 people with $300.**

## 1 Clone this repository

1. Open VS Code.
2. Press **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac.
3. Choose **Git: Clone** and paste:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

4. Choose a folder, then select **Open**.

Everyone clones the same instructor repository. No new repository or push is required.

## 2 Try the working app

Open **my_project.py** and select **Run Python File in Terminal**. Choose the provided Python interpreter if asked. A separate app window opens, possibly behind VS Code.

Click **Calculate my event** with the sample values:
- 20 attendees
- $10 food per person
- $50 supplies
- $300 budget

**Expected result: $250 total and $50 remaining.**

Try $15 food per person. The total should be **$350**, which is **$50 over budget**.

The file already contains a working example so you can see the goal. You will use a prompt to recreate or change it, then compare the result. Close the app window before running again.

## 3 Your app prompt

Open **GitHub Copilot Chat** and paste:

> I have never programmed before. In my_project.py, create a small Python Tkinter event budget app. Include labeled fields for number of attendees, food cost per person, supplies cost, and available budget. Add a Calculate button. Show the total cost and how much is left or how far over budget I am. Start with 20 attendees, $10 food per person, $50 supplies, and a $300 budget. Handle blank, nonnumeric, negative, and non-finite input with a helpful message. Require at least one attendee. Use only the standard library, a readable window, clear variable names, and brief comments. Explain how to run it in VS Code. If you use print(), separate arguments with commas, not f-strings.

Copilot may suggest replacing the current example. Review and apply that edit to **my_project.py**, or copy only the Python code into the file if it appears only in chat. Save, close the old app, and run again.

**Prompt = your request. Program = the Python code. App = the window you use.** Copilot helps write the code; Python calculates the budget.

## 4 Check it works

Try both examples above. Then try a word or blank field. Your app should explain what needs fixing instead of stopping with an error.

Type requests to AI in **Copilot Chat**. Type event numbers into the **app's fields**.

## 5 Make it useful to you

Choose ONE change:
- Give the app your event's name and chosen colors.
- Add a result showing the cost per attendee.
- Add a Clear button.

Copy:

> Update my_project.py to [my chosen change]. Keep the existing calculation and input checks working. Explain what changed and give me one test.

Save, close the old window, run, and check.

## 6 The $300 partner challenge

Pick an event: a student club meetup, faculty workshop, or celebration. Keep 20 attendees and the $300 limit. Choose food and supply costs that fit. Take turns changing the numbers.

In 20 seconds, share your event, total cost, and one change you asked AI to make.

## Completion checklist

- [ ] I ran the app and checked the $250 example.
- [ ] I tested an over-budget plan.
- [ ] I requested one change and checked it.
- [ ] I saved my_project.py to my own approved storage.

## Our 55 minutes

| Minutes | Activity |
|---|---|
| 0–5 | Live app demonstration |
| 5–15 | Clone and run the example |
| 15–25 | Use the app prompt in Copilot |
| 25–35 | Check calculations and unexpected input |
| 35–45 | Make one personal improvement |
| 45–55 | Partner challenge, sharing, and saving |

## Help

Save before running. Close the previous app window first. If no window appears, look behind VS Code and ask the facilitator.

For a code problem, copy this into Copilot:

> I expected [result], but got [actual result]. Here is my code and full error: [paste]. Help me make the smallest fix and explain it simply.

Missing Tk/_tkinter or display errors need facilitator setup help. Use desktop Python with Tk support, not a terminal-only remote environment. No pip packages are needed.

**Files:** my_project.py is the only Python file. PROMPTS.md contains copyable prompts and FACILITATOR.md contains the instructor guide. This activity uses Tkinter, with no turtle graphics.
