# Полиморфизм: назначение и семантика

## Определение

**Полиморфизм** (от греч. «много форм») — способность объектов разных классов обрабатываться через единый интерфейс, при этом каждый класс реализует этот интерфейс по-своему.

## Назначение

- **Упрощение кода** — единый код работает с разными типами объектов
- **Расширяемость** — легко добавлять новые типы без изменения существующего кода
- **Абстракция** — скрытие деталей реализации, работа на уровне интерфейсов
- **Гибкость** — изменение поведения программы во время выполнения

## Виды полиморфизма

### 1. Полиморфизм подтипов (наследование)

Объекты производных классов используются вместо базовых через переопределение методов.

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

# Полиморфная функция
def make_sound(animal: Animal):
    print(animal.speak())  # Вызовется нужная реализация

make_sound(Dog())  # Гав!
make_sound(Cat())  # Мяу!
```

### 2. Параметрический полиморфизм (Generic)

Код работает с разными типами данных через параметры типов.

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T):
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()

# Один класс работает с любыми типами
int_stack = Stack[int]()
str_stack = Stack[str]()
```

### 3. Ad-hoc полиморфизм (перегрузка)

Одна операция имеет разное поведение для разных типов аргументов.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        # Перегрузка оператора +
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        # Перегрузка оператора *
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Сложение векторов
print(v1 * 3)   # Умножение на скаляр
```

## Семантика

### Принцип подстановки Лисков (LSP)

> Объекты подклассов должны заменять объекты базовых классов без нарушения корректности программы.

```python
def process_shape(shape: Shape):
    return shape.calculate_area()

# Работает для всех подклассов Shape
process_shape(Circle(5))
process_shape(Rectangle(3, 4))
process_shape(Triangle(3, 4))
```

### Раннее и позднее связывание

- **Раннее связывание** (compile-time) — решение о вызываемом методе принимается при компиляции
  - Используется: параметрический и ad-hoc полиморфизм
  - Быстрее, безопаснее

- **Позднее связывание** (runtime) — решение принимается во время выполнения
  - Используется: полиморфизм подтипов
  - Более гибко

## Когда использовать

| Вид | Когда использовать | Примеры |
|-----|-------------------|---------|
| **Подтипы** | Семейство связанных классов с общим поведением | Shape → Circle, Rectangle<br>Transport → Car, Plane |
| **Параметрический** | Структуры данных, алгоритмы для разных типов | List[T], Stack[T]<br>sort(), find_max() |
| **Ad-hoc** | Естественный синтаксис операций, перегрузка операторов | Vector, Matrix, Money<br>+, -, *, == |

## Преимущества

**Переиспользование кода** — один код для множества типов  
**Гибкость архитектуры** — легко расширять функциональность  
**Читаемость** — понятные абстракции вместо условных операторов  
**Поддерживаемость** — изменения локализованы в конкретных классах  
**Тестируемость** — легко подменять реализации

## Практические паттерны

**Стратегия (Strategy)**
```python
class PaymentStrategy:
    def pay(self, amount): pass

class CreditCard(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата {amount} картой"

class PayPal(PaymentStrategy):
    def pay(self, amount):
        return f"Оплата {amount} через PayPal"
```

**Фабричный метод (Factory Method)**
```python
class Document:
    def create(self): pass

class PDFDocument(Document):
    def create(self):
        return "PDF создан"

class WordDocument(Document):
    def create(self):
        return "Word создан"
```
