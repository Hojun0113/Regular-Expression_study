#문자열에서 패턴 검색하기 (re.search() 사용)
import re

string = "Hello, World!"
pattern = r"Hello"
match = re.search(pattern, string)
if match:
    print("일치하는 패턴을 찾았습니다:", match.group())
else:
    print("일치하는 패턴이 없습니다.")

#문자열에서 패턴 일치하는 모든 항목 찾기 (re.findall() 사용)

import re

string = "apple, banana, cherry, date"
pattern = r"\b\w+\b"  # 단어 경계로 구분된 단어들
matches = re.findall(pattern, string)
print("일치하는 패턴들:", matches)

#문자열에서 패턴 일치하는 항목 치환하기 (re.sub() 사용)
<code>
import re

string = "Hello, World!"
pattern = r"World"
replacement = "Python"
new_string = re.sub(pattern, replacement, string)
print("치환된 문자열:", new_string)

#문자열 분할하기 (re.split() 사용)

import re

string = "apple,banana,cherry,date"
pattern = r","
parts = re.split(pattern, string)
print("분할된 문자열:", parts)
