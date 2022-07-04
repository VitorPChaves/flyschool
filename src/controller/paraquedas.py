from src.entity import Aluno
from src.entity.day import Day
from src.entity.paraquedas import Paraquedas


class ParachuteController:

    def __init__(self):
        self.__parachute_inventory = []
        self.__day = []
        self.__parachute1 = Paraquedas('Vermelho', True, Day())
        self.__parachute2 = Paraquedas('Azul', True, Day())
        self.__parachute3 = Paraquedas('Verde', True, Day())

        self.inventory()

    # Alterar codigo para cadastro de paraquedas
    def inventory(self):
        self.__parachute_inventory.append(self.__parachute1)
        self.__parachute_inventory.append(self.__parachute2)
        self.__parachute_inventory.append(self.__parachute3)

    def check_parachutes(self, aluno: Aluno, day: str, period: str):
        for index, parachute in enumerate(self.__parachute_inventory):
            try:
                # Checa se há paraquedas disponíveis e retorna um valor booleano
                if parachute.day.days[day][period]:
                    if aluno.nivel.name == 'EXPERIENTE':
                        # self.__parachute.status = False
                        self.reserve_parachutes(parachute, period)
                        return True
                    else:
                        next_parachute = self.__parachute_inventory[index + 1]
                        if next_parachute.day.days[day][period]:
                            # self.__parachute.status = False
                            # next_parachute.status = False
                            self.reserve_parachutes(parachute, day, period)
                            self.reserve_parachutes(next_parachute, day, period)
                            return True
                        return False
            except:
                return False

    # Deve "encher" cada aula com paraquedas disponiveis após o instrutor confirmar a aula e dar presença aos alunos
    def refill_parachutes(self):
        for parachute in self.__parachute_inventory:
            parachute.status = True

    def reserve_parachutes(self, parachute, dia, turno):
        parachute.status = False
        parachute.day.days[dia][turno] = False
        print(self.__parachute_inventory)
        print(parachute)
        print(parachute.status)



