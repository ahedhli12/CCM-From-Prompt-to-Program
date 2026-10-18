# From Prompt to Program: Coding with AI

## Save the Ball
**With Prof. Hedhli • County College of Morris**

Create your own Python game with **GitHub Copilot**. No programming experience needed.

**The goal:** save the moving ball from touching the boundaries of the game area.
- Click inside the ball to earn one point, return it to the center, and send it in a new direction.
- Clicking the background does nothing.
- When any part of the ball touches a boundary, the game ends.
- Play Again starts a fresh game with zero points.

**my_project.py is intentionally empty. You create the game through prompts.**

## 1 Open your project

1. Open VS Code.
2. Press **Ctrl+Shift+P** on Windows or **Cmd+Shift+P** on Mac.
3. Choose **Git: Clone** and paste:

   ```text
   https://github.com/ahedhli12/CCM-From-Prompt-to-Program.git
   ```

4. Choose a folder and select **Open**.
5. Open **my_project.py**. Do not run the empty file yet.

If it already contains code from an earlier activity, ask the instructor for help getting a fresh copy without losing your work.

## 2 Ask GitHub Copilot to create the game

Open **GitHub Copilot Chat** in VS Code. A prompt is a message telling GitHub Copilot what you want.

Copy this example:

> I have never programmed before. Help me create a simple Python game in my_project.py. Show one large ball moving slowly inside a window. Start it in the center. When it touches an edge, stop the game and display Game Over. It should not bounce. Do not add points yet. Use Python’s built-in drawing tools without extra downloads. Explain how to run it in VS Code using simple steps.

Review the suggested edit and choose **Apply** or **Keep** if offered. If GitHub Copilot only shows code in chat, ask the instructor to help place it in my_project.py.

Save with **Ctrl+S** (Windows) or **Cmd+S** (Mac). Select **Run Python File in Terminal** at the top right. Ask the instructor if you are prompted to select Python.

**Try it:** the ball moves slowly and stops with Game Over when it touches a boundary. It does not bounce.

## 3 Add clicking and points

Continue in the same GitHub Copilot conversation:

> When I click the ball, give me one point, move it back to the center, and send it in a new direction at the same slow speed. Show my score. Clicking outside the ball should do nothing. Stop adding points after Game Over.

**Try it:** click the ball to earn one point. Click the background and check that no point is added.

## 4 Add Play Again

> Add a Play Again button after Game Over. It should start a new game with zero points and the ball in the center, moving at its original speed.

**Try it:** let the ball reach a boundary. Click Play Again. Check that the score resets and the ball moves at its original speed.

## 5 Make it your own

Try this example or request your own colors:

> Make the background dark blue and the ball yellow. Keep the score easy to read and keep everything else working.

For an easier game:

> Make the ball larger and move more slowly so I have more time to click it. Keep the other game rules the same.

**After every edit:** apply the changes, save, close the old game window, and run again.

## 6 Challenge a partner

Take turns playing each other's games. Can you reach five points?
Check that hits score exactly one point, misses score nothing, touching any boundary ends the game, and Play Again resets it.

Ask your partner for one improvement. Describe it to GitHub Copilot and try the change.

## 7 Show and save

Show your game and explain one change you requested. Save **my_project.py** to your own approved storage before leaving. You do not need a new repository or a push to the instructor's repository.

## Help

> I am a beginner. My game is not working as expected. Please help me fix it one step at a time. Tell me what information you need and explain it simply.

Copy any error into GitHub Copilot Chat. Look behind VS Code for a missing game window. Ask the instructor if the window does not open.

## Files

- **my_project.py:** your empty starting file
- **PROMPTS.md:** example prompts
- **handouts/CCM-Save-the-Ball-Participant-Guide.docx:** beginner directions
- **FACILITATOR.md:** instructor notes
- **.github/copilot-instructions.md:** friendly GitHub Copilot guidance
- **.vscode:** editor settings

**Instructor setup:** this activity uses desktop Python with Tkinter and a graphical display. No extra Python packages or downloaded assets are needed. Test on the workshop computers before the session.
