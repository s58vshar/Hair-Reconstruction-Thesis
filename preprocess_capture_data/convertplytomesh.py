import open3d as o3d
import numpy as np

pcd = o3d.io.read_point_cloud("/home/sharma/MonoHair/strand_integration/result/merged_ply/si/ct2wings_restructured.ply")  # Replace with your file path

pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.00005, max_nn=30))

mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8)

o3d.io.write_triangle_mesh("hair_mesh.obj", mesh) 

vertices = np.asarray(mesh.vertices)
mesh = mesh.select_by_index(np.where(densities > np.quantile(densities, 0.15))[0])

pcd_mesh = o3d.geometry.PointCloud()
pcd_mesh.points = mesh.vertices
pcd_mesh.normals = mesh.vertex_normals  # Normals for the mesh vertices

#o3d.visualization.draw_geometries([pcd_mesh], point_show_normal=False)
o3d.visualization.draw_geometries([mesh], point_show_normal = False)
