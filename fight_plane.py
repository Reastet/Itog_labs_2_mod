import plane

class FightPlane(plane):
    def __init__(self, model : str, curfuel: float, expenses : float, posx: float, posy: float, posh: float, rocket_type : str, rocket_num: int):
        '''
                Инициализация объекта "боевой самолет"
                :param model: название модели
                :param curfuel: начальный объем топлива
                :param expenses: расход топлива на 100 км
                :param posx: начальная широта
                :param posy: начальная долгота
                :param posh: начальная Высота над уровнем моря
                :param rocket_type: тип ракет
                :param rocket_num: количество ракет
                Пример:
                >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 , "AnyName", 4)
                '''
        super.__init__(model, curfuel, expenses, posx,posy,posh)
        self.set_rocket_model(rocket_type)
        self.set_rocket_num(rocket_num)

    def set_rocket_model(self, model: str)->None:
        '''
        Устанавливает название модели ракеты
        :param model: название модели ракеты
        Пример:
        >>> my_plane = FightPlane("Super jet", 100000, 100, 0.0, 25.4, 4000.5, "AnyName", 4 )
        >>> my_plane.set_rocket_model("boing")
        '''
        if (not isinstance(model, str)):
            raise (TypeError("Incorrect type of rocket model"))
        self.rock_mod = model

    def set_rocket_num(self, numb : int)->None:
        '''
                Устанавливает количество ракет
                :param numb: количество ракет
                Пример:
                >>> my_plane = FightPlane("Super jet", 100000, 100, 0.0, 25.4, 4000.5, "AnyName", 4 )
                >>> my_plane.set_rocket_num(2)
                '''
        if (not isinstance(numb, int)):
            raise (TypeError("Incorrect type of rocket number"))
        self.rocknum = numb

    def __str__(self) -> None:
        return f"Боевой самолет модели {self.model} с расходом {self.expenses},количеством топлива {self.curfuel}, с начальными координатами {self.startx, self.starty, self.h} и ракетами типа {self.rock_mod} в количестве {self.rocknum} шт"

    def __repr__(self) -> None:
        return f"{self.__class__.__name__}(model={self.model}, curfuel={self.curfuel}, expenses={self.expenses}, posx={self.startx}, posy = {self.starty}, h = {self.h}, rock_mod= {self.rock_mod}, rocknum={self.rocknum})"
