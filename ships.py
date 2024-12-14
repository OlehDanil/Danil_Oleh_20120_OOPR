
from pprint import pprint
import random

class Ship:

    """
    класс для представления кораблей
    """
    def __init__(self, length, tp = 1, x = None, y = None) -> None:
        self._length = length
        self._tp = tp
        self._x = x
        self._y = y
        self._is_move = True
        self._cells = [1 for _ in range(length)]
        self._field = None


    def __getitem__(self, item) -> None:
        return self._cells[item]

    def __setitem__(self, key, value) -> None:
        self._cells[key] = value

    def set_start_coords(self,x,y) -> None:
        self._x = x
        self._y = y


    def get_start_coords(self) -> tuple:
        return self._x, self._y

    def move(self, go):
        if not self._is_move:
            return False
        
        if self._field is None:
            if self._tp == 1:
                self._x += go
                return
            if self._tp == 2:
                self._y += go
                return
        
        if self._tp == 1:
            temp = self._x
            self._x += go
            if self.is_out_pole(self._field._size):
                self._x = temp
                return False
            for otherShip in self._field._ships:
                if self.is_collide(otherShip):
                    self._x = temp
                    return False
            return True
        
        if self._tp == 2:
            temp = self._y
            self._y += go
            if self.is_out_pole(self._field._size):
                self._y = temp
                return False
            for otherShip in self._field._ships:
                if self.is_collide(otherShip):
                    self._y = temp
                    return False
            return True
        

    def is_collide(self, ship):
        if ship._x == None and ship._y == None:
            return False
        
        selfSet, _1 = self.__coordsShips()
        selfSet = set(selfSet)
        _2 , otherWithRangeSet = ship.__coordsShips()
        otherWithRangeSet = set(otherWithRangeSet)
        if selfSet.intersection(otherWithRangeSet):
            return True
        return False
        
    def __coordsShips(self):
        if self._tp == 1: #horizont
            cordship = {(self._x+i, self._y): cells for cells in self._cells for i in range(self._length)}
            defcord = {(x,y) for x in range(self._x -1, self._x+self._length+1) for y in range(self._y-1,self._y+2)}
            return cordship , defcord
        if self._tp == 2: #vertical
            cordship = {(self._x, self._y+i): cells for cells in self._cells for i in range(self._length)}
            defcord = {(x,y) for x in range(self._x -1, self._x+2) for y in range(self._y-1,self._y + self._length+1)}
            return cordship , defcord


    '''def is_out_pole(self, size) -> bool:
        if self._tp == 2: #horizont
            if self._x in range(size) == False:
                return False
            if self._y in range(size) == False:
                return False
            if self._length >= size - self._x + 1:
                return True
            return False
        
        if self._tp == 1: #vertical
            if self._x in range(size) == False:
                return False
            if self._y in range(size) == False:
                return False
            if self._length >= size - self._y + 1:
                return True
        return False'''
    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x not in range(size):
                return True
            if self._y not in range(size):
                return True
            if self._length >= size - self._x + 1:
                return True
            return False
    
        if self._tp == 2:
            if self._x not in range(size):
                return True
            if self._y not in range(size):
                return True
            if self._length >= size - self._y + 1:
                return True
            return False
    
'''ship = Ship(2,1,3,4)
s2 = Ship(4,1,3,2)
ship[1] = 2
#print(ship.get_start_coords(),s2.get_start_coords())
#print(ship.__coordsShips(), s2.__coordsShips()[1])
print(ship.is_collide(s2))'''

class GamePole:

    """
    класс для описания игрового поля
    """

    def __init__(self, size:int = 10) -> None:
        self._size = size
        self._ships = list()

    def init(self):
        for sizeship, count in [(1, 4), (2, 3), (3, 2), (4, 1)]:
            for _ in range(count):
                self._ships.append(Ship(sizeship, random.choice([1, 2])))
        for ship in self._ships:
            ship._field = self
            while ship._x == None and ship._y == None:
                ship._x = random.randint(0, self._size -1)
                ship._y = random.randint(0, self._size -1)

                if ship.is_out_pole(self._size):
                    ship._x = None
                    ship._y = None
                    continue

                for otherShip in self._ships:
                    if id(ship) == id(otherShip):
                        continue
                    if ship._x == None and ship._y == None:
                        continue
                    if ship.is_collide(otherShip):
                        ship._x = None
                        ship._y = None
                        continue
    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            i = random.randrange(-1, 2, 2)
            if ship.move(i):
                continue
            elif ship.move(-i):
                continue

    def show(self):
        field = self.__fill_field()
        pprint(field)

    def __fill_field(self):
        _field = [[0 for _ in range (self._size)] for _ in range(self._size)]
        return _field

    def get_pole(self):
        _field = self.__fill_field()
        field_tuple = [tuple(item) for item in _field]
        return tuple(field_tuple)



def test():
    # Tests
    ship = Ship(2)
    ship = Ship(2, 1)
    ship = Ship(3, 2, 0, 0)
    assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
    assert ship._cells == [1, 1, 1], "неверный список _cells"
    assert ship._is_move, "неверное значение атрибута _is_move"
    ship.set_start_coords(1, 2)
    assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
    assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
    ship.move(1)
    s1 = Ship(4, 1, 0, 0)
    s2 = Ship(3, 2, 0, 0)
    s3 = Ship(3, 2, 0, 2)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
    assert s1.is_collide(
        s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
    s2 = Ship(3, 2, 1, 1)
    assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
    s2 = Ship(3, 1, 8, 1)
    assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
    s2 = Ship(3, 2, 1, 5)
    assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
    s2[0] = 2
    assert s2[0] == 2, "неверно работает обращение ship[indx]"
    p = GamePole(10)
    p.init()
    for nn in range(5):
        for s in p._ships:
            assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
            for ship in p.get_ships():
                if s != ship:
                    print(s._length, s._x, s._y, s._tp,'|||', ship._length, ship._x, ship._y, ship._tp)
                    assert s.is_collide(ship) == False  , "корабли на игровом поле соприкасаются"
        p.move_ships()
        print('movement')

    gp = p.get_pole()
    assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
    assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
    pole_size_8 = GamePole(8)
    pole_size_8.init()
    print("\n Passed")

test()
'''s1 = Ship(1,1,9,6)
s2 = Ship(1,2,9,5)
print(s1.is_collide(s2))
'''