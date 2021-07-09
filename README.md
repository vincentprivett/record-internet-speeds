Run speedtest-ci and saves results to a CSV file for review.  This can also be scheduled via a CRON job with;

0 2-6/2 * * * /home/XXX/record_internet_speeds/script.py

to run (at 0200, 0400 & 0600) and save the results to internet_speeds_dataset.csv within record_internet_speeds folder.


CSV Example;

| Date             | Ping (ms) | Download (Mb/s) | Upload (Mb/s) | host                     | location | sponsor |
| ---------------- | --------- | --------------- | ------------- | ------------------------ | -------- | ------- |
| 09/07/2021 09:01 | 11.219    | 170.09          | 37.13         | example.example.com:8080 | Example  | Example |
| 09/07/2021 09:03 | 14.545    | 175.11          | 37.18         | example.example.com:8080 | Example  | Example |

