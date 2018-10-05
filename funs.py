from numpy import roots
from random import choice
from mincir import make_circle


def complex_to_tuple(c: list):
    t = []
    for e in c:
        e = complex(e)
        t.append((e.real, e.imag))
    return t


def get_rand_poly(deg, coeff_radius):
    coeff_minor = list(range(-coeff_radius, coeff_radius + 1))
    coeff_major = list(range(-coeff_radius, coeff_radius + 1))
    coeff_major.remove(0)
    poly = [choice(coeff_major)]
    for _ in range(deg - 1):
        poly.append(choice(coeff_minor))
    return poly


def get_rouche_radius(poly: list):
    a = []
    for i in range(1, len(poly)):
        a.append(abs(poly[i] / poly[0]))
    return 1 + max(a)


def get_real_radius(poly: list):
    poly_roots = roots(poly)
    points = complex_to_tuple(poly_roots)
    circle = make_circle(points)
    return circle[2]


def get_zero_center_radius(poly: list):
    poly_roots = roots(poly)
    modules = []
    for e in poly_roots:
        modules.append(abs(e))
    return max(modules)


def get_min_cir_vs_rouche_stat(exper_num, deg, coeff_radius):
    ratios = []
    for _ in range(exper_num):
        p = get_rand_poly(deg, coeff_radius)
        ratio = get_real_radius(p) / get_rouche_radius(p)
        ratios.append(ratio)
    return ratios


def get_zero_center_vs_rouche_stat(exper_num, deg, coeff_radius):
    ratios = []
    for _ in range(exper_num):
        p = get_rand_poly(deg, coeff_radius)
        ratio = get_zero_center_radius(p) / get_rouche_radius(p)
        ratios.append(ratio)
    return ratios


def get_min_cir_vs_zero_center_stat(exper_num, deg, coeff_radius):
    ratios = []
    for _ in range(exper_num):
        p = get_rand_poly(deg, coeff_radius)
        ratio = get_real_radius(p) / get_zero_center_radius(p)
        ratios.append(ratio)
    return ratios