from flask import Flask ,request,render_template
import pickle 
from sklearn.fearture_extraction.text import TfidfVectorizer

vector=TfidfVectorizer(stop_word='english',max_df=0.7)
