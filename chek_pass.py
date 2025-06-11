import re

def validate_password(password):
    
    # 1. אורך מינימלי של 8 תווים
    if len(password) < 8:
        # print("שגיאה: אורך מינימלי של 8 תווים נדרש.")
        return False

    # 2. מכיל לפחות תו קטן אחד, תו גדול אחד, ספרה אחת, תו מיוחד אחד
    # שימוש בביטויים רגולריים לבדיקה מהירה
    if not re.search(r"[a-z]", password):
        # print("שגיאה: חייב להכיל לפחות תו קטן אחד.")
        return False
    if not re.search(r"[A-Z]", password):
        # print("שגיאה: חייב להכיל לפחות תו גדול אחד.")
        return False
    if not re.search(r"\d", password):
        # print("שגיאה: חייב להכיל לפחות ספרה אחת.")
        return False
    if not re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]", password):
        # print("שגיאה: חייב להכיל לפחות תו מיוחד אחד.")
        return False

    # 3. לא ניתן לחזור על תו יותר מפעמיים (לדוגמה, 'aaa' אינו חוקי)
    # שימוש בביטוי רגולרי: (.{1})\1\1 - מחפש כל תו (.{1}) ואז חוזר עליו פעמיים (\1\1)
    if re.search(r"(.)\1\1", password):
        # print("שגיאה: אסור לחזור על תו יותר מפעמיים ברצף (לדוגמה, 'aaa').")
        return False

    # 4. אין רצפים של 3 תווים עוקבים (לדוגמה, 'abc', 'xyz', '123')
    for i in range(len(password) - 2):
        char1 = password[i]
        char2 = password[i+1]
        char3 = password[i+2]

        # בדיקה לרצפים עולים (abc, 123)
        if (ord(char2) == ord(char1) + 1 and ord(char3) == ord(char2) + 1):
            # print(f"שגיאה: רצף עולה אסור ({char1}{char2}{char3}).")
            return False
        # בדיקה לרצפים יורדים (cba, 321)
        if (ord(char2) == ord(char1) - 1 and ord(char3) == ord(char2) - 1):
            # print(f"שגיאה: רצף יורד אסור ({char1}{char2}{char3}).")
            return False

    # אם כל הבדיקות עברו בהצלחה
    return True

# --- דוגמאות שימוש ---
print("--- בדיקות סיסמאות ---")

# סיסמאות חוקיות
print(f"'MyPass123!': {validate_password('MyPass123!')}")         # True
print(f"'P@ssw0rd1': {validate_password('P@ssw0rd1')}")         # True
print(f"'aB1!aB1!': {validate_password('aB1!aB1!')}")           # True

print("\n--- סיסמאות לא חוקיות ---")

# אורך קצר
print(f"'Short!1': {validate_password('Short!1')}")           # False (אורך)

# חסר תו קטן
print(f"'MYPASS123!': {validate_password('MYPASS123!')}")       # False (חסר קטן)

# חסר תו גדול
print(f"'mypass123!': {validate_password('mypass123!')}")       # False (חסר גדול)

# חסר ספרה
print(f"'MyPassWrd!': {validate_password('MyPassWrd!')}")       # False (חסר ספרה)

# חסר תו מיוחד
print(f"'MyPass1234': {validate_password('MyPass1234')}")       # False (חסר מיוחד)

# חזרה על תו יותר מפעמיים
print(f"'MyPaaass1!': {validate_password('MyPaaass1!')}")      # False (AAA)
print(f"'Mmmypass1!': {validate_password('Mmmypass1!')}")      # False (mmm)

# רצף עוקב
print(f"'MyPassabc!': {validate_password('MyPassabc!')}")      # False (abc)
print(f"'MyPass123!': {validate_password('MyPass123!')}")      # False (123)
print(f"'Passxyz1!': {validate_password('Passxyz1!')}")        # False (xyz)
print(f"'ZYXpass1!': {validate_password('ZYXpass1!')}")        # False (zyx - רצף יורד, אם נבדק)