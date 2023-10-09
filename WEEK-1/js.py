import json
import pandas as pd

json_filedata = open("WEEK-1\example_2.json").read()
json_ = json.loads(json_filedata)

df = pd.read_json("WEEK-1\example_2.json",orient ="records")
# print(json_)
print(df)