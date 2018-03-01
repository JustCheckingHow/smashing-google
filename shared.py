import numpy as np
from copy import deepcopy

DISTANCE = 400
WAITING_TIME = 10
MAX_TRACK_DEPTH = 20


def distance_from(car, track):
    return np.abs(car.x - track[1]) + np.abs(car.y - track[2])


def track_length(track):
    return np.abs(track[1] - track[3]) + np.abs(track[4] - track[5])

def decide_on_job(car, available_tracks, t):
    if len(available_tracks) == 0:
        return available_tracks
    new_tracks = deepcopy(available_tracks)
    for i, track in enumerate(new_tracks):
        if distance_from(car, track) < DISTANCE:
            # pop track
            if is_track_doable(car, track, t):
                car.goRide(track, t)
                new_tracks = np.delete(available_tracks, (i), axis = 0)
                return new_tracks
    # waits
    return new_tracks

def leftover_tracks(car, available_tracks, t, extra):
        if len(available_tracks) == 0:
                return available_tracks
        new_tracks = deepcopy(available_tracks)
        for i, track in enumerate(new_tracks):
            if distance_from(car, track) < DISTANCE + extra:
                # take any track literally
                car.goRide(track, t)
                new_tracks = np.delete(available_tracks, (i ), axis = 0)
                return new_tracks
        # waits
        return new_tracks

def is_track_doable(car, track, t):
    # first tracks that are ovedue land at the end
    if track[-1] >= t + distance_from(car, track) + track_length(track):
        # has the track started yet? or is in the specified waiting time?
        if (distance_from(car, track) + t - track[-2]) >= -WAITING_TIME:
            return True
        else:
            return False
    else:
        return False
