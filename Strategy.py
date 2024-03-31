from abc import ABC, abstractmethod

class RouteStrategy(ABC): # Интерфейс стратегии
    @abstractmethod
    def buildRoute(self, A, B):
        ...

class RoadStrategy(RouteStrategy):
    def buildRoute(self, A, B):
        return f"Чтобы добраться от {A} до {B} Вам нужно воспользоваться машиной"

class WalkingStrategy(RouteStrategy):
    def buildRoute(self, A, B):
        return f"Чтобы добраться от {A} до {B} Вам можно пройти пешком"

class PublicTransportStrategy(RouteStrategy):
    def buildRoute(self, A, B):
        return f"Чтобы добраться от {A} до {B} Вам нужно воспользоваться общественным транспортом"

class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def buildRoute(self, A, B):
        print(self._strategy.buildRoute(self, A, B))

route = Navigator(RoadStrategy)
route.buildRoute('г.Москва, ул.Академика Сахарова', 'г.Москва, ул.Бутовская Аллея')

route.set_strategy(WalkingStrategy)
route.buildRoute('ул.Стромынка 20', 'метро Соскольники')

route.set_strategy(PublicTransportStrategy)
route.buildRoute('ул.Артюхиной 15', 'метро Текстильщики')