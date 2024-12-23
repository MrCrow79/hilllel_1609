import re

row = """Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated"""


print(row.startswith('Tom gave'))
print(row.endswith('sweated'))
print('Tom' in row)
# The Company has 225.3B USD market cap"
news = """
The Company has market cap 225.3 billion and 58 daily revenues USD "
The Company has market cap 225 322 555 000 usd"""

# \b225.?3\s?(billion|[Bb])?([\s\w\s\d\s])+\s\b(USD|usd)\b
pattern = r'\b225.?3\s?(billion|[Bb])?([\s\w\s\d\s])+\s\b(USD|usd)\b'

is_numbers_in_text = re.search(pattern, news) is  None

numbers_in_text = re.search(pattern, news)
numbers_in_text.span()






print(re.match(pattern, news))
