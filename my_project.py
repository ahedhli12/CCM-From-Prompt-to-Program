# A ready-to-run robot. Ask Copilot to help you change it.
import turtle

screen = turtle.Screen()
screen.title("From Prompt to Program - My Robot")
screen.setup(700, 600)
screen.bgcolor("white")

robot = turtle.Turtle()
robot.speed(0)
robot.penup()
robot.shape("square")

# Head
robot.color("skyblue")
robot.shapesize(3, 3)
robot.goto(0, 95)
robot.stamp()

# Body
robot.color("orange")
robot.shapesize(4, 4)
robot.goto(0, 0)
robot.stamp()

# Arms
robot.color("slategray")
robot.shapesize(1, 2)
robot.goto(-65, 10)
robot.stamp()
robot.goto(65, 10)
robot.stamp()

# Legs
robot.shapesize(2, 1)
robot.goto(-22, -60)
robot.stamp()
robot.goto(22, -60)
robot.stamp()

# Eyes and a smile
robot.goto(-15, 100)
robot.dot(10, "black")
robot.goto(15, 100)
robot.dot(10, "black")
robot.goto(-15, 80)
robot.pencolor("black")
robot.pensize(3)
robot.pendown()
robot.goto(15, 80)
robot.penup()
robot.hideturtle()

# Keep the drawing window open.
turtle.done()
