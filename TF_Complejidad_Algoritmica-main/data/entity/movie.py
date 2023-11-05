class Pelicula:
  def __init__(self,id,name,year,age,rating, category,subcategory,franquicia,netflix,hulu, prime,disney):
       self.id=id
       self.name = name
       self.year=year
       self.age=age
       self.rating=rating
       self.category=category
       self.subcategory=subcategory
       self.franquicia = franquicia
       self.netflix=netflix
       self.hulu=hulu
       self.prime = prime
       self.disney=disney
       self.peso = self.setPeso()

  def getID(self):
      return self.id
  def getName(self):
      return self.name
  def getYear(self):
      return self.year
  def getAge(self):
      return self.age
  def getRating(self):
      return self.rating
  def getCategory(self):
      return self.category
  def getsubCategory(self):
      return self.subcategory
  def getFranquicia(self):
      return self.franquicia
  def getnetflix(self):
      return self.netflix
  def gethulu(self):
      return self.hulu
  def getPrime(self):
      return self.prime
  def getDisney(self):
      return self.disney
  def getPeso(self):
      return self.peso

  def setPeso(self):
    if self.name == "Netflix" or self.name == "Hulu" or self.name == "Disney+" or self.name == "Prime":
      self.peso = 0
      return

    #Calcular edad
    if self.age == "all":
      edad = 0
    else:
      edad = int(self.age.split("+")[0])

    #Calcular puntaje
    puntaje = int(self.rating.split("/")[0])

    #Calcular categoría
    if self.category == "Comedia" or self.category == "Acción" or self.category == "Aventura":
      categoria = 5
    elif self.category == "Ciencia Ficción" or self.category == "Romance" or self.category == "Terror" or self.category == "Fantasía" or self.category == "Drama" or self.category == "Misterio":
      categoria = 4
    elif self.category == "Crimen" or self.category == "Musical" or self.category == "Súper Héroes" or self.category == "Princesas":
      categoria = 3
    elif self.category == "Navidad" or self.category == "Halloween":
      categoria = 2
    else:
      categoria = 1

    #Calcular subcategoría
    if self.subcategory == "Comedia" or self.subcategory == "Acción" or self.subcategory == "Aventura":
      subcategoria = 5
    elif self.subcategory == "Ciencia Ficción" or self.subcategory == "Romance" or self.subcategory == "Terror" or self.subcategory == "Fantasía" or self.subcategory == "Drama" or self.subcategory == "Suspenso" or self.subcategory == "Misterio":
      subcategoria = 4
    elif self.category == "Crimen" or self.category == "Musical" or self.category == "Familia":
      subcategoria = 3
    elif self.category == "Navidad":
      subcategoria = 2
    elif self.subcategory == "Animal" or self.subcategory == "Documental" or self.subcategory == "Deporte":
      subcategory = 1
    else:
      categoria = 0

    #Calcular peso
    peso = int((((2100 - self.year) + (edad * 5) + (100 - puntaje))/(categoria + (subcategoria/2))) * (4/(self.disney+self.netflix+self.hulu+self.prime)))
    return peso
