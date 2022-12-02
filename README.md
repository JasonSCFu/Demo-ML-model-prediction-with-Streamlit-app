## Streamlit demo for ML model prediction

Streamlit is a very convenient tool to showcase the ML model result to the non-technical business stakeholders.
With its user friendly UI, stakeholders can easily understand what the expected output is in the PoC stage.
In this repo, I will show how to use some basic functions of Streamlit to achieve this goal.


### UI Demo
![alt text](https://github.com/JasonSCFu/Demo-ML-model-prediction-with-Streamlit-app/blob/main/GIF/GIF.gif)



You can click this [link](https://jasonscfu-demo-ml-model-prediction-with-streamlit-testml-dzr840.streamlit.app/) to visualize the app.


### Installation
- pip install streamlit
- pip install scikit-learn
- pip install matplotlib



### Step to create this streamlit interface
1. Use Logistic Regression Employee Analytics Streamlit.ipynb to create and save the model. The model is saved as emp-model.pkl. We built a toy model for demo purpose, the focus is not on modelling part.
2. Create a streamlit interface to interact with our pickle file.
3. Get model results from the streamlit interface.
4. Run streamlit run main.py in terminal to deploy the streamlit app.

