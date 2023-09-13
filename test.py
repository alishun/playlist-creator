import unittest
from unittest.mock import patch
import main

class TestGenerateTopTracks(unittest.TestCase):

    def setUp(self):
        self.mock_response_1 = {'items': [{'name': 'Song1'}, {'name': 'Song2'}]}
        self.mock_response_2 = {'items': [{'name': 'Song3'}, {'name': 'Song2'}]}

    # Using mocking to prevent unstable results
    @patch('main.sp.current_user_top_tracks')
    def test_generate_short_top_tracks(self, mock_current_user_top_tracks):
        # side_effect: cycle through the two elements
        mock_current_user_top_tracks.side_effect = [self.mock_response_1]
        
        songs_generator = main.generate_top_tracks("short_term")

        actual_songs = list(songs_generator)
        expected_songs = [{'name': 'Song1'}, {'name': 'Song2'}]
        self.assertEqual(actual_songs, expected_songs)

    @patch('main.sp.current_user_top_tracks')
    def test_generate_medium_top_tracks(self, mock_current_user_top_tracks):
        # side_effect: cycle through the two elements
        mock_current_user_top_tracks.side_effect = [self.mock_response_2]
        
        songs_generator = main.generate_top_tracks("medium_term")

        actual_songs = list(songs_generator)
        expected_songs = [{'name': 'Song3'}, {'name': 'Song2'}]
        self.assertEqual(actual_songs, expected_songs)

    # Testing the actual API data, can compare with StatsForSpotify
    def test_generate_real_top_tracks(self):
        short_songs_generator = main.generate_top_tracks("short_term")
        medium_songs_generator = main.generate_top_tracks("medium_term")
        print("TOP TRACKS (4 WEEKS)")
        for track in short_songs_generator:
            print(track['name'])
        print("\nTOP TRACKS (6 MONTHS)")
        for track in medium_songs_generator:
            print(track['name'])

    def test_generate_real_combined_tracks(self):
        print("TOP TRACKS (4 WEEKS, 6 MONTHS COMBINED)")
        for track in main.generate_combined_top_tracks():
            print(track['name'])


if __name__=="__main__":
    unittest.main()