import pickle
import pandas as pd
import re

def processing_Data(text):
    with open("E:\\AIM_APP\\Any additional files\\Models\\vectorizer.pickle", 'rb') as handle:
        vectorizer = pickle.load(handle)
    


    my_df_text=pd.DataFrame({"new_text":[text]})
    my_df_text["new_text"]=my_df_text["new_text"].apply(lambda x:re.sub('[a-zA-Z0-9_]|#|@|http\S+', '',x))
    my_df_text["new_text"]=my_df_text["new_text"].apply(lambda x:re.sub("\W+"," ",x))
    my_df_text["new_text"]=my_df_text["new_text"].apply(lambda x:x.strip())
    
    my_df_text=my_df_text["new_text"].astype("U").tolist()


    features = vectorizer.transform(my_df_text)
    features=features.toarray()

    return features
