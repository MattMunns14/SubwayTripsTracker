from statistics import mean

import boto3


def get_train_stats():

    trip_dict = {}

    wait_time_list = []

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table("TextReciever-TripsTable-1J4MQSZD4BG19")

    response = table.scan()

    for trip in response['Items']:

        if (train := str(trip["train"])) in trip_dict:
            trip_dict[train].append(int(trip['wait_time']))
        else:
            trip_dict[train] = [int(trip['wait_time'])]
        wait_time_list.append(int(trip['wait_time']))

    train_list = [unique_train for unique_train in trip_dict.keys()]
    trip_count_list = [len(trip_dict[unique_train]) for unique_train in train_list]
    trip_average_wait_time_list = [round(mean(trip_dict[unique_train]), 2) for unique_train in train_list]

    return train_list, trip_count_list, trip_average_wait_time_list, round(mean(wait_time_list), 2)
