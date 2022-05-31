"""
Usage: clouddb_import.py [OPTIONS] [COLLECTION] [%Y-%m-%d] [%H:%M] [%H:%M]
                         FILE_OUTPUT

  Obtains ECG data from the Kymira cloud storage and stores it to a CSV.

Options:
  --help  Show this message and exit.
"""
#!/usr/bin/env python

import click
from kymira_data_in import get_from_cloudDB

@click.command()
@click.argument("collection", type=click.STRING, default="debug-device_ecg-raw")
@click.argument("collection_date", type=click.DateTime(formats=["%Y-%m-%d"]),)
@click.argument("time_start", type=click.DateTime(formats=["%H:%M"]),)
@click.argument("time_end", type=click.DateTime(formats=["%H:%M"]),)
@click.argument("file_output", type=click.Path(),)
def clouddb_import(collection_date, time_start, time_end, collection, file_output):
    """
    Obtains ECG data from the Kymira cloud storage and stores it to a CSV.
    """
    get_from_cloudDB(collection_date, time_start, time_end, collection).to_csv(file_output, index=False,)


if __name__ == "__main__":
    clouddb_import()