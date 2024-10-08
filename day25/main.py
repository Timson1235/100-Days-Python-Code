import turtle
import pandas as pd

# Setup screen
screen = turtle.Screen()
screen.title("USA Staaten")

# Add the map image
image = r"C:\Users\TimPr\100-Days-Python-Code-2\day25\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Read the CSV file
df = pd.read_csv(r"C:\Users\TimPr\100-Days-Python-Code-2\day25\50_states.csv")
states_guessed = []

# Function to update the title with the score
def update_title(score, total):
    screen.title(f"Guess the State - {score}/{total} States Correct")

# Initialize score
score = 0
total_states = len(df)

# Main game loop
while score < total_states:
    update_title(score, total_states)
    answer_state = screen.textinput(title=f"Guess the State - {score}/{total_states} States Correct", prompt="What's another state?")

    if answer_state is None:  # if the user closes the input box
        break
    
    answer_state = answer_state.title()

    if answer_state.lower() in df['state'].str.lower().values:
        if answer_state.lower() not in [state.lower() for state in states_guessed]:
            state_data = df[df['state'].str.lower() == answer_state.lower()].iloc[0]
            x, y = state_data['x'], state_data['y']
            
            # Create a new turtle to write the text
            writer = turtle.Turtle()
            writer.hideturtle()
            writer.penup()
            writer.goto(x, y)
            writer.write(answer_state, align="center", font=("Arial", 12, "normal"))
            
            states_guessed.append(answer_state)
            score += 1
            update_title(score, total_states)
        else:
            print(f"You've already guessed {answer_state}. Try another state.")
    else:
        print(f"{answer_state} is not a valid state.")

# Determine missed states
missed_states = [state for state in df['state'] if state.lower() not in [state.lower() for state in states_guessed]]

# Save missed states to CSV
missed_states_df = pd.DataFrame(missed_states, columns=["Missed States"])
missed_states_df.to_csv("day25\missed_states.csv", index=False)

# Keep the window open
turtle.mainloop()
