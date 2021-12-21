"""
Chapitre 11.2
"""

import numbers
import copy
import collections
import collections.abc


class Matrix:
    """
    Matrice numérique stockée en tableau 1D en format rangée-major.

    :param height: La hauteur (nb de rangées)
    :param width: La largeur (nb de colonnes)
    :param data: Si une liste, alors les données elles-mêmes (affectées, pas copiées). Si un nombre, alors la valeur de remplissage
    """

    def __init__(self, height, width, data=0.0):
        if not isinstance(height, numbers.Integral) or not isinstance(width, numbers.Integral):
            raise TypeError()
        if height == 0 or width == 0:
            raise ValueError(numbers.Integral)
        self.__height = height
        self.__width = width
        if isinstance(data, list):
            if len(data) != len(self):
                raise ValueError(list)
            self.__data = data
        elif isinstance(data, numbers.Number):
            self.__data = [data for i in range(len(self))]
        else:
            raise TypeError()

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def data(self):
        return self.__data

    # ATTENTION, quand on a un property, apres, on doit designer l'attribut sans le __ !!
    # TODO: Accès à un élément en lecture
    def __getitem__(self, indexes):
        """
        Indexation rangée-major

        :param indexes: Les index en `tuple` (rangée, colonne)
        """
        if not isinstance(indexes, tuple):
            raise IndexError()
        if indexes[0] >= self.height or indexes[1] >= self.width:
            raise IndexError()

        return self.data[indexes[0] * self.width + indexes[1]]

    # TODO: Retourner la valeur

    # TODO: Affectation à un élément
    def __setitem__(self, indexes, value: float):
        """
        Indexation rangée-major

        :param indexes: Les index en `tuple` (rangée, colonne)
        """
        if not isinstance(indexes, tuple):
            raise IndexError()
        if indexes[0] >= self.height or indexes[1] >= self.width:
            raise IndexError()

        n = 0
        while n <= ((self.height * self.width) - 1):
            if n == indexes[1]:
                self.data[n] = value
            self.data[n] = 0

    # TODO: L'affectation

    def __len__(self):
        """
        Nombre total d'éléments
        """
        return self.height * self.width

    # TODO: Représentation affichable (conversion pour print)
    def __str__(self):
        # TODO: Chaque rangée est sur une ligne, avec chaque élément séparé d'un espace.
        empty_str = ''
        for n in self.data:
            if self.data.index(n) == self.width - 1:
                empty_str += f"{n}\n"
            else:
                empty_str += f"{n} "

        print(empty_str)

    # doesnt work
    # TODO: Représentation officielle
    def __repr__(self):
        # TODO: une string qui représente une expression pour construire l'objet.
        return self

    # !!!
    # TODO: String formatée
    def TODO(TODO):
        # TODO: On veut pouvoir dir comment chaque élément doit être formaté en passant la spécification de formatage qu'on passerait à `format()`
        pass

    def clone(self):
        return Matrix(self.height, self.width, self.data)

    def copy(self):
        return Matrix(self.height, self.width, copy.deepcopy(self.data))

    def has_same_dimensions(self, other):
        return (self.height, self.width) == (other.height, other.width)

    def __pos__(self):
        return self.copy()

    # ATTENTION!! On doit retourner toute formule Matrix
    # TODO: Négation
    def __neg__(self):
        for numb in self.data:
            self.data[self.__data.index(numb)] = -1 * numb
        return Matrix(self.height, self.width, self.data)

    # TODO: Addition
    def __add__(self, other):
        if not self.has_same_dimensions(other):
            raise ValueError(Matrix)
        result = Matrix(self.height, self.width)
        for i in range(len(self)):
            result.data[i] = self.data[i] + other.data[i]
        return result

    # TODO: Soustraction
    def __sub__(self, other):
        for n in range(len(self.data)):
            self.data[n] = self.data[n] - other[n]
            return self + -other

    # TODO: Multiplication matricielle/scalaire
    def TODO(TODO):
        if isinstance(other, Matrix):
            # TODO: Multiplication matricielle.
            # Rappel de l'algorithme simple pour C = A * B, où A, B sont matrices compatibles (hauteur_A = largeur_B)
            # C = Matrice(hauteur_A, largeur_B)
            # Pour i dans [0, hauteur_C[
            # Pour j dans [0, largeur_C[
            # Pour k dans [0, largeur_A[
            # C(i, j) = A(i, k) * B(k, j)
            pass
        elif isinstance(other, numbers.Number):
            # TODO: Multiplication scalaire.
            pass
        else:
            raise TypeError()

    # TODO: Multiplication scalaire avec le scalaire à gauche

    def __abs__(self):
        return Matrix(self.height, self.width, [abs(e) for e in self.data])

    # TODO: Égalité entre deux matrices

    @classmethod
    def identity(cls, width):
        result = cls(width, width)
        for i in range(width):
            result[i, i] = 1.0
        return result
