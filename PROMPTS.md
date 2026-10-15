# From Prompt to Program step by step

Start with the empty my_project.py. Use ONE prompt at a time in Copilot Chat. After each edit, save, close any old app window, run, and check the result.

## 1 Create the app
I have never programmed before. Create my first version in the empty my_project.py file. Use Python Tkinter to open an Event Budget Planner window with two labeled input fields: number of attendees and food cost per person in dollars. Add a Calculate button that displays attendees times food cost as a dollar amount. Keep the interface readable and the code straightforward with brief comments. Show a helpful message for blank, nonnumeric, negative, or non-finite input, and require at least one attendee. Use only the standard library. Do not add supplies, a budget limit, or extra features yet. Explain how to apply the code and run the file in VS Code. If print() is needed, use comma-separated arguments, not f-strings.

Check: 20 attendees at $10 each gives $200.

## 2 Add supplies
Add a supplies cost field to my existing app. Update Calculate to use attendees times food cost per person plus supplies. Keep the existing interface and input checks working, including checking the supplies input. Explain what changed and give me one test.

Check: 20 attendees at $10 each plus $50 supplies gives $250.

## 3 Personalize
Personalize my app for [my event name]. Change the window title and use [my chosen colors]. Keep the fields, calculations, and input checks working. Explain the changes briefly.

Check: the title and colors change, and the $250 calculation still works.

## 4 Fix a problem
I entered [values]. I expected [result], but got [actual result]. Here is my code and error: [paste]. Help me make the smallest fix and explain it simply.

## Explain without editing
Explain what happens when I click Calculate in everyday language. Point out the calculation line. Do not change the code.

## Optional only if time remains
Add an available-budget field and display how much is left or how far over budget the event is. Preserve existing calculations and input checks. Check: a $250 total with a $300 budget leaves $50.
