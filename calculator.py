def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide_free(a,b):
   return a/b

import random
import time

def pick_one(*options):
    """입력받은 옵션 중 하나를 흥미롭게 골라주는 함수"""
    
    if not options:
        return "선택지가 없어요!"

    print(f"🤔 {len(options)}개의 선택지 중에서 고민 중입니다...")
    time.sleep(1)  # 긴장감을 위해 1초 대기
    
    result = random.choice(options)
    
    return f"✨ 결과는 바로: [{result}] 입니다!"

# 사용 예시
print(pick_one("점심에 제육볶음", "점심에 돈까스", "점심에 햄버거"))