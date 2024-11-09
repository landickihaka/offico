import pickle

def serialize_example(priors, forecasts):
    serialized_data = {'priors': priors.tolist(), 'forecasts': forecasts.tolist()}
    with open('serialized_example.pkl', 'wb') as f:
        pickle.dump(serialized_data, f)
