def greeting(greet):
    print(f"➡ Вызов greeting() с greet = '{greet}'")

    def inner(name):
        print(f"  👋 Внутренняя функция вызвана с name = '{name}'")
        print(f"  🔒 greet всё ещё доступен и равен '{greet}'")
        return f"{greet}, {name}!"

    print("🔁 Возвращаем внутреннюю функцию (она замыкает greet)")
    return inner


# Создаём замыкания
print("📦 Создаём morning_greeting")
morning_greeting = greeting("Good Morning")

print("\n📦 Создаём evening_greeting")
evening_greeting = greeting("Good Evening")

# Используем замыкания
print("\n💬 Вызываем morning_greeting('Alex'):")
print(morning_greeting("Alex"))

print("\n💬 Вызываем evening_greeting('Alex'):")
print(evening_greeting("Alex"))