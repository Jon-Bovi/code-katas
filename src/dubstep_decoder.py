"""Module containing dubstep decoder function."""


def song_decoder(song):
    """De-WUB song."""
    return ' '.join(' '.join(song.split('WUB')).split())
