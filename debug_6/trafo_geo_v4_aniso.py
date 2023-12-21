import gmsh
import sys
import os


# === Input Parameters ===
# -> Mesh Control <-

mesh_all = 15         # Overall mesh size
mesh_core = 15/2         # Overall mesh core size
mesh_inner_surf = 15/4   # Mesh size for inner surface (adjacent to 'none' region)
mesh_joint = 15/4        # Mesh size for joint surface (between leg and yoke)


gmsh.initialize()

gmsh.option.setNumber('Geometry.OCCBooleanPreserveNumbering',True)

gmsh.model.add('t4_a')

# Testar depois usando o OpenCASCADE
# creating the cubes:

# lc = 1

mps = 0 # mesh point size

gmsh.model.occ.addPoint(0, 0, 0, meshSize=mps, tag=1)
gmsh.model.occ.addPoint(100, 0, 0, meshSize=mps, tag=2)
gmsh.model.occ.addPoint(100, 100, 0, meshSize=mps, tag=3)
gmsh.model.occ.addPoint(200, 100, 0, meshSize=mps, tag=4)
gmsh.model.occ.addPoint(200, 200, 0, meshSize=mps, tag=5)
gmsh.model.occ.addPoint(0, 200, 0, meshSize=mps, tag=6)

gmsh.model.occ.addPoint(200, 0, 0, meshSize=mps, tag=7)

l1 = gmsh.model.occ.addLine(1, 2)
l2 = gmsh.model.occ.addLine(2, 3) # -> also in none
l3 = gmsh.model.occ.addLine(3, 4) # -> also in none
l4 = gmsh.model.occ.addLine(4, 5)
l5 = gmsh.model.occ.addLine(5, 6)
l6 = gmsh.model.occ.addLine(6, 1)

l7 = gmsh.model.occ.addLine(2, 7)
l8 = gmsh.model.occ.addLine(7, 4)

l9 = gmsh.model.occ.addLine(3, 6)

c1y = gmsh.model.occ.addCurveLoop([l1, l2, l9, l6]) # the points must be ordered
c1x = gmsh.model.occ.addCurveLoop([l3, l4, l5, -l9]) # the points must be ordered
c2 = gmsh.model.occ.addCurveLoop([l7, l8, -l3, -l2]) # the points must be ordered

s1y = gmsh.model.occ.addPlaneSurface([c1y])
s1x = gmsh.model.occ.addPlaneSurface([c1x])
s2 = gmsh.model.occ.addPlaneSurface([c2])

gmsh.model.occ.synchronize()

gmsh.model.addPhysicalGroup(2,[s1y],1,'core_DL_Y') # Physical groups tags are unique per dimension
gmsh.model.addPhysicalGroup(2,[s1x],2,'core_DL_X') # Physical groups tags are unique per dimension
gmsh.model.addPhysicalGroup(2,[s2],3,'none') # Physical groups tags are unique per dimension

gmsh.model.addPhysicalGroup(1,[l1],1,'BC1') # Starting from the bottom and increasing counterclockwise
gmsh.model.addPhysicalGroup(1,[l7],2,'BC2')
gmsh.model.addPhysicalGroup(1,[l8],3,'BC3')
gmsh.model.addPhysicalGroup(1,[l4],4,'BC4')
gmsh.model.addPhysicalGroup(1,[l5],5,'BC5')
gmsh.model.addPhysicalGroup(1,[l6],6,'BC6')

gmsh.model.occ.synchronize()

# lc = 15

gmsh.model.mesh.setSize(gmsh.model.getEntities(0),mesh_all)

core_list = []
core_list.append(gmsh.model.getEntitiesForPhysicalGroup(2,1)[0])
core_list.append(gmsh.model.getEntitiesForPhysicalGroup(2,2)[0])

gmsh.model.mesh.field.add('Constant',1)
gmsh.model.mesh.field.setNumbers(1,'SurfacesList',core_list)
gmsh.model.mesh.field.setNumber(1, "VIn", mesh_core)

gmsh.model.mesh.field.add('Constant',2)
gmsh.model.mesh.field.setNumbers(2,'CurvesList',[l2, l3])
gmsh.model.mesh.field.setNumber(2, "VIn", mesh_inner_surf)

gmsh.model.mesh.field.add('Constant',3)
gmsh.model.mesh.field.setNumbers(3,'CurvesList',[l9])
gmsh.model.mesh.field.setNumber(3, "VIn", mesh_joint)

gmsh.model.mesh.field.add("Min", 4)
gmsh.model.mesh.field.setNumbers(4, "FieldsList", [1, 2, 3])

gmsh.model.mesh.field.setAsBackgroundMesh(4)


gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(2)

# gmsh.write('t4_a.geo_unrolled')

# # # # # # Usando o formato *.msh melhora ao reter as definições dos Physical Groups. Os nomes ficam no 
# # # # # #   arquivo entities.sif. 
gmsh.write('t4_a.msh')

# os.system('gmsh t4_a.msh')

os.system('ElmerGrid 14 2 t4_a.msh -autoclean')
os.system('ElmerSolver case_ef.sif')
# os.system('ElmerSolver case_ef_aniso.sif')
# os.system('ElmerSolver case_ef_NL.sif')

gmsh.finalize()
