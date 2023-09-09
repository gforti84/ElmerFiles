Test case for linear systems.  
  
This folder has different test cases for a simplest case of magnetic flux distribution in a simplified transformer core.  
  
The core is defined only at one joint, leg and yoke. Magnetic flux is driven by a boundary condition. There is a dummy surface, or volume, but it is there only for numerical purpose. The relative permeability is low enough to avoid magnetic flux.  

![image](Figures/mesh_bodies.png)
  
The meshes are created using gmsh python and there are some refinement parameters:   
  
# === Input Parameters ===  
# -> Mesh Control <-  
  
mesh_all = 15            # Overall mesh size  
mesh_core = 15/2         # Overall mesh core size  
mesh_inner_surf = 15/4   # Mesh size for inner surface (adjacent to 'none' region)  
mesh_joint = 15/4        # Mesh size for joint surface (between leg and yoke)  
  
![image](Figures/mesh_inner.png)  
![image](Figures/mesh_joint.png)  
  
The cases were compared with FEMM simulation.
  
2D base:  
![image](Figures/case_2d.png)   
![image](Figures/femm.png)   
  
2D anisotropic linear:  
![image](Figures/case_2d_aniso.png)   
![image](Figures/femm_aniso.png)    
  
2D isotropic non-linear:  
![image](Figures/case_2d_nl.png)   
![image](Figures/femm_nl.png)   
  
3D base:  
![image](Figures/case_3d.png)   
![image](Figures/case_3d_lines.png)  
   
3D anisotropic linear (z-axis mu_r=10000):  
![image](Figures/case_3d_aniso.png)   
![image](Figures/case_3d_aniso_lines.png)  

Now the problems. For 3D anisotropic linear, if the z-axis permeability is defined with lower values, 
the results diverges significantly.  
  
3D anisotropic linear (z-axis mu_r=1):  
![image](Figures/case_3d_aniso_urz1.png)   
![image](Figures/case_3d_aniso_urz1_lines.png)  

Also, for 3D non-linear cases, the non-linear solver did not converge, either isotropic or anisotrpic.



  
  




