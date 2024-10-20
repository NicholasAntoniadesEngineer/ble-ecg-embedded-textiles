"""
Code to retrieve Kymira datasets from various sources.

:author: Soma Chakraborty
:author: Athanasios Anastasiou
:date: Mon Jan 27 15:08:14 2020
"""
from pymongo import MongoClient
import time
from datetime import datetime
from .packet_tools import uncompress_samples
import pandas

# SAMPLING_FRE = 500  # Hz
# ADDITIONAL_INFO_1 = ['# Sampling rate: 500 Hz']


def get_from_cloudDB(date_of_exp, start_time, end_time, collection="debug-device_ecg-raw"):
    """
    Reads ECG data from a given ecg data collection in the KYMIRA MongoDB database hosted in Azure CosmosDB.

    :param collection: The collection to retrieve data from
    :type collection: str
    :param date_of_exp: Specific date of the collection
    :type date_of_exp: datetime.datetime
    :param start_time: Specific start time of the collection
    :type start_time: datetime.datetime
    :param end_time: Specific end time of the collection
    :type end_time: datetime.datetime

    :returns: A Dataframe with the ECG data.
    :rtype: pandas.DataFrame
    """

    if not isinstance(collection, str):
        raise TypeError(f"Expected a collection received {collection} / {type(collection)}")

    db_string = 'mongodb://devtest-db:LKqCyxHxYRKA39Pis7lUGLX0cnUXzMwzXeU8vzzk9aVwf1MF6pXIhx1URdvMJmSc3kZBHJHXRumSjkvjAk77rQ==@devtest-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@devtest-db@'
    client = MongoClient(db_string)  # Mongo Client
    db = client['dev-kymetric-db']  # Database
    COLLECTION = db[collection]  # Collection

    date = time.strptime(date_of_exp, "%Y-%m-%d")
    year = date.tm_year
    mon = date.tm_mon
    day = date.tm_mday

    st = time.strptime(start_time, "%H:%M")
    start_hr = st.tm_hour
    start_min = st.tm_min

    et = time.strptime(end_time, "%H:%M")
    end_hr = et.tm_hour
    end_min = et.tm_min

    start_time = datetime(year, mon, day, start_hr, start_min, 0)  # (YYYY,MM,DD,hh,mm,ss)
    startT = time.mktime(start_time.timetuple()) * 1000

    end_time = datetime(year, mon, day, end_hr, end_min, 0)  # (YYYY,MM,DD,hh,mm,ss)
    endT = time.mktime(end_time.timetuple()) * 1000

    query = COLLECTION.find({'packet_info.tstamp': {"$gt": startT, "$lt": endT}})

    ecg_data = []
    packet_timestamp = []
    data_packets = []

    for item in query:
        uncompressed_data = uncompress_samples(item['samples'])
        sample_data = pandas.DataFrame.from_dict(uncompressed_data)
        data_packets.append(sample_data)

        packet_timestamp.append(item['packet_info']['tstamp'])
        timesorted_indices = sorted(range(len(packet_timestamp)), key=packet_timestamp.__getitem__)

    for index in range(len(timesorted_indices)):  # This step is needed to ensure that the data points
        current_tstamp = packet_timestamp[timesorted_indices[index]]  # are always continuous in time
        data_list = data_packets[timesorted_indices[index]]

    ecg_data = pandas.concat(data_packets, ignore_index=True)

    return ecg_data


def read_ecg_trial(an_input_file):
    """
    Reads a KYMIRA ECG CSV file.

    Notes:
        * A Kymira CSV has columns ecg<1..5>, tstamp and optionall a comment in the first line
          denoting the Fs of the file.

    :param an_input_file: Path to the csv file to load
    :type an_input_file: str (path)

    :returns: A DataFrame with the actual data
    :rtype: pandas.DataFrame

    """
    # TODO: HIGH, Enable this to read the Fs from the CSV comments
    # Fs_rule = (pyparsing.Suppress("# Sampling rate: ") +
    #            pyparsing.Regex("[0-9]+").setParseAction(lambda s, l, t: int(t[0])) +
    #            pyparsing.Suppress("Hz"))
    # with open(an_input_file, "rt") as fd:
    #     # Just read the first line which usually contains the sample rate "comment"
    #     fs_data = fd.readline()
    # Extract the Fs
    # Fs = Fs_rule.parseString(fs_data)[0]
    # WARNING: The unit here is always assumed to be **HERTZ** and you cannot have fractional Fs
    # (In this version at least).
    return pandas.read_csv(an_input_file,
                           index_col=None,
                           infer_datetime_format=True,
                           parse_dates=["tstamp", ],
                           # date_parser=(lambda x: datetime.datetime.fromisoformat(x).timestamp()),
                           comment="#")
