class Pokemon():
    def __init__(self, id, especie, peso, altura, tipo):
        self._id = id
        self._especie = especie
        self._peso = peso
        self._altura = altura
        self._tipo = tipo

    def sqlInserirPokemon(self):

        sql = f'''
        INSERT INTO "Pokemons"
        Values('{self._id}','{self._especie}','{self._peso}', '{self._altura}', '{self._tipo}')  
        '''
        return sql