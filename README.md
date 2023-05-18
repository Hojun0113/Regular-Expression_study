# 1. 정규 표현식(Regular Expression)
<h3>정규 표현식이란 ?</h3><br>

- 강력한 문자열 검색과 패턴 매칭 기능을 제공합니다.
- re 모듈을 통해 파이썬에서 정규식을 사용할 수 있습니다.
- 정규식은 텍스트 패턴을 표현하는 문자열입니다. 이를 사용하여 특정한 패턴을 가진 문자열을 찾거나 변형할 수 있습니다.
- 정규식을 사용하여 문자열을 검사하거나 추출할 때, 일치하는 패턴을 찾아주는 메타문자와 특수 시퀀스를 사용합니다.
<hr>

<h3>파이썬에서 자주 쓰이는 메타문자</h3><br>

. (마침표): 임의의 문자 한 개와 일치합니다. 예를 들어, 정규식 a.b는 "aab", "acb" 등과 일치하지만 "ab"와는 일치하지 않습니다.<br>

 (별표): 앞의 문자가 0번 이상 반복됨을 나타냅니다. 예를 들어, 정규식 ca*t는 "ct", "cat", "caat" 등과 일치합니다.<br>

 (더하기): 앞의 문자가 1번 이상 반복됨을 나타냅니다. 예를 들어, 정규식 ca+t는 "cat", "caat" 등과 일치하지만 "ct"와는 일치하지 않습니다.<br>

? (물음표): 앞의 문자가 0 또는 1번 반복됨을 나타냅니다. 예를 들어, 정규식 colou?r는 "color", "colour"와 일치합니다.<br>

| (파이프): 여러 패턴 중 하나와 일치합니다. 예를 들어, 정규식 a|b는 "a" 또는 "b"와 일치합니다.<br>

[] (대괄호): 문자 집합을 나타냅니다. 대괄호 안에 있는 문자 중 하나와 일치합니다. 예를 들어, 정규식 [abc]는 "a", "b", "c" 중 하나와 일치합니다.<br>

() (괄호): 그룹화를 나타내며, 그룹으로 묶인 패턴을 하나의 단위로 처리합니다. 예를 들어, 정규식 (ab)+는 "ab", "abab", "ababab" 등과 일치합니다.<br>

<hr>
<h3>파이썬에서 쓰이는 특수문자(이스케이프)</h3>

\ (역슬래시): 이스케이프 문자로서, 다른 문자와 함께 사용하여 특수한 의미를 가진 문자를 일반 문자로 취급합니다. 예를 들어, \., \\, \( 등은 각각 점, 역슬래시, 괄호를 일반 문자로 사용합니다.<br>

\d: 숫자에 대응됩니다. [0-9]와 동일한 의미를 가집니다.<br>

\D: 숫자가 아닌 문자에 대응됩니다. [^0-9]와 동일한 의미를 가집니다.<br>

\w: 알파벳 문자나 숫자에 대응됩니다. [a-zA-Z0-9_]와 동일한 의미를 가집니다.<br>

\W: 알파벳 문자나 숫자가 아닌 문자에 대응됩니다. [^a-zA-Z0-9_]와 동일한 의미를 가집니다.<br>

\s: 공백 문자에 대응됩니다. 스페이스, 탭, 개행 문자 등을 포함합니다.<br>

\S: 공백이 아닌 문자에 대응됩니다.<br>

\b: 단어 경계에 대응됩니다. 단어 경계는 단어와 비단어 문자 사이의 위치를 나타냅니다.<br>

이 외에도 \t (탭), \n (개행 문자), \r (캐리지 리턴) 등의 이스케이프 문자도 사용할 수 있습니다. 이스케이프 문자를 활용하여 정규식 패턴을 작성할 때는 주의가 필요하며, 문자열 안에서 이스케이프 문자를 사용할 때는 역슬래시를 두 번 입력해야 합니다. 예를 들어, 역슬래시를 검색하려면 \\로 작성해야 합니다.<br>
<hr>
<h3>파이썬에서 정규표현식을 다루기 위한 주요 함수</h3><br>

re.search(pattern, string, flags=0): 문자열 전체에서 정규식 패턴과 일치하는 첫 번째 항목을 검색합니다.<br> 일치하는 객체가 발견되면 Match 객체를 반환하고, 일치하지 않으면 None을 반환합니다.<br>

re.match(pattern, string, flags=0): 문자열의 시작에서 정규식 패턴과 일치하는지 검사합니다.<br> 일치하는 객체가 발견되면 Match 객체를 반환하고, 일치하지 않으면 None을 반환합니다.<br>

re.findall(pattern, string, flags=0): 문자열에서 정규식 패턴과 일치하는 모든 항목을 찾아 리스트로 반환합니다.<br>

re.finditer(pattern, string, flags=0): 문자열에서 정규식 패턴과 일치하는 모든 항목을 찾아 Match 객체의 이터레이터를 반환합니다.<br>

re.sub(pattern, repl, string, count=0, flags=0): 문자열에서 정규식 패턴과 일치하는 모든 항목을 주어진 대체 문자열(repl)로 치환합니다.<br> count 매개변수를 사용하여 치환할 항목 수를 제한할 수 있습니다.<br>

re.split(pattern, string, maxsplit=0, flags=0): 정규식 패턴을 기준으로 문자열을 분할하여 리스트로 반환합니다.<br> maxsplit 매개변수를 사용하여 분할 횟수를 제한할 수 있습니다.<br>

<hr>
<h3>정규식 코드 예제</h3>

<b>문자열에서 패턴 검색하기 (re.search() 사용)</b>
<code>
import re

string = "Hello, World!"
pattern = r"Hello"
match = re.search(pattern, string)
if match:
    print("일치하는 패턴을 찾았습니다:", match.group())
else:
    print("일치하는 패턴이 없습니다.")
</code><br>
<b>문자열에서 패턴 일치하는 모든 항목 찾기 (re.findall() 사용)</b>
<code>
import re

string = "apple, banana, cherry, date"
pattern = r"\b\w+\b"  # 단어 경계로 구분된 단어들
matches = re.findall(pattern, string)
print("일치하는 패턴들:", matches)
</code><br>
<b>문자열에서 패턴 일치하는 항목 치환하기 (re.sub() 사용)</b>
<code>
import re

string = "Hello, World!"
pattern = r"World"
replacement = "Python"
new_string = re.sub(pattern, replacement, string)
print("치환된 문자열:", new_string)
</code><br>
<b>문자열 분할하기 (re.split() 사용)</b>
<code>
import re

string = "apple,banana,cherry,date"
pattern = r","
parts = re.split(pattern, string)
print("분할된 문자열:", parts)
</code>
