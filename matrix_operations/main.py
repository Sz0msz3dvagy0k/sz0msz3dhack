def beolvas_matrix(matrix_str):
  """
  Beolvassa a mátrixot a bemeneti stringből.

  Args:
    matrix_str: A bemeneti string, amely a mátrix elemeit tartalmazza.

  Returns:
    Egy lista, amely a mátrix elemeit tartalmazza.
  """
  sorok = matrix_str.strip().split("\n")
  matrix = []
  for sor in sorok:
    matrix_sor = [int(elem) for elem in sor.strip().split()]
    matrix.append(matrix_sor)
  return matrix

def osszead_matrix(matrix1, matrix2):
  """
  Két mátrix összeadása.

  Args:
    matrix1: Az első mátrix.
    matrix2: A második mátrix.

  Returns:
    Az összegzett mátrix.
  """
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    raise ValueError("A mátrixoknak azonos méretűnek kell lenniük az összeadáshoz.")
  eredmeny_matrix = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      eredmeny_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
  # Use function arguments directly in the print statement
  print(f"{matrix1} + {matrix2} eredménye:")
  for sor in eredmeny_matrix:
    print(sor)
  return eredmeny_matrix

def szoroz_matrix(matrix1, matrix2):
  """
  Két mátrix szorzása.

  Args:
    matrix1: Az első mátrix.
    matrix2: A második mátrix.

  Returns:
    A szorzatmátrix.
  """
  if len(matrix1[0]) != len(matrix2):
    raise ValueError("Az első mátrix oszlopának számának meg kell egyeznie a második mátrix sorainak számával a szorzáshoz.")
  eredmeny_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
  for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
      for k in range(len(matrix2)):
        eredmeny_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
  print(f"{matrix1} * {matrix2} eredménye:")
  for sor in eredmeny_matrix:
    print(sor)
  return eredmeny_matrix

def main():
  """
  A program fő függvénye.
  """
  # Beolvassa a mátrixokat és a műveleteket a fájlból.
  with open("input.txt") as f:
    matrixek_str = f.read()
  matrixek_str_sorok = matrixek_str.split("\n\n")
  matrixek = {}
  muveletek = []
  for sorok in matrixek_str_sorok:
    if sorok.startswith("matrices"):
      for matrix_str in sorok.strip().split("\n")[1:]:
        matrix_nev, matrix_elemek_str = matrix_str.split("\n", 1)
        matrixek[matrix_nev] = beolvas_matrix(matrix_elemek_str)
    elif sorok.startswith("operations"):
      for muvelet_str in sorok.strip().split("\n")[1:]:
        muveletek.append(muvelet_str)
