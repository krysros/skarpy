import argparse
import ezdxf
import numpy as np

parser = argparse.ArgumentParser(description='Save coords of points from DXF file as NumPy arrays in .npz file')
parser.add_argument('filename', help='DXF file')
args = parser.parse_args()

print('Reading DXF...')
dwg = ezdxf.readfile(args.filename)
modelspace = dwg.modelspace()
points = modelspace.query('POINT[layer=="PY"]')

print('Preparing numpy arrays...')
coords = np.array([p.dxf.location for p in points])
x = coords[:, 0]
y = coords[:, 1]
z = coords[:, 2]

print('Saving to file...')
np.savez(args.filename[:-4] + '.npz', x=x, y=y, z=z)
