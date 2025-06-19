from django.db import models
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


import numpy as np
import pickle

import json
from PIL import Image


# Testing phase
xgb = pickle.load(open(r"C:\Users\dinnu\Documents\WHATSAPP_CHAT\FRONTEND\xgboost_model.pkl", 'rb'))
lgbm = pickle.load(open(r"C:\Users\dinnu\Documents\WHATSAPP_CHAT\FRONTEND\lgbm_model.pkl", 'rb'))
lstm = pickle.load(open(r"C:\Users\dinnu\Documents\WHATSAPP_CHAT\FRONTEND\xgboost_model.pkl", 'rb'))

tfidf_feature = pickle.load(open(r"C:\Users\dinnu\Documents\WHATSAPP_CHAT\FRONTEND\count_vect.pkl", 'rb'))


def predict(text,algo): 
	#text = [text]
	filter_text = tfidf_feature.transform(text)
	print(filter_text.shape)
	if algo=='xgb':
		y_pred=xgb.predict(filter_text)
		return y_pred[0]
	if algo=='lgbm':
		y_pred=xgb.predict(filter_text)
		return y_pred[0]
	else:
		y_pred=lstm.predict(filter_text)
		return y_pred[0]

