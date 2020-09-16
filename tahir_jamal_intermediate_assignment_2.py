
"""
Assignment #2
Returns current time in Hour:Minutes PM/AM format

By Tahir Jamal
"""
from datetime import datetime
today = datetime.now()
answer = (today.strftime('%H:%M:%p'))
print(answer)
