"""Test module for dubstep decoder."""
import pytest


SONGS = [
    ["AWUBBWUBC", "A B C"],
    ["AWUBWUBWUBBWUBWUBWUBC", "A B C"],
    ["WUBAWUBBWUBCWUB", "A B C"],
]


@pytest.mark.parametrize("song, decoded_song", SONGS)
def test_dubstep_decoder(song, decoded_song):
    """Test song_decoder properly deWUBs song."""
    from dubstep_decoder import song_decoder
    assert song_decoder(song) == decoded_song
