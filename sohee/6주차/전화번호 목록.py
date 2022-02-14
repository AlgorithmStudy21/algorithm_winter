def solution(phone_book):
    phone_book.sort(key=lambda x: (x, len(x)))

    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True


if __name__ == '__main__':
    solution(["119", "97674223", "1195524421"])
    solution(["123", "456", "789"])
    solution(["12", "123", "1235", "567", "88"])
