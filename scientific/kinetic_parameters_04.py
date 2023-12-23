#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
To calculate kinetic and thermodynamic parameters 
of the reference: 

J. Phys. Chem. C 2014, 118, 6706-6718
"""

from decimal import Decimal, getcontext
from pprint import pprint
from typing import Union

import numpy as np
from print_fence import print_fence

getcontext().prec = 40

R = "8.31446261815324" # molar gas constant; unit: J*K^{-1}*mol^{-1}
k_B = "8.617333262145e-5" # Boltzmann constant; unit: eV/K
h = "4.135667696e-15" # Planck constant; unit: eV*s
elem_charge = "1" # elementary charge; unit: Hartree atomic units
U = "0.9" # The voltage; unit: Volt vs RHE
beta_i = "0.5" # unit: dimensionless 
E0_ai = "0.26" # unit: eV


def get_TST_rate_constant(G_ai: Union[int, float], 
                          T: Union[int, float]=300) -> float:
    """
    Formula (16): 
    Return the rate constant "k" according to TST theory. 
    """
    k_B_decimal = Decimal(k_B)
    h_decimal = Decimal(h)
    T_decimal = Decimal(T)
    G_ai_decimal = Decimal(G_ai)

    k_i = (
        ((k_B_decimal*T_decimal) / h_decimal) 
        * Decimal.exp(-G_ai_decimal / (k_B_decimal*T_decimal))
    )
    return float(k_i)


def get_TST_equilibrium_constant(delta_G_i: Union[int, float], 
                                 T: Union[int, float]=300) -> float:
    """
    Formula (22): 
    Return the equilibrium constant "K" according to TST theory. 
    """
    k_B_decimal = Decimal(k_B)
    T_decimal = Decimal(T)
    delta_G_i_decimal = Decimal(delta_G_i)

    K_i = Decimal.exp(-delta_G_i_decimal / (k_B_decimal*T_decimal))
    return float(K_i)


def get_total_effect_diffusion_reaction(delta_G_i: Union[int, float]) -> Union[int, float]:
    """
    Calculate the total effect 
    of diffusion and reaction to Ea. 
    """
    delta_G_i_decimal = Decimal(delta_G_i)
    beta_i_decimal = Decimal(beta_i)

    if float(-beta_i_decimal * delta_G_i_decimal) > 0.26:
        Ea = 0
    elif float((1-beta_i_decimal) * delta_G_i_decimal) > 0.26:
        Ea = float(delta_G_i_decimal)
    else:
        Ea = 0.26 + float(beta_i_decimal*delta_G_i_decimal)
    return Ea


def get_reverse_rate_constant(k_f: Union[int, float], 
                              K: Union[int, float]) -> Union[int, float]:
    """
    Get the reverse rate constant 
    using the rate constant and the equilibrium constant. 
    """
    return k_f / K





if __name__ == "__main__":

    read_coverage_01 = np.loadtxt(
        open(
            "D:/zigzag/postgraduate/received_WeChat/catmap-test-2023-08-22/coverage-1.csv", 
            "r"
        ), 
        delimiter=",", skiprows=1, usecols=[i for i in range(1, 7)]
    )

    read_delta_G_02 = np.loadtxt(
        open(
            "D:/zigzag/postgraduate/received_WeChat/catmap-test-2023-08-22/delta_G_02.csv", 
            "r"
        ), 
        delimiter=",", skiprows=1, usecols=[i for i in range(1, 7)]
    )

    get_total_effect_diffusion_reaction_vectorized = np.vectorize(
        get_total_effect_diffusion_reaction
    )

    E_a_array = get_total_effect_diffusion_reaction_vectorized(read_delta_G_02)

    get_TST_rate_constant_vectorized = np.vectorize(
        get_TST_rate_constant
    )

    k_forward_array = get_TST_rate_constant_vectorized(E_a_array)

    get_TST_equilibrium_constant_vectorized = np.vectorize(
        get_TST_equilibrium_constant
    )

    K_eq_array = get_TST_equilibrium_constant_vectorized(read_delta_G_02)

    get_reverse_rate_constant_vectorized = np.vectorize(
        get_reverse_rate_constant
    )

    k_reverse_array = get_reverse_rate_constant_vectorized(k_forward_array, K_eq_array)

    print(E_a_array)
    print(k_forward_array)
    print(K_eq_array)
    print(k_reverse_array)

    #np.savetxt("C:/Users/user/Downloads/k_forward_array.csv", k_forward_array, delimiter=",")
    #np.savetxt("C:/Users/user/Downloads/K_eq_array.csv", K_eq_array, delimiter=",")
    #np.savetxt("C:/Users/user/Downloads/k_reverse_array.csv", k_reverse_array, delimiter=",")

    read_coverage_02 = np.loadtxt(
        open(
            "C:/Users/user/Downloads/002.csv", 
            "r"
        ), 
        delimiter=",", skiprows=1, usecols=[i for i in range(1, 7)]
    )

    np.savez(
        "C:/Users/user/Downloads/read_coverage_02.npz", 
        read_coverage_02=read_coverage_02
    )

    print(read_coverage_02)
    print(type(read_coverage_02))
    print(read_coverage_02.shape)
