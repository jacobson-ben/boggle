from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""
        with self.client as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            self.assertIn('<button class="word-input-btn">Go</button>', html)

            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:
            response = client.get('/api/new-game')
            data = response.json
            print(data)
            self.assertIn("gameId", data)
            self.assertIn("board", data)
            self.assertIn(games['game_id'], games)
            # write a test for this route
    

    def test_score_word(self):
        """Test scoring a word"""

        with self.client as client:
            response = client.get('/api/new-game')
            gameId = response.json["gameId"]
            word = response.json["word"]
            
            response = client.post('/api/score-word', json = {'game_id': gameId, 'word': "dog"})
            json = response.json

            self.assertEqual(json, {'result': 'ok'})
            



