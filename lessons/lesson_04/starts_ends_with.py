

sent = 'Would yyou tell me, please, which way t much care where ——" said Alice. ASD. Alice.'

print(sent.startswith('Would'))  # True
print(sent.startswith('Could'))  # False
print(sent.endswith('Alice'))  # False
print(sent.endswith('Alice.'))  # True
print(sent.endswith('Shmalice'))  # False
#
for word in sent.split():
    print(f'is {word} starts with s: {word.startswith("A")}')

returns_urls = ['www.simple.com/asd?a=b', 'www.simple.com/asd?', 'www.simple.com/xxxxxxx?a=b', 'www.s1imple.com/asd?a=b']
expected_start = 'www.simple.com'

index = 0
for url in returns_urls:
    res = url.startswith(expected_start)
    if not res:
        print(f'BAD CASE in position {index}: {url}')

    index += 1  # index = index + 1
