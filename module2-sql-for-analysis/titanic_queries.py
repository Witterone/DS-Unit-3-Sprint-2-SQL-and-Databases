from sqlalchemy import create_engine

import pandas as pd

engine = create_engine("postgres://nidnwrpi:SfFTOS3EQqsV1c4RKQZEtU7O2g8Kic-9@ruby.db.elephantsql.com:5432/nidnwrpi")

df = pd.read_csv("titanic.csv")

df.to_sql("titanic", con=engine)

