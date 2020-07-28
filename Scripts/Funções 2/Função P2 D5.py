def notas(*notas, sit=False):
    """
    =>Função para analisar notas e situações de vários alunos
    :param notas: As notas a ser digitadas
    :param sit: (opcional). Situação do aluno
    :return: Dicionário com várias informações sobre a situação da turma
    """
    total = dict()
    total['total'] = len(notas)
    total['maior'] = max(notas)
    total['menor'] = min(notas)
    total['média'] = sum(notas)/len(notas)
    if sit:
        if total['média'] >= 7:
            total['situação'] = 'Boa'
        elif total['média'] >= 5:
            total['situação'] = 'Razoável'
        else:
            total['situação'] = 'Ruim'
    return total


resp = notas(5.5, 2.5, 10, 6.5, sit=True)
help(notas)
