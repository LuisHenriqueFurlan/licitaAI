pregoes_cache = []


def salvar_pregoes(dados):

    global pregoes_cache

    pregoes_cache = dados


def obter_pregoes():

    return pregoes_cache