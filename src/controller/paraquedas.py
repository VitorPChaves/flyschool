from src.entity.paraquedas import Paraquedas


class ParachuteController:

    def __init__(self):
        self.__parachute_inventory = []

        self.__parachute1 = Paraquedas('Vermelho', True)
        self.__parachute2 = Paraquedas('Azul', True)
        self.__parachute3 = Paraquedas('Verde', True)

        self.inventory()

    # Alterar codigo para cadastro de paraquedas
    def inventory(self):
        self.__parachute_inventory.append(self.__parachute1)
        self.__parachute_inventory.append(self.__parachute2)
        self.__parachute_inventory.append(self.__parachute3)

    def check_parachutes(self, aluno):
        for index, parachute in self.__parachute_inventory:
            next_parachute = self.__parachute_inventory[index + 1]

            # Checa se há paraquedas disponíveis
            if parachute.status:
                if aluno.nivel == 'EXPERIENTE':
                    # self.__parachute.status = False
                    self.reserve_parachutes(parachute)
                    return True
                elif next_parachute.status:
                    # self.__parachute.status = False
                    # next_parachute.status = False
                    self.reserve_parachutes(parachute)
                    self.reserve_parachutes(next_parachute)
                    return True
        return False

    def refill_parachutes(self):
        for parachute in self.__parachute_inventory:
            parachute.status = True

    def reserve_parachutes(self, paraquedas):
        paraquedas.status = False
        print(self.__parachute_inventory)



