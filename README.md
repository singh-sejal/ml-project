# IPL Win Predictor

This project provides a Streamlit web application that predicts the probability of an IPL team winning a match.

## Prerequisites

- Python 3.9 or newer
- Internet access for installing Python packages

## Run the application

1. Open a terminal or Command Prompt.
2. Change to the project folder:

   ```powershell
   cd "D:\semester5\data science ibm\ml-project"
   ```

3. Install the required packages:

   ```powershell
   pip install streamlit pandas scikit-learn
   ```

4. Start the web application:

   ```powershell
   streamlit run app.py
   ```

5. Open a web browser and visit:

   ```text
   http://localhost:8501
   ```

Streamlit also prints the local and network URLs in the terminal. To stop the application, press `Ctrl+C` in the terminal.

## Using the predictor

1. Select the batting team and bowling team.
2. Select the host city.
3. Enter the target, current score, completed overs, and wickets lost.
4. Click **Predict Probability** to display the win probabilities.
