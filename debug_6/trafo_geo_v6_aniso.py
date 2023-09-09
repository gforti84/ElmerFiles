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

gmsh.model.add('t6_a')

# Testar depois usando o OpenCASCADE
# creating the cubes:


mps = 0 # mesh point size

gmsh.model.occ.addPoint(0, 0, 0, meshSize=mps, tag=1)
gmsh.model.occ.addPoint(100, 0, 0, meshSize=mps, tag=2)
gmsh.model.occ.addPoint(100, 100, 0, meshSize=mps, tag=3)
gmsh.model.occ.addPoint(200, 100, 0, meshSize=mps, tag=4)
gmsh.model.occ.addPoint(200, 200, 0, meshSize=mps, tag=5)
gmsh.model.occ.addPoint(0, 200, 0, meshSize=mps, tag=6)
gmsh.model.occ.addPoint(200, 0, 0, meshSize=mps, tag=7)

# z = 0 surfaces
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

gmsh.model.occ.addPlaneSurface([c1y], 101)
gmsh.model.occ.addPlaneSurface([c1x], 102)
gmsh.model.occ.addPlaneSurface([c2], 103)


gmsh.model.occ.addPoint(0, 0, 100, meshSize=mps, tag=11)
gmsh.model.occ.addPoint(100, 0, 100, meshSize=mps, tag=12)
gmsh.model.occ.addPoint(100, 100, 100, meshSize=mps, tag=13)
gmsh.model.occ.addPoint(200, 100, 100, meshSize=mps, tag=14)
gmsh.model.occ.addPoint(200, 200, 100, meshSize=mps, tag=15)
gmsh.model.occ.addPoint(0, 200, 100, meshSize=mps, tag=16)
gmsh.model.occ.addPoint(200, 0, 100, meshSize=mps, tag=17)

# z = 0 surfaces
l11 = gmsh.model.occ.addLine(11, 12)
l12 = gmsh.model.occ.addLine(12, 13) # -> also in none
l13 = gmsh.model.occ.addLine(13, 14) # -> also in none
l14 = gmsh.model.occ.addLine(14, 15)
l15 = gmsh.model.occ.addLine(15, 16)
l16 = gmsh.model.occ.addLine(16, 11)

l17 = gmsh.model.occ.addLine(12, 17)
l18 = gmsh.model.occ.addLine(17, 14)

l19 = gmsh.model.occ.addLine(13, 16)

c11y = gmsh.model.occ.addCurveLoop([l11, l12, l19, l16]) # the points must be ordered
c11x = gmsh.model.occ.addCurveLoop([l13, l14, l15, -l19]) # the points must be ordered
c12 = gmsh.model.occ.addCurveLoop([l17, l18, -l13, -l12]) # the points must be ordered

gmsh.model.occ.addPlaneSurface([c11y], 111)
gmsh.model.occ.addPlaneSurface([c11x], 112)
gmsh.model.occ.addPlaneSurface([c12], 113)

l111 = gmsh.model.occ.addLine(1, 11)
l112 = gmsh.model.occ.addLine(2, 12) # -> also in none
l113 = gmsh.model.occ.addLine(3, 13) # -> also in none
l114 = gmsh.model.occ.addLine(4, 14)
l115 = gmsh.model.occ.addLine(5, 15)
l116 = gmsh.model.occ.addLine(6, 16)
l117 = gmsh.model.occ.addLine(7, 17)

c111 = gmsh.model.occ.addCurveLoop([l111, l11, -l112, -l1]) # the points must be ordered
c112 = gmsh.model.occ.addCurveLoop([l112, l12, -l113, -l2]) # the points must be ordered
c113 = gmsh.model.occ.addCurveLoop([l113, l13, -l114, -l3]) # the points must be ordered
c114 = gmsh.model.occ.addCurveLoop([l114, l14, -l115, -l4]) # the points must be ordered
c115 = gmsh.model.occ.addCurveLoop([l115, l15, -l116, -l5]) # the points must be ordered
c116 = gmsh.model.occ.addCurveLoop([l116, l16, -l111, -l6]) # the points must be ordered

c117 = gmsh.model.occ.addCurveLoop([l112, l17, -l117, -l7]) # the points must be ordered
c118 = gmsh.model.occ.addCurveLoop([l117, l18, -l114, -l8]) # the points must be ordered

c_a = gmsh.model.occ.addCurveLoop([l113, l19, -l116, -l9]) # the points must be ordered

gmsh.model.occ.addPlaneSurface([c111], 201)
gmsh.model.occ.addPlaneSurface([c112], 202)
gmsh.model.occ.addPlaneSurface([c113], 203)
gmsh.model.occ.addPlaneSurface([c114], 204)
gmsh.model.occ.addPlaneSurface([c115], 205)
gmsh.model.occ.addPlaneSurface([c116], 206)

gmsh.model.occ.addPlaneSurface([c117], 207)
gmsh.model.occ.addPlaneSurface([c118], 208)

gmsh.model.occ.addPlaneSurface([c_a], 209)

# gmsh.model.occ.addSurfaceLoop([])

gmsh.model.occ.addSurfaceLoop([101, 111, 201, 202, 209, 206], 301)
gmsh.model.occ.addSurfaceLoop([102, 112, 203, 204, 205, 209], 302)
gmsh.model.occ.addSurfaceLoop([103, 113, 202, 203, 207, 208], 303)

gmsh.model.occ.addVolume([301], 311)
gmsh.model.occ.addVolume([302], 312)
gmsh.model.occ.addVolume([303], 313)

gmsh.model.occ.synchronize()

gmsh.model.addPhysicalGroup(3,[311],1,'core_dl_y') # Physical groups tags are unique per dimension
gmsh.model.addPhysicalGroup(3,[312],2,'core_dl_x') # Physical groups tags are unique per dimension
gmsh.model.addPhysicalGroup(3,[313],3,'none') # Physical groups tags are unique per dimension

gmsh.model.addPhysicalGroup(2,[201],1,'BC1') # Starting from the bottom and increasing counterclockwise
gmsh.model.addPhysicalGroup(2,[207],2,'BC2')
gmsh.model.addPhysicalGroup(2,[208],3,'BC3')
gmsh.model.addPhysicalGroup(2,[204],4,'BC4')
gmsh.model.addPhysicalGroup(2,[205],5,'BC5')
gmsh.model.addPhysicalGroup(2,[206],6,'BC6')

# gmsh.model.addPhysicalGroup(2,[207],7,'BC7')
# gmsh.model.addPhysicalGroup(2,[208],8,'BC8')

gmsh.model.addPhysicalGroup(2,[101, 111],7,'BC7')
gmsh.model.addPhysicalGroup(2,[102, 112],8,'BC8')
gmsh.model.addPhysicalGroup(2,[103, 113],9,'BC9')


gmsh.model.occ.synchronize()

# lc = 15

gmsh.model.mesh.setSize(gmsh.model.getEntities(0),mesh_all)

core_list = []
core_list.append(gmsh.model.getEntitiesForPhysicalGroup(3,1)[0])
core_list.append(gmsh.model.getEntitiesForPhysicalGroup(3,2)[0])

gmsh.model.mesh.field.add('Constant',1)
gmsh.model.mesh.field.setNumbers(1,'VolumesList',core_list)
gmsh.model.mesh.field.setNumber(1, "VIn", mesh_core)

# print(gmsh.model.getEntitiesForPhysicalGroup(3,1))

gmsh.model.mesh.field.add('Constant',2)
gmsh.model.mesh.field.setNumbers(2,'SurfacesList',[202, 203])
gmsh.model.mesh.field.setNumber(2, "VIn", mesh_inner_surf)

gmsh.model.mesh.field.add('Constant',3)
gmsh.model.mesh.field.setNumbers(3,'SurfacesList',[209])
gmsh.model.mesh.field.setNumber(3, "VIn", mesh_joint)

gmsh.model.mesh.field.add("Min", 4)
gmsh.model.mesh.field.setNumbers(4, "FieldsList", [1, 2, 3])

gmsh.model.mesh.field.setAsBackgroundMesh(4)

gmsh.model.mesh.generate(3)

gmsh.write('t6_a.geo_unrolled')

# # # # # # # Usando o formato *.msh melhora ao reter as definições dos Physical Groups. Os nomes ficam no 
# # # # # # #   arquivo entities.sif. 
gmsh.write('t6_a.msh')

# os.system('gmsh t6_a.geo_unrolled')
# os.system('gmsh t6_a.msh')

os.system('ElmerGrid 14 2 t6_a.msh -autoclean')
os.system('ElmerGrid 2 2 ./t6_a -autoclean -partdual -metiskway 4')

# os.system('ElmerSolver case_ef_3d.sif')
os.system('ElmerSolver case_ef_3d_aniso.sif')
# os.system('ElmerSolver case_ef_3d_NL.sif')
# os.system('ElmerSolver case_ef_3d_anNL.sif')

# os.system('mpirun -np 4 ElmerSolver_mpi case_ef_3d.sif ')

# os.system('ElmerGUI')

gmsh.finalize()
