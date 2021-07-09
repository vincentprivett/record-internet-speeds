#!/usr/bin/python3
# https://github.com/sivel/speedtest-cli
import speedtest as st
import pandas as pd
from datetime import datetime
import os, sys
os.chdir(sys.path[0]) # set working directory to save csv when run as cron job

def get_new_speeds():
    speed_test = st.Speedtest()
    speed_test.get_best_server()

    # Get ping (miliseconds)
    ping = speed_test.results.ping
    # Get server info
    host = speed_test.results.server['host']
    location = speed_test.results.server['name']
    sponsor = speed_test.results.server['sponsor']
    # Perform download and upload speed tests (bits per second)
    download = speed_test.download()
    upload = speed_test.upload()

    # Convert download and upload speeds to megabits per second
    download_mbs = round(download / (10**6), 2)
    upload_mbs = round(upload / (10**6), 2)

    return (ping, download_mbs, upload_mbs, host, location, sponsor)


def update_csv(internet_speeds):
    # Get today's date in the form Month/Day/Year
    date_today = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
    # File with the dataset
    csv_file_name = "internet_speeds_dataset.csv"

    # Load the CSV to update
    try:
        csv_dataset = pd.read_csv(csv_file_name, index_col="Date")
    # If there's an error, assume the file does not exist and create\
    # the dataset from scratch
    except:
        csv_dataset = pd.DataFrame(
            list(),
            columns=["Ping (ms)", "Download (Mb/s)", "Upload (Mb/s)", "host", "location", "sponsor"]
        )

    # Create a one-row DataFrame for the new test results
    results_df = pd.DataFrame(
        [[ internet_speeds[0], internet_speeds[1], internet_speeds[2], internet_speeds[3], internet_speeds[4], internet_speeds[5] ]],
        columns=["Ping (ms)", "Download (Mb/s)", "Upload (Mb/s)", "host", "location", "sponsor"],
        index=[date_today]
    )

    updated_df = csv_dataset.append(results_df, sort=False).to_csv(csv_file_name, index_label="Date")
    # https://stackoverflow.com/a/34297689/9263761
    # updated_df\
        # .loc[~updated_df.index.duplicated(keep="last")]\
        # .to_csv(csv_file_name, index_label="Date")


new_speeds = get_new_speeds()
update_csv(new_speeds)
