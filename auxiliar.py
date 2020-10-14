from functools import reduce

# Está função avalia a igualdade entre os vetores dados #
__equals = lambda x, y: True if (x == y) else False
# Está função reduz a resposta a 0 ou 1
__multip = lambda x, y: x * y
# 0 ou 1 ~ True ou False #
__check = lambda x: False if (x == 1) else True


def __best__(vec1, vec2):
    for i in range(0, len(vec1)):
        if vec1[i] != 0 and vec2[i] != 0:
            return vec1[i]
    return 1


# Está função verifica a existencia do vetor nulo #
def __null__(vec):
    for i in range(0, len(vec)):
        vetorNulo = True
        for j in range(0, len(vec)):
            if vec[i][j] != 0:
                vetorNulo = False
                break

        if vetorNulo is True:
            return vetorNulo

    for i in range(0, len(vec)):
        vetorNulo = True
        for j in range(0, len(vec)):
            if vec[j][i] != 0:
                vetorNulo = False
                break

        if vetorNulo is True:
            return True

    return vetorNulo


# Está função compara o resultado dois a dois #
def __ind_lin__(vec1, vec2):
    # Copiando os vetores para não tratar diretamente no original #
    vec1 = vec1[:]
    vec2 = vec2[:]

    # multiplicador para igualar os primeiros elementos #

    multi = lambda x: x * y

    y = __best__(vec2, vec1)
    temp1 = list(map(multi, vec1))
    y = __best__(vec1, vec2)
    temp2 = list(map(multi, vec2))

    # Retornando o resultado da igualdade #
    return reduce(__multip, list(map(__equals, temp1, temp2)))


def independencia_linear(lista):
    independencia = False

    for i in range(0, len(lista)):

        for j in range(i + 1, len(lista)):

            independencia = __ind_lin__(lista[i], lista[j])
            if independencia == 1:
                return __check(independencia)
    if __check(independencia) is True and __null__(lista) is False:
        return True
    else:
        return False
