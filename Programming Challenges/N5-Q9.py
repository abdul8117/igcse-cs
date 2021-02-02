# ask no. of carbon atoms
# calc no. of hydrogen atoms
# atomic weight/mass = nC * 12 + nH * 1


def calc_atomic_mass(nCarbon, nHydrogen):
    return nCarbon * 12 + nHydrogen

def main():
    n_carbon = int(input("Number of carbon atoms:\n"))
    n_hydrogen = (n_carbon * 2) + 2

    atomic_mass = calc_atomic_mass(n_carbon, n_hydrogen)

    print(f"Atomic mass of C{n_carbon}H{n_hydrogen} is\n{atomic_mass}")

main()