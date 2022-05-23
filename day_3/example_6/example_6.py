from iofile import get_molecule_from_file


print('Center of mass\n')
for file_name in ['water.xyz', 'ethylene.xyz', 'methane.xyz']:
    water_molecule = get_molecule_from_file(file_name)
    print('{:20}'.format(file_name), '{:10.5f} {:10.5f} {:10.5f}'.format(*water_molecule.get_center_of_mass()))
