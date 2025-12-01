def type7_decrypt(password):
    key = 'dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fglwyeoajrvn1ijtnd'
    result = ''

    # Берем первые две цифры зашифрованного пароля
    offset = int(password[:2])

    # Получаем фактическую длину пароля
    encoded_password = password[2:]

    # Проходим по каждому символу и восстанавливаем оригинальный текст
    for i, char in enumerate(encoded_password):
        index = (i + offset) % len(key)
        decrypted_char = chr(int(char, 16) ^ ord(key[index]))
        result += decrypted_char

    return result.strip()


# Пример использования
encoded_pass = '0D501E150228475B1A4B554542'  # Ваш зашифрованный пароль типа 7
print(type7_decrypt(encoded_pass))