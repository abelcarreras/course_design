from iofile import get_molecule_from_file


data_dir = 'data'

print('Center of mass\n')
for file_name in ['water.xyz', 'ethylene.xyz', 'methane.xyz']:
    molecule = get_molecule_from_file(data_dir + '/' + file_name)
    print('{:20}'.format(file_name), '{:10.5f} {:10.5f} {:10.5f}'.format(*molecule.get_center_of_mass()))
