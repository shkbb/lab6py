import random

def treasure_division():
    """Гра "Скарбниця короля" - поділ монет між командою"""
    coins = random.randint(1, 1000)
    print(f"Знайдено {coins} золотих монет!")
    try:
        team_size = int(input("Введіть кількість людей у команді: "))
        share = coins // team_size
        print(f"Кожен отримує {share} монет.")
    except ValueError:
        print("Помилка! Введіть число.")
    except ZeroDivisionError:
        print("Помилка! Не можна ділити на нуль.")
    finally:
        print("Пригоди тривають!")

def safe_crack():
    """Гра "Код сейфу" - злам кодового замка"""
    code = random.randint(100, 999)
    attempts = 5
    while attempts > 0:
        try:
            guess = int(input("Введіть тризначний код: "))
            if guess == code:
                print("Ви зламали сейф!")
                return
            elif guess < code:
                print("Код більший")
            else:
                print("Код менший")
        except ValueError:
            print("Помилка! Введіть число.")
        finally:
            attempts -= 1
            print(f"Залишилось спроб: {attempts}")
    print(f"Код сейфу був: {code}")

def rpsls():
    """Розширена гра "Камінь-ножиці-папір-ящірка-Спок"""
    choices = ["камінь", "ножиці", "папір", "ящірка", "спок"]
    rules = {
        "камінь": ["ножиці", "ящірка"],
        "ножиці": ["папір", "ящірка"],
        "папір": ["камінь", "спок"],
        "ящірка": ["папір", "спок"],
        "спок": ["ножиці", "камінь"]
    }
    computer = random.choice(choices)
    try:
        player = input("Оберіть: камінь, ножиці, папір, ящірка, спок: ").lower()
        if player not in choices:
            raise ValueError("Некоректний вибір!")
        print(f"Комп'ютер обрав: {computer}")
        if player == computer:
            print("Нічия!")
        elif computer in rules[player]:
            print("Ви виграли!")
        else:
            print("Ви програли!")
    except ValueError as e:
        print(e)

def bonus_system():
    """Система нарахування бонусів"""
    multipliers = [(90, 100, "Платиновий гравець", 3),
                   (70, 89, "Золотий гравець", 2),
                   (50, 69, "Срібний гравець", 1.5),
                   (0, 49, "Початківець", 1)]
    try:
        score = int(input("Введіть кількість очок (0-100): "))
        if score < 0 or score > 100:
            raise ValueError("Некоректне введення!")
        for low, high, rank, multiplier in multipliers:
            if low <= score <= high:
                final_score = int(score * multiplier)
                print(f"Ваш рейтинг: {rank}! Ви отримали {final_score} балів (множник ×{multiplier})!")
                break
    except ValueError:
        print("Помилка! Введіть число у межах 0-100.")

def pirate_escape():
    """Гра "Втеча з острова піратів"""
    try:
        wood = int(input("Скільки деревини у вас є? (1-10): "))
        if wood < 3:
            raise ValueError("Деревини замало, пліт затонув!")
    except ValueError:
        print("Це не число або деревини замало!")
        return
    
    try:
        action = input("Як ви втечете? (бігти/сховатися/битися): ").lower()
        if action not in ["бігти", "сховатися", "битися"]:
            raise ValueError("Такого варіанту немає, пірати вас спіймали!")
    except ValueError as e:
        print(e)
        return
    
    code = random.randint(10, 99)
    try:
        user_code = int(input("Введіть код для відкриття скрині: "))
        if user_code != code:
            raise ValueError("Неправильний код, скриня вибухнула!")
        print("Скарб ваш, ви врятовані!")
    except ValueError:
        print("Неправильний код, гра завершена!")
    finally:
        print("Гра завершена. Дякуємо за участь у пригоді!")

def main():
    """Головне меню"""
    games = {
        "1": treasure_division,
        "2": safe_crack,
        "3": rpsls,
        "4": bonus_system,
        "5": pirate_escape
    }
    while True:
        print("\nОберіть гру:")
        print("1 - Скарбниця короля")
        print("2 - Код сейфу")
        print("3 - Камінь-ножиці-папір-ящірка-Спок")
        print("4 - Система бонусів")
        print("5 - Втеча з острова піратів")
        print("0 - Вийти")
        choice = input("Ваш вибір: ")
        if choice == "0":
            break
        elif choice in games:
            games[choice]()
        else:
            print("Некоректний вибір!")

if __name__ == "__main__":
    main()
