def is_adult(age):
    if age > 19:
        return "성인입니다."
    else:
        return "성인이 아닙니다."

age = 30

print(is_adult(age))
