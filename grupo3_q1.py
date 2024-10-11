class ListaEncadeada(object):
  """Implementa uma lista encadeada"""

  class No(object):
    """Implementa um nó de lista encadeada"""
    def __init__(self, valor, proximo=None):
      self.valor = valor
      self.proximo = proximo

  def __init__(self):
    self.__primeiro_no = None

  def __str__(self):
    no = self.__primeiro_no
    s = ""
    while no:
      s += f" → {no.valor}" if s else str(no.valor)
      no = no.proximo
    return s

  def acessa(self, ind):
    """Retorna o item na posição ind da lista"""
    no = self.__primeiro_no
    while no and ind > 0:
      no = no.proximo
      ind -= 1
    if no:
      return no.valor

  def busca(self, item):
    """Retorna a posição do item (-1 se não encontra)"""
    no = self.__primeiro_no
    i = 0
    while no:
      if no.valor == item:
        return i
      no = no.proximo
      i += 1
    return -1

  def insere(self, item, ind=0):
    """Insere item na posição ind (padrão 0)"""
    if ind == 0 or not self.__primeiro_no:
      novo_no = self.No(item, self.__primeiro_no)
      self.__primeiro_no = novo_no
    else:
      no = self.__primeiro_no
      while no.proximo and ind > 1:
        no = no.proximo
        ind -= 1
      novo_no = self.No(item, no.proximo)
      no.proximo = novo_no

  def remove(self, ind=0):
    """Remove e retorna item da posição ind (padrão 0)"""
    if not self.__primeiro_no:
      return None
    if ind == 0:
      item = self.__primeiro_no.valor
      self.__primeiro_no = self.__primeiro_no.proximo
      return item
    no = self.__primeiro_no
    while no.proximo and ind > 1:
      no = no.proximo
      ind -= 1
    if no.proximo:
      item = no.proximo.valor
      no.proximo = no.proximo.proximo
      return item
  
lista = ListaEncadeada()
lista.insere("once")
lista.insere("upon", 1)
lista.insere("a", 2)
lista.insere("time", 3)

print(lista)
print(lista.acessa(3))
print(lista.busca("time"))
lista.remove(2)
print(lista)