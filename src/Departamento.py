#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'


class Departamento():
    """

    Este módulo gestiona un departamento

    """
    def __init__(self, nombre_depto, id_depto):
        """

        Construye un objeto Departamento

        :param nombre_depto: nombre del departamento
        :param id_depto: Identificador de departamento

        """
        self.__nombre_depto = nombre_depto
        self.__id_depto = id_depto
        self.__empleado = []

    def anyadir_emplado(self, empleado):
        """

        Añade un empleado a la lista de empleados del departamento

        :param empleado: Objeto tipo Empleado

        """
        self.__empleado.append(empleado)

    def get_salario_total(self):
        """

        :return: Devuelve el salario anual de todos los empleados del departamento
        :rtype: float

        """
        return round(float(sum([i.get_salario() for i in self.__empleado])), 2)

    def get_salario_total_mensual(self):
        """

        :return: Devuelve el salario mensual de todos los empleados del departamento
        :rtype: float

        """
        return round(float(sum([i.get_salario_menusal() for i in self.__empleado])), 2)

    def get_nombre_depto(self):
        """

        :return: Devuelve el nombre del departamento
        :rtype: str

        """
        return self.__nombre_depto

    def __str__(self):
        """

        :return: Devuelve el formato de impresión de un objeto Departamento
        :rtype: str

        """
        return 'Salario total ' + str(self.get_salario_total()) + 'Salario total mensual' + str(
            self.get_salario_total_mensual())