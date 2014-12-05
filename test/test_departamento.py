#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase
from mockito import *
from src.Empleados import Empleado
from src.Departamento import Departamento


__author__ = 'Nacho-w7'



class TestDepartamento(TestCase):
    """

    Comprueba que los métodos complicados de Departamento funcionan

    """
    def test_get_salario_total(self):
        """

        Test que comprueba los valores y el tipo que devuelve el saldo anual de todos los empleados de un departamento
        Instanciación de un objeto de una clase solo centrandose en algunos atributos con ayuda de la función mock

        """
        em1 = mock(Empleado)
        when(em1).get_salario().thenReturn(1000.56)
        em2 = mock(Empleado)
        when(em2).get_salario().thenReturn(954.23)
        em3 = mock(Empleado)
        when(em3).get_salario().thenReturn(1000.56)
        dep1 = Departamento('Movistar', 'id001')
        self.assertIsInstance(dep1.get_salario_total(), float)
        self.assertEqual(dep1.get_salario_total(), 0.0)
        dep1.anyadir_emplado(em1)
        self.assertEqual(dep1.get_salario_total(), 1000.56)
        dep1.anyadir_emplado(em2)
        self.assertEqual(dep1.get_salario_total(), 1954.79)
        dep1.anyadir_emplado(em3)
        self.assertEqual(dep1.get_salario_total(), 2955.35)

    def test_get_salario_total_mensual(self):
        """

        Test que comprueba los valores y el tipo que devuelve el saldo mensual de todos los empleados de un departamento
        Instanciación de un objeto de una clase solo centrandose en algunos atributos con la ayuda de la función mock

        """
        em1 = mock(Empleado)
        when(em1).get_salario_menusal().thenReturn(83.38)
        em2 = mock(Empleado)
        when(em2).get_salario_menusal().thenReturn(79.52)
        em3 = mock(Empleado)
        when(em3).get_salario_menusal().thenReturn(83.38)
        dep1 = Departamento('Movistar', 'id001')
        self.assertIsInstance(dep1.get_salario_total(), float)
        self.assertEqual(dep1.get_salario_total_mensual(), 0.0)
        dep1.anyadir_emplado(em1)
        self.assertEqual(dep1.get_salario_total_mensual(), 83.38)
        dep1.anyadir_emplado(em2)
        self.assertEqual(dep1.get_salario_total_mensual(), 162.9)
        dep1.anyadir_emplado(em3)
        self.assertEqual(dep1.get_salario_total_mensual(), 246.28)
