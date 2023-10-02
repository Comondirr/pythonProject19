class Task:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def object_info(self):
        return f"Поле 1 (нижнее основание трапеции): {self.field1}, Поле 2 (верхнее основание трапеции): {self.field2}"

    def process_fields(self):
        # Ваша индивидуальная логика обработки полей для данной задачи
        # Например, вычисление площади трапеции
        area = 0.5 * (self.field1 + self.field2)  # Пример расчета площади трапеции
        return f"Площадь трапеции: {area}"


if __name__ == "__main__":
    num_tasks = int(input("Введите количество задач: "))
    tasks = []

    for i in range(num_tasks):
        field1 = int(input(f"Введите значение Поле 1 для задачи {i + 1}: "))
        field2 = int(input(f"Введите значение Поле 2 для задачи {i + 1}: "))
        task = Task(field1, field2)
        tasks.append(task)

    result = []

    for i, task in enumerate(tasks):
        result.append(f"Задача {i + 1}:")
        result.append(task.object_info())
        result.append(task.process_fields())

    # Вывод результатов в Memo (здесь используется простой вывод в консоль)
    for line in result:
        print(line)


        print()
        print()
        print()
        print()
        print()


        class Task:
            def __init__(self, field1, field2):
                self.field1 = field1
                self.field2 = field2

            def object_info(self):
                return f"Поле 1 (нижнее основание трапеции): {self.field1}, Поле 2 (верхнее основание трапеции): {self.field2}"

            def process_fields(self):
                # Ваша индивидуальная логика обработки полей для данной задачи
                # Например, вычисление площади трапеции
                area = 0.5 * (self.field1 + self.field2)  # Пример расчета площади трапеции
                return f"Площадь трапеции: {area}"


        class PrismTask(Task):
            def __init__(self, field1, field2, height):
                super().__init__(field1, field2)
                self.height = height

            def object_info(self):
                return f"Поле 1 (нижнее основание трапеции): {self.field1}, " \
                       f"Поле 2 (верхнее основание трапеции): {self.field2}, " \
                       f"Высота призмы: {self.height}"

            def process_fields(self):
                # Ваша индивидуальная логика обработки полей для задачи с призмой
                # Например, вычисление объема призмы
                volume = 0.5 * (self.field1 + self.field2) * self.height
                return f"Объем призмы: {volume}"


        if __name__ == "__main__":
            num_tasks = int(input("Введите количество задач: "))
            tasks = []

            for i in range(num_tasks):
                field1 = int(input(f"Введите значение Поле 1 для задачи {i + 1}: "))
                field2 = int(input(f"Введите значение Поле 2 для задачи {i + 1}: "))
                height = int(input(f"Введите значение Высота призмы для задачи {i + 1}: "))

                # Создаем объекты классов Task и PrismTask
                task = Task(field1, field2)
                prism_task = PrismTask(field1, field2, height)

                # Добавляем объекты в список
                tasks.append(task)
                tasks.append(prism_task)

            result = []

            for i, task in enumerate(tasks):
                result.append(f"Задача {i + 1}:")
                result.append(task.object_info())
                result.append(task.process_fields())

            # Вывод результатов в Memo (здесь используется простой вывод в консоль)
            for line in result:
                print(line)
print()
print()
print()
print()


class TheaterPerformance:
    def __init__(self, name, nl, n2):
        self.name = name
        self.nl = nl
        self.n2 = n2

    def quality(self, n1):
        return (self.n2 - self.nl) / n1

    def info(self):
        return f"Спектакль: {self.name}, Начальное количество зрителей: {self.nl}, " \
               f"Конечное количество зрителей: {self.n2}"


class PlayPerformance(TheaterPerformance):
    def __init__(self, name, nl, n2, year_written, current_year):
        super().__init__(name, nl, n2)
        self.year_written = year_written
        self.current_year = current_year

    def quality(self, n1):
        Q = super().quality(n1)
        T = self.current_year
        P = self.year_written
        Op = Q * (T - P + 1)
        return Op

    def info(self):
        base_info = super().info()
        return f"{base_info}, Год написания пьесы: {self.year_written}, " \
               f"Текущий год: {self.current_year}"


if __name__ == "__main__":
    name = input("Введите название спектакля: ")
    nl = int(input("Введите начальное количество зрителей: "))
    n2 = int(input("Введите конечное количество зрителей: "))
    year_written = int(input("Введите год написания пьесы: "))
    current_year = int(input("Введите текущий год: "))

    theater_performance = TheaterPerformance(name, nl, n2)
    play_performance = PlayPerformance(name, nl, n2, year_written, current_year)

    print("Информация о спектакле (класс 1-го уровня):")
    print(theater_performance.info())
    print(f"Качество спектакля (класс 1-го уровня): {theater_performance.quality(nl)}")

    print("\nИнформация о спектакле (класс 2-го уровня):")
    print(play_performance.info())
    print(f"Качество спектакля (класс 2-го уровня): {play_performance.quality(nl)}")

