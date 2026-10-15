# Event Budget Planner prompts

Use these requests in GitHub Copilot Chat. Make one change at a time in my_project.py. Review and apply the edit, save, close the old app window, and run again.

## Build the app
I have never programmed before. In my_project.py, create a small Python Tkinter event budget app. Include labeled fields for number of attendees, food cost per person, supplies cost, and available budget. Add a Calculate button. Show the total cost and how much is left or how far over budget I am. Start with 20 attendees, $10 food per person, $50 supplies, and a $300 budget. Handle blank, nonnumeric, negative, and non-finite input with a helpful message. Require at least one attendee. Use only the standard library, a readable window, clear variable names, and brief comments. Explain how to run it in VS Code. If you use print(), separate arguments with commas, not f-strings.

## Personalize
Change my app's title to [event name] and its main colors to [colors]. Keep the budget calculation and input checks working.

## One useful feature
Add [cost per attendee / a Clear button] to my app. Keep the existing features working. Explain the change and give me one test.

## Understand
Explain in everyday language what happens when I click Calculate. Show me where attendees times food cost plus supplies is calculated. Do not change the file.

## Fix
I entered [values]. I expected [result] but got [actual result]. Here is my code and any error: [paste]. Explain the cause and help me make the smallest fix.

## Check
Give me two sets of sample numbers with the expected totals so I can check my app. Use easy arithmetic.
