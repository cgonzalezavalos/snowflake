import pandas as pd
import  snowflake.connector as sc
from datetime import date

con = sc.connect(
    user='CAGONZALEZ',
    password='Servcivil1234',
    account='FUA39190',
    session_parameters={
        'QUERY_TAG': 'EndOfMonthFinancials',
    }
)