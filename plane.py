class Plane:
    def __init__(self, model : str, curfuel: float, expenses : float, posx: float, posy: float, posh: float):
        '''
        Инициализация объекта "самолет"
        :param model: название модели
        :param curfuel: начальный объем топлива
        :param expenses: расход топлива на 100 км
        :param posx: начальная широта
        :param posy: начальная долгота
        :param posh: начальная Высота над уровнем моря
        Пример:
        >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 )
        '''
        a = self.transform_coord(posx, posy, posh)
        self.startx = a[0]
        self.starty = a[1]
        self.h = a[2]
        self.set_exsp(expenses)
        self.set_model(model)
        self.set_curfuel(curfuel)


    def can_complete_distance (self, posx: float, posy: float, posh: float)->bool:
        '''
        Выполняет проверку, долетит ли самолет до точки из начальных координат
        :param posx: конечная широта
        :param posy: конечная долгота
        :param posh:конечная  Высота над уровнем моря
        Пример:
        >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 )
        >>> my_plane.can_complete_distance(100.4, 22.3, 3990.3)
        '''
        pass

    def set_model(self, model: str)->None:
        '''
        Устанавливает название модели
        :param model: название модели
        Пример:
        >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 )
        >>> my_plane.set_model("boing")
        '''
        if (not isinstance(model, str)):
            raise (TypeError("Incorrect type of model"))
        self.model = model

    def set_curfuel(self, curfuel: float)->None:
        '''
        Устанавливает текущий объем топлива
        :param curfuel: текущий объем топлива
        Пример:
        >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 )
        >>> my_plane.set_curfuel(90000)
        '''
        if (not isinstance(curfuel, float)):
            raise(TypeError("Incorrect type of curfuel"))
        if (curfuel < 0):
            raise (ValueError("curfuel can`t be negative"))
        self.curfuel = curfuel
    def set_exsp(self, expenses: float):
        '''
        Устанавливает расход топлива
        :param expenses: расход топлива
        Пример:
        >>> my_plane = Plane("Super jet", 100000, 100, 0.0, 25.4, 4000.5 )
        >>> my_plane.expenses(120)
        '''
        if (not isinstance(expenses, float)):
            raise(TypeError("Incorrect type of expenses"))
        self.expenses = expenses


    def transform_coord (self, posx: float, posy: float, posh: float) ->list:
        '''
        Проверяет координаты на корректность ввода
        :param posx: широта
        :param posy: долгота
        :param posh: Высота над уровнем моря
        Пример:

        '''
        if (not isinstance(posx, float)):
            raise(TypeError("Incorrect type of x position"))
        if (abs(posx)>= 180):
            raise (ValueError("To big value of x"))
        if (not isinstance(posy, float)):
            raise(TypeError("Incorrect type of y position"))
        if (abs(posy)>= 180):
            raise (ValueError("To big value of y"))
        if (not isinstance(posh, float)):
            raise(TypeError("Incorrect type of h position"))
        return [posx, posy, posh]
    def __str__(self)->None:
        return f"Самолет модели {self.model} с расходом {self.expenses},количеством топлива {self.curfuel}, с начальными координатами {self.startx, self.starty, self.h}"

    def __repr__(self)->None:
        return f"{self.__class__.__name__}(model={self.model}, curfuel={self.curfuel}, expenses={self.expenses}, posx={self.startx}, posy = {self.starty}, h = {self.h})"

