import pickle

#doc_new = ['obama is running for president in 2016']
'''
var = input("Please enter the news text you want to verify: ")
print("You entered: " + str(var))

'''
#function to run for prediction
def detecting_fake_news(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    return prediction, prob

'''
if __name__ == '__main__':
    detecting_fake_news(var)
'''