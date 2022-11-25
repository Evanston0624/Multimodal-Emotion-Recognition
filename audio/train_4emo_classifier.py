from emotion_recognition import EmotionRecognizer
import pickle
from sklearn.svm import SVC

load_model = pickle.load(open('./grid/cp_best_classifier.pickle', 'rb'))

rec = EmotionRecognizer(model=load_model, emotions=['sad', 'neutral', 'happy','angry'], balance=True, tess_ravdess=True,emod=True,custom_db=True,features=["mfcc","mel"],verbose=1)

rec.determine_best_model(train=True)

print(rec.model.__class__.__name__, "is the best")
# get the test accuracy score for the best estimator
print("Test score:", rec.test_score())
print("Train score:", rec.train_score())

save best 4 emo model
with open('./best_4emo_model/4emo_classifier.pickle','wb') as  f:
    pickle.dump(rec.model,f)
