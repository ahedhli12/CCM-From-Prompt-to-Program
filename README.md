# From Prompt to Program: Coding with AI

**Create Your Own Event Budget App**  
A 55-minute CCM workshop with Prof. Hedhli

You will create a small graphical Python app using GitHub Copilot. **my_project.py starts empty.** Your prompts will turn it into a window with input fields, a Calculate button, and a result.

No programming experience needed. You choose what the app should do, Copilot helps write the code, and you run it to check the answer.

## Your assignment

Build an app in small stages:
1. Calculate food costs for an event.
2. Add supplies costs.
3. Give it your event's name and colors.
4. Check it and show a partner.

Use only **my_project.py** for your work. You do not need to write the code from memory.

## 1 Clone and open

1. Open VS Code.
2. Press **Ctrl+Shift+P** (Windows) or **Cmd+Shift+P** (Mac).
3. Choose **Git: Clone** and paste:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

4. Choose a folder, then select **Open**.
5. Open **my_project.py**. It is intentionally empty. Do not run it yet.

If you cloned an older workshop version, ask the facilitator to help you get a fresh copy in a new folder so your existing work is preserved.

## 2 Create your first version

Open **GitHub Copilot Chat** and copy this prompt:

> I have never programmed before. Create my first version in the empty my_project.py file. Use Python Tkinter to open an Event Budget Planner window with two labeled input fields: number of attendees and food cost per person in dollars. Add a Calculate button that displays attendees times food cost as a dollar amount. Keep the interface readable and the code straightforward with brief comments. Show a helpful message for blank, nonnumeric, negative, or non-finite input, and require at least one attendee. Use only the standard library. Do not add supplies, a budget limit, or extra features yet. Explain how to apply the code and run the file in VS Code. If print() is needed, use comma-separated arguments, not f-strings.

Copilot will suggest code:
1. Review and apply the suggested edit to **my_project.py**. If it only displays code in chat, copy just the Python code into your file.
2. Save the file.
3. Select **Run Python File in Terminal** at the top right.
4. If asked, choose the provided Python interpreter.
5. Look for the separate app window, which may open behind VS Code.

**Check:** enter **20** attendees and **10** dollars per person. Click Calculate. The result should be **$200**.

Prompts go in **Copilot Chat**. Event numbers go into the **app's fields**.

## 3 Add a feature through a new prompt

Close the app window, then ask Copilot:

> Add a supplies cost field to my existing app. Update Calculate to use attendees times food cost per person plus supplies. Keep the existing interface and input checks working, including checking the supplies input. Explain what changed and give me one test.

Review and apply the edit, save, and run again.

**Check:** 20 attendees, $10 food per person, and $50 supplies should give **$250**.

Try changing supplies to $80. The total should become **$280**.

## 4 Make it yours

Choose an event: a faculty workshop, club meetup, community gathering, or celebration. Replace the brackets in this prompt:

> Personalize my app for [my event name]. Change the window title and use [my chosen colors]. Keep the fields, calculations, and input checks working. Explain the changes briefly.

Save, close the old app window, and run again. Check that your title and colors changed and the $250 example still works.

## 5 The $300 partner challenge

Imagine you have **$300 for 20 people**. Your app does not need a budget-limit feature. Use its total to find a plan that fits.

Take turns choosing food and supplies costs. Can you stay at or below $300? Tell your partner what the total should be before clicking Calculate.

Then try a blank field or the word **pizza** in a number field. Does your app show a helpful message? If not, ask Copilot to fix it.

## 6 Share and save

In 20 seconds, show your app, name your event, and explain one change you requested.

- [ ] I created an app from the empty file using a prompt.
- [ ] I checked the first $200 calculation.
- [ ] I added supplies and checked the $250 calculation.
- [ ] I personalized the app and tested it again.
- [ ] I saved my_project.py to my own approved storage.

No new repository or push to the instructor's repository is required.

## Help prompt

> I entered [values]. I expected [result], but got [actual result]. Here is my code and any error: [paste]. Help me make the smallest fix and explain it simply.

Save before running and close the previous app window before starting again. If Python reports missing Tk/_tkinter or no display, ask the facilitator for setup help.

## Our 55 minutes

| Minutes | Activity |
|---|---|
| 0–5 | Instructor shows the goal and explains prompts |
| 5–12 | Clone and open the empty file |
| 12–27 | Create the first app and check $200 |
| 27–37 | Add supplies and check $250 |
| 37–47 | Personalize and try the partner challenge |
| 47–55 | Share and save |

**Facilitator:** test desktop Python/Tk, Git, the Python extension, and Copilot on the lab computers beforehand. No pip packages are needed. FACILITATOR.md includes a backup plan. The instructor folder contains a finished reference, not the participant starting point.
