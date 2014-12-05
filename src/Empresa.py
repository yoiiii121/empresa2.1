#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Nacho-w7'


class Empresa():
    """

    Este módulo gestiona una Empresa

    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """

        Construye un objeto Empresa

        :param nombre_empresa: Nombre de una empresa
        :param cif: código de identificación físcal de una empresa
        :param razon_social:

        """
        self.__nombre_empresa = nombre_empresa
        self.__cif = cif
        self.__razon_social = razon_social
        self.__departamentos = []