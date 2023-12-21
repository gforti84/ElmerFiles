// Dimensions of the machine 
DefineConstant[ R_rot_in = { 20}]; 
DefineConstant[ R_rot_out = { 40}]; 
DefineConstant[ R_stat_out = { 96}]; 
DefineConstant[ Gap = { 0.6}]; 
DefineConstant[ b_d = { 21}]; 
DefineConstant[ hss_tot = { 32.4}]; 
DefineConstant[ bridge = { 0.6}]; 
DefineConstant[ w_PM = { 39}]; 
DefineConstant[ h_PM = { 4.9}]; 
DefineConstant[ h_wedge = { 3}]; 
// Mesh density points 
DefineConstant[ mesh_gap = { Gap/2}]; 
DefineConstant[ mesh_fine = { 0.5}]; 
DefineConstant[ mesh_normal = { 3}]; 
DefineConstant[ mesh_coarse = { 10}]; 
//================================================================= 
// Geometry definition 
Point(1) = {0, 0, 0, mesh_coarse}; 
// ========================================================== 
// =============== Stator Geometry =============================== 
// ========================================================== 
//Tooth bottom 
Point(2) = {Gap+R_rot_out, 0, 0, mesh_gap}; 
Rotate {{0, 0, 1}, {0, 0, 0}, Asin(b_d/2/(Gap+R_rot_out))} { 
 Duplicata { Point{2}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, -Asin(b_d/2/(Gap+R_rot_out))} { 
 Duplicata { Point{2}; } 
} 
//Tooth top 
Point(5) = {Gap+R_rot_out+hss_tot, 0, 0, mesh_normal}; 
Rotate {{0, 0, 1}, {0, 0, 0}, Asin(b_d/2/(Gap+R_rot_out+hss_tot))} { 
 Duplicata { Point{5}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, -Asin(b_d/2/(Gap+R_rot_out+hss_tot))} { 
 Duplicata { Point{5}; } 
} 
Point(8) = {Gap+R_rot_out+h_wedge, 0, 0, mesh_normal}; 
Rotate {{0, 0, 1}, {0, 0, 0}, Asin(b_d/2/(Gap+R_rot_out+h_wedge))} { 
 Duplicata { Point{8}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, -Asin(b_d/2/(Gap+R_rot_out+h_wedge))} { 
 Duplicata { Point{8}; } 
} 
//Sector edges 
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} { 
 Duplicata { Point{2, 5, 8}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, -Pi/6} { 
 Duplicata { Point{2, 5, 8}; } 
} 
Line(1) = {12, 13}; 
Line(2) = {13, 11}; 
Line(3) = {6, 9}; 
Line(4) = {9, 3}; 
Line(5) = {7, 10}; 
Line(6) = {10, 4}; 
Line(7) = {15, 16}; 
Line(8) = {16, 14}; 
Circle(9) = {15, 1, 7}; 
Circle(10) = {16, 1, 10}; 
Circle(11) = {14, 1, 4}; 
Circle(12) = {4, 1, 2}; 
Circle(13) = {2, 1, 3}; 
Circle(14) = {3, 1, 11}; 
Circle(15) = {9, 1, 13}; 
Circle(16) = {6, 1, 12}; 
//Finalize stator yoke segment 
Point(17) = {R_stat_out, 0, 0, mesh_coarse}; 
Rotate {{0, 0, 1}, {0, 0, 0}, -Pi/6} { 
 Duplicata { Point{17}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/6} { 
 Duplicata { Point{17}; } 
} 
Line(17) = {19, 12}; 
Line(18) = {18, 15}; 
Circle(19) = {18, 1, 17}; 
Circle(20) = {17, 1, 19}; 
//Define plane surface for the steel segment 
Line Loop(21) = {19, 20, 17, -16, 3, 4, -13, -12, -6, -5, -9, -18}; 
Plane Surface(22) = {21}; 
//Define plane surfaces of the coil (plus and minus of the phase coil) and wedges 
Line Loop(23) = {16, 1, -15, -3}; 
Plane Surface(24) = {23}; 
Line Loop(25) = {5, -10, -7, 9}; 
Plane Surface(26) = {25}; 
Line Loop(27) = {15, 2, -14, -4}; 
Plane Surface(28) = {27}; 
Line Loop(29) = {10, 6, -11, -8}; 
Plane Surface(30) = {29}; 
//Duplicate stator sectors 
For it In {1:5} 
Rotate {{0, 0, 1}, {0, 0, 0}, it*Pi/3} { 
 Duplicata { Surface{22, 24, 28, 30, 26}; } 
} 
EndFor 
// ========================================================== 
// =============== Rotor geometry =============================== 
// ========================================================== 
Point(379) = {R_rot_in, 0, 0, mesh_coarse}; 
Point(380) = {R_rot_out, 0, 0, mesh_gap}; 
//Rotor sector borders 
Rotate {{0, 0, 1}, {0, 0, 0}, Pi/4} { 
 Duplicata { Point{379, 380}; } 
} 
Rotate {{0, 0, 1}, {0, 0, 0}, -Pi/4} { 
 Duplicata { Point{379, 380}; } 
} 
Line(176) = {382, 381}; 
Line(177) = {383, 384}; 
Circle(178) = {383, 1, 379}; 
Circle(179) = {379, 1, 381}; 
Circle(180) = {384, 1, 380}; 
Circle(181) = {380, 1, 382}; 
//Magnet points 
Point(385) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge))), 0, 0, mesh_normal}; 
Point(386) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge))), w_PM/2, 0, mesh_gap}; 
Point(387) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge))), -w_PM/2, 0, mesh_gap}; 
Point(388) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge)))-h_PM, 0, 0, mesh_normal}; 
Point(389) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge)))-h_PM, w_PM/2, 0, 
mesh_normal}; 
Point(390) = {(R_rot_out-bridge)*Cos(Asin(w_PM/2/(R_rot_out-bridge)))-h_PM, -w_PM/2, 0, 
mesh_normal}; 
//PM edges 
Line(182) = {389, 386}; 
Line(183) = {386, 385}; 
Line(184) = {385, 387}; 
Line(185) = {387, 390}; 
Line(186) = {390, 388}; 
Line(187) = {388, 389}; 
//PM surface 
Line Loop(188) = {184, 185, 186, 187, 182, 183}; 
Plane Surface(189) = {188}; 
//Pole sector iron 
Line Loop(190) = {181, 176, -179, -178, 177, 180}; 
Plane Surface(191) = {190, 188}; 
//Duplicate rotor poles 
For it In {1:3} 
Rotate {{0, 0, 1}, {0, 0, 0}, it*Pi/2} { 
 Duplicata { Surface{191, 189}; } 
} 
EndFor 
//shaft plane surface 
Line Loop(234) = {196, -179, -178, 223, 224, 209, 210, 195}; 
Plane Surface(235) = {234}; 
// ========================================================== 
// =============== Air gap =============================== 
// ========================================================== 
//sliding surface 
Point(529) = {Gap/2+R_rot_out, 0, 0, mesh_gap}; 
Point(530) = {0, Gap/2+R_rot_out, 0, mesh_gap}; 
Point(531) = {0, -Gap/2-R_rot_out, 0, mesh_gap}; 
Point(532) = {-Gap/2-R_rot_out, 0, 0, mesh_gap}; 
Circle(236) = {529, 1, 530}; 
Circle(237) = {530, 1, 532}; 
Circle(238) = {532, 1, 531}; 
Circle(239) = {531, 1, 529}; 
//create air gap part of the stator 
Line Loop(240) = {13, 14, -57, -39, -38, -52, -86, -68, -67, -81, -115, -97, -96, -110, -144, 
-126, -125, -139, -173, -155, -154, -168, 11, 12}; 
Line Loop(241) = {239, 236, 237, 238}; 
Plane Surface(242) = {240, 241}; 
//create air gap part of the rotor 
Line Loop(243) = {181, 198, 193, 212, 207, 226, 221, 180}; 
Plane Surface(244) = {241, 243}; 
// ========================================================== 
// =============== Bodies =============================== 
// ========================================================== 
// u+- 
Physical Surface(1) = {88, 175}; 
Physical Surface(2) = {73, 160}; 
// v+- 
Physical Surface(3) = {26, 117}; 
Physical Surface(4) = {24, 102}; 
// w+- 
Physical Surface(5) = {59, 146}; 
Physical Surface(6) = {44, 131}; 
//Stator iron 
Physical Surface(7) = {60, 31, 22, 147, 118, 89}; 
//Rotor iron 
Physical Surface(8) = {206, 192, 191, 220}; 
//Wedges 
Physical Surface(9) = {28, 54, 49, 83, 78, 112, 107, 141, 136, 170, 165, 30}; 
//shaft 
Physical Surface(10) = {235}; 
//PMs 
Physical Surface(11) = {189}; 
Physical Surface(12) = {205}; 
Physical Surface(13) = {219}; 
Physical Surface(14) = {233}; 
//stator air gap 
Physical Surface(15) = {242}; 
//rotor air gap 
Physical Surface(16) = {244}; 
// ========================================================== 
// =============== Boundaries =============================== 
// ========================================================== 
//outer boundary 
Physical Line(1) = {32, 33, 61, 62, 90, 91, 119, 120, 148, 149, 19, 20}; 
//sliding boundary 
Physical Line(2) = {239, 236, 237, 238};
