import numpy as np

DISTANCE = 10
MAX_TRACK_DEPTH = 20

def distance_from(car, track):
    return np.abs(car.x - track[0]) + np.abs(car.y - track[1])

def decide_on_job(car, available_tracks):
    for i, track in enumerate(available_tracks):
        if distance_from(car, track) < DISTANCE:
            # pop track
            car.goRide(track)
            available_tracks.pop(i)
    # waits
    return new_tracks
