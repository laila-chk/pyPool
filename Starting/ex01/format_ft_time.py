import datetime as dt

timeNow = dt.datetime.now()
seconds = (timeNow - dt.datetime(1970, 1, 1)).total_seconds()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or "
      f"{seconds:.2e} in scientific notation")
print(dt.datetime.now().strftime("%b %d %Y"))
