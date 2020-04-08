#Exercio 1#
class Funcionario:

    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
    
    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def set_nome (self, nome):
      self.__nome = nome

    def get_salario(self):
        return self.__salario

    def set_cpf(self, cpf):
        if len(cpf) == 11:
            self.__cpf = cpf
        else:
            print("Erro - cpf invalido")

    def set_salario(self, salario):
        self.__salario = salario
    
func1 = Funcionario("Pedro", "", 1500.0)
func1.salario = 3000.0              
print("Nome:", func1.get_nome())
cpf = input ("CPF: ")
func1.set_cpf(cpf)

print("Salário:", func1.get_salario())


