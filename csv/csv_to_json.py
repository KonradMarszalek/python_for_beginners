import csv
import json
from os import path

base_path = path.dirname(__file__)
csv_path = path.abspath(path.join(base_path, "results_summary.csv"))
json_path = path.abspath(path.join(base_path, "results_summary.json"))

csv_file = open(csv_path, 'r')
json_file = open(json_path, 'w')

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
reader = csv.DictReader(csv_file, fieldnames)
out = json.dumps([row for row in reader], )
json_file.write(out)
