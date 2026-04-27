## Heart Disease Prediction Pipeline
An end-to-end ML project using XGBoost and GridSearchCV to predict heart disease, featuring a fully automated CI/CD workflow.


* XGBoost + GridSearchCV: Automated hyperparameter tuning for peak accuracy.
* Streamlit: Interactive web interface for real-time health predictions.
* GitHub Actions: Automated testing, retraining and Containerized app.py on every push.


Run the app via Docker:

docker pull kumar2700/heartdisease-prediction:latest
docker run -p 8501:8501 kumar2700/heartdisease-prediction:latest

