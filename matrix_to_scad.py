from typing import List
import solid as sp


def matrix_to_scad(mat: List[List[List[int]]], voxel_dim: float) -> str:
    """
    matrix_to_scad returns generated openscad code to render a 3D scene with cubes of length voxel_dim placed at every
    x, y, z location where the input matrix is equal to 1.
    :param mat:
    :param voxel_dim:
    :return: generated openscad code
    """
    op_list = []
    for x in range(0, len(mat)):
        for z in range(0, len(mat[0])):
            for y in range(0, len(mat[0][0])): 
                if mat[x][z][y] == 1:
                    op_list.append(sp.translate([x * voxel_dim, y * voxel_dim, z * voxel_dim])(sp.cube(voxel_dim)))
    
    u = sp.union()(op_list)
    return sp.scad_render(u)


if __name__ == "__main__":
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

    print("Using sample matrix {}".format(sample_matrix))
    s = matrix_to_scad(sample_matrix, 1)
    print(s)
