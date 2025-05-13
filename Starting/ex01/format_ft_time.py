import datetime

timeNow = datetime.datetime.now() 
seconds = (timeNow - datetime.datetime(1970, 1, 1)).total_seconds()
print(f"Seconds since January 1, 1970: {seconds:,.4f} or "
      f"{seconds:.2e} in scientific notation")
print(datetime.datetime.now().strftime("%b %d %Y"))
