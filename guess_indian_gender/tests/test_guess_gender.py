from guess_indian_gender.guess_gender import IndianGenderPredictor

predictor = IndianGenderPredictor()


class TestIndianGenderPredictor():

    def test_gender_predictor(self):
        assert predictor.predict("adhithyan") == "male"
        assert predictor.predict("arun") == "male"
        assert predictor.predict("poorani") == "female"
