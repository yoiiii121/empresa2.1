#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'


class Empleado():
    """

    Este módulo gestiona un Empleado

    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """

        Construye un empleado
        
        :param nombre: nombre de un empleado
        :param apellidos: apellidos de un empleado
        :param dni: dni de un empleado
        :param direccion: dirección de un empleado
        :param edad: edad de un empleado
        :param email: email de un empleado
        :param salario: salario anual que tiene un empleado

        """
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__dni = dni
        self.__direccion = direccion
        self.__edad = edad
        self.__email = email
        self.__salario = salario

    def get_salario(self):
        """

        :return: Devuelve el salario de un empleado
        :rtype: float

        """
        return round(self.__salario, 2)

    def get_dni(self):
        """

        :return: Devuelve un dni de un empleado
        :rtype: str

        """
        return self.__dni

    def get_nombre_completo(self):
        """

        :return: Devuelve el nombre de pila de un empleado
        :rtype: str

        """
        return self.__nombre + ' ' + self.__apellidos

    def get_edad(self):
        """

        :return: Devuelve la edad de un empleado
        :rtype: int

        """
        return int(self.get_edad())

    def get_email(self):
        """

        :return: Devuelve el email de un empleado
        :rtype: str

        """
        return str(self.get_email())

    def get_direccion(self):
        """

        :return: Devuelve la dirección de un empleado
        :rtype: str

        """
        return str(self.get_direccion())

    def get_salario_menusal(self):
        """

        :return: Devuelve el salario mensual de un empleado
        :rtype: float

        """
        return float(round(self.get_salario() / 12.0, 2))

    def __str__(self):
        """

        :return: Devuelve el formato de impresión de un objeto empleado
        :rtype: str

        """
        return 'Nombre ' + self.get_nombre_completo() + ' Dni ' + self.get_dni() + ' Salario ' + str(
            self.get_salario()) + ' Salario mensual ' + str(self.get_salario_menusal())