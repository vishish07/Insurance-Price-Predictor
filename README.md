# Insurance Price Prediction App

This project is a web application for predicting insurance prices based on various user inputs. The application uses a Random Forest Regressor model, which is trained on preprocessed insurance data. The web app is built with Flask, HTML, and Bootstrap for a modern and responsive user interface.
## Website Link

You can access the website here: [Insurance Price Web Application](https://web-application-insurance-price.onrender.com)

## Project Structure

- **app.py**: Flask application to handle form submissions and model predictions.
- **templates/**: Directory containing HTML templates for the web pages:
  - `index.html`: Main page with the prediction form.
  - `about.html`: About page with information about the developer.
  - `contact.html`: Contact page with links to LinkedIn, GitHub, and Instagram.
- **static/**: Directory containing static files such as images and CSS.
  - `student-image.jpg`: Image of the student (replace with actual image).
  - `linkedin-icon.png`, `github-icon.png`, `instagram-icon.png`: Social media icons.
- **model.pkl**: Pickle file containing the trained Random Forest model.
- **requirements.txt**: List of Python packages required for the project.
- **README.md**: This file.

## Features

- **Insurance Price Prediction**: Users can input their details to get a prediction of their insurance charges.
- **Responsive Design**: The web application is styled using Bootstrap with a dark theme and rainbow gradient text.
- **Social Media Links**: Contact page with links to LinkedIn, GitHub, and Instagram.

## Setup Instructions

1. **Clone the Repository**

   bash
   git clone insurance-price-prediction
   

2. **Install Dependencies**

   Ensure you have Python 3.7 or higher installed. Create a virtual environment and install the required packages:

   bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   pip install -r requirements.txt
   

3. **Prepare the Model**

   Ensure that `model.pkl` is present in the root directory. This file should contain the trained Random Forest Regressor model. If not present, you can create it by running the following script:

   python
   import pandas as pd
   from sklearn.preprocessing import StandardScaler
   from sklearn.ensemble import RandomForestRegressor
   from sklearn.model_selection import train_test_split
   import pickle

   # Load dataset
   df = pd.read_csv("insurance.csv")

   # Convert categorical columns to integers
 ```
   df['sex'] = df['sex'].map({'male': 1, 'female': 0})
   df['smoker'] = df['smoker'].map({'yes': 1, 'no': 0})
   df['region'] = df['region'].map({
       'northeast': 1,
       'northwest': 2,
       'southeast': 3,
       'southwest': 4
   })
```
   # Features and target
```
   x = df.drop(columns='charges')
   y = df['charges']

   # Split the dataset
   x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

   # Standardize features
   sc = StandardScaler()
   x_train = sc.fit_transform(x_train)
   x_test = sc.transform(x_test)
```
   # Train Random Forest model
 ```
   regressor_rf = RandomForestRegressor()
   regressor_rf.fit(x_train, y_train)
```
 # Save the model
pickle.dump(regressor_rf, open("model.pkl", "wb"))
  

4. **Run the Application**
```
   Start the Flask application:

   bash
   python app.py
   

   Open your browser and go to `http://127.0.0.1:5000` to access the application.
```
## Usage

1. **Home Page**

   - Input age, BMI, number of children, sex, smoking status, and region into the form.
   - Submit the form to get a prediction of the insurance charges.

2. **About Page**

   - Provides information about the developer and their interest in data science and machine learning.

3. **Contact Page**

   - Contains links to LinkedIn, GitHub, and Instagram profiles.

## Random Forest Model

The Random Forest Regressor model is used to predict insurance charges based on input features. The model was trained on a dataset after preprocessing, including:

- Converting categorical columns ('sex', 'smoker', and 'region') to numerical values.
- Standardizing features using `StandardScaler`.
- Training the Random Forest Regressor on the preprocessed data.

The trained model is saved as `model.pkl` and loaded into the Flask application for making predictions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Bootstrap for styling the web pages.
- Flask for building the web application.
- Scikit-learn for the Random Forest Regressor model.
