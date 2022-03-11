# Text Classification-Dialect Prediction

- **Dataset of tweets** belonging to a wide range of country-level Arabic dialects - covering **18 different countries** in the Middle East and North Africa region.his dataset relies on applying multiple filters to identify users who belong to different countries based on their account descriptions and to eliminate tweets that are either written in Modern Standard Arabic or contain inappropriate language. The resultant dataset contains **490k tweets** from **2,525 users** who are evenly distributed across 18 Arab countries.** 

- For more inforamtion about the data, Check this [Link](https://arxiv.org/pdf/2005.06557.pdf) 
----------------------------------------------------
#### Introduction about this project:

>In this project,  an **arabic dataset** ,contains two columns ids and dialects (you can find the file dialect_dataset.csv in data folder above ), was provided and required to use **ML** Model and **Deep Leaning** Model to predict the dialect given the arabic text.  
 
> **These **steps** were followed in getting app done:**
- [x] Get the data by calling company **API** with request body list of strings ids of dialect to get the **texts**.
- You could check this step in `..//Data fectching script/getfull_df.ipynb`
- [x] Do some **preprocessing** on the text by cleaning it from emojis, punctuations and English words.
- You could check this step in `..//Data pr-processing script/preprocessing.ipynb
- [x] **Training** Deep Learning Model **FC Dense** Layer and train ML Model **Multinomial Naive Bayes**
<span style="color:red">NOTE:
•  Due to large amount of the proccessed data as tfidf will need large Ram the 1/3 size of actual volume of data was used in training so Overfitting will appear in these notebooks
•  Recommended to run it in (google colab pro or premuim aws or google cloud with all data to get better accuracy)
 </span>.
- You can check this step in `..//Model Training script/ML_Model.ipynb` and `..//Model Training script/Deep_Learning.ipynb`

- [x] Deployment of ML and Deep Learning Model using **Flask**.
-You can check this step in `..//Deployment script/App_Deep_Learning`
 and `..//Deployment script/APP_ML`
 
--------------------------------------------------
### How to get this app work !!!?
![this iamge](https://drive.google.com/uc?export=view&id=1iajUDw40uR6yyAQYowRNsjsUk4PLODs7)

------------------------------------------------------
##### **First**: Install some required libraries:
```shell
pip install -r /path/to/requirements.txt
```
-------------------------------------------------
##### **Second**: to run ML_APP:
```shell
python ..//Deployment script//APP_ML//app_ml.py
```
-----------------------------------------------
##### **Third**: to run Deep Learning APP:
```shell
python ..//Deployment script//APP_ML//app_deeplearning.py
```
---------------------------------------------
**THANKS**
FOR ANY QUESTION, Contact with me via **Email**: 
- [x] `abdelrahmanaahmed1@gmail.com` 