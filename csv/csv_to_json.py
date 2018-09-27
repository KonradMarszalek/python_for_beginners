#!/usr/bin/env python

import csv
import json
from datetime import datetime

csv_file = open("results_summary.csv", 'r')
json_file = open("results_summary.json", 'w')

fieldnames = (
    "sampler_label",
    "aggregate_report_count",
    "average",
    "aggregate_report_median",
    "aggregate_report_90%_line",
    "aggregate_report_95%_line",
    "aggregate_report_99%_line",
    "aggregate_report_min",
    "aggregate_report_max",
    "aggregate_report_error%",
    "aggregate_report_rate",
    "aggregate_report_bandwidth",
    "aggregate_report_stddev")
summary = [row for row in csv.DictReader(csv_file, fieldnames)]
summary.remove(summary[0])  # Remove unnecessary headers info

timestamp = datetime.utcnow().isoformat()
for row in summary:
    row['@timestamp'] = timestamp

json_summary = [json.dumps(row) for row in summary]
json_file.write('\n'.join(json_summary) + '\n')
