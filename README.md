# matrix-to-scad

This is a simple utility that can take a 3D matrix of integers (1s and 0s) and generate the OpenSCAD code to render a 3D scene with cubes placed at the locations of 1s in the matrix. A parameter `voxel_dim` defines the length of the cube shaped voxels in the matrix. Simply take the returned code and paste it into OpenScad to take your matrix and turn it into an STL. 

## Example
```py
 sample_matrix = [
        [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ],
        [
            [1, 1, 1],
            [0, 1, 0],
            [0, 1, 0],
        ],
    ]

    print(matrix_to_scad(sample_matrix, 1))
```
Prints OpenSCAD code that renders the following:
