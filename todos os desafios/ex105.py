# programa que tem uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações
# quantidade de notas; a maior nota; a menor; a média da turma; e a situação que é opcional
# add docstring


def notas(*n, sit=False):
    """

    :param n: São as notas dos alunos ficticios
    :param sit: É a situação da sala, resultado adquirido a partir da média desta
    :return: O dicionario 'r', é onde está localizado a analise das notas
    """
    r = dict()
    r['numero de notas'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = float(f'{sum(n)/len(n):.2f}')
    if sit:
        if r['media'] < 5:
            r['situação'] = 'RUIM'
        elif r['media'] < 7:
            r['situação'] = 'PAIA'
        elif r['media'] <= 10:
            r['situação'] = 'BOM'
        else:
            r['situação'] = 'ESTRONDO'
    return r


# main
help(notas)
resp = notas(5.5, 9.5, 10.0, 6.5, 4.2, 0.5, 2, 4.5, sit=True)
print(resp)
