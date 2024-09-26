answer_v1 = 'Intel bla-bla 250 USD ....'
answer_v2 = 'Intel bla-bla $250 ....'
answer_v3_incorrect = 'Intel bla-bla 250 ....'


is_text_correct = False
expected_elements = ['USD', '$']

for element in expected_elements:
    if element in answer_v1:
        is_text_correct = True
        print('text in correct')


assert is_text_correct, 'USD or $ is not found in text'


import os

print(os.system('ls'))
print(os.listdir('.'))

