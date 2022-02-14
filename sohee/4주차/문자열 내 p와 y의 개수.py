def solution(s):
    _s = s.lower()
    if _s.count('p') == _s.count('y'):
        return True
    else:
        return False
