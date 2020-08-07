from emotion_analysis import emotion_analysis
from get_data import get_data
from participle import participle

data = get_data()
news_cut_list = participle(data)
emotion_analysis(news_cut_list)
