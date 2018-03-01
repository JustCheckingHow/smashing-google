import numpy as np

DISTANCE = 10
MAX_TRACK_DEPTH = 20


def distance_from(car, track):
    return np.abs(car.x - track[1]) + np.abs(car.y - track[2])


def track_length(track):
    return np.abs(track[1] - track[3]) + np.abs(track[4] - track[5])


def decide_on_job(car, available_tracks, t):
    for i, track in enumerate(available_tracks):
        if distance_from(car, track) < DISTANCE:
            print('distance ok')
            # pop track
            if is_track_doable(car, track, t):
                car.goRide(track, t)
                print('goRide')
                available_tracks.pop(i)
    # waits
    return available_tracks


def is_track_doable(car, track, t):
    # first tracks that are ovedue land at the end
    if track[-1] >= t + distance_from(car, track) + track_length(track):
        # has the track started yet? or is in the specified waiting time?
        if (distance_from(car, track) + t - track[-2]) >= -5:
            return True
    else:
        return False
