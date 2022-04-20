from bokeh.layouts import column
import logging

from bokeh.plotting import figure

from train_stats_collection import get_train_stats

color_dict = {
    '1': '#ee352e',
    '2': '#ee352e',
    '3': '#ee352e',
    '4': '#00933c',
    '5': '#00933c',
    '6': '#00933c',
    '7': '#b933ad',
    'A': '#0039a6',
    'B': '#ff6319',
    'C': '#0039a6',
    'D': '#ff6319',
    'E': '#0039a6',
    'F': '#ff6319',
    'G': '#6cbe45',
    'J': '#996633',
    'L': '#a7a9ac',
    'M': '#ff6319',
    'N': '#fccc0a',
    'Q': '#fccc0a',
    'R': '#fccc0a',
    'W': '#fccc0a',
    'Z': '#996633'
}


def produce_plot():
    train_list, trip_count_list, trip_average_wait_time_list, average_wait_time = get_train_stats()

    logging.info(train_list)
    logging.info(trip_count_list)
    logging.info(trip_average_wait_time_list)
    logging.info(average_wait_time)

    p1 = figure(x_range=train_list, height=250, title=f"Trip Count by Train - {sum(trip_count_list)} Total Trips",
                toolbar_location=None, tools="")

    p1.vbar(x=train_list, top=trip_count_list, color=[color_dict[train] for train in train_list], width=0.9)

    p2 = figure(x_range=train_list, height=250,
                title=f"Averge Wait Time by Train - {average_wait_time} min Overall Average Wait Time",
                toolbar_location=None, tools="")

    p2.vbar(x=train_list, top=trip_average_wait_time_list, color=[color_dict[train] for train in train_list], width=0.9)

    return column(p1, p2)