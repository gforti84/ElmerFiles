!-------------------------------------------------------------------------------
SUBROUTINE reluctaxfun(Model, n, X, Y)
    !-------------------------------------------------------------------------------
      USE DefUtils
      IMPLICIT NONE
      TYPE(Model_t) :: Model
      INTEGER :: n
      REAL(KIND=dp) :: X(*)
      REAL(KIND=dp), POINTER CONTIG :: Y(:,:)
    
      INTEGER :: i
      REAL(KIND=dp) :: B(3), Babs, HabsX, HabsY, HabsZ, nuX, nuY, nuZ
      REAL(KIND=dp) :: BabsX, BabsY, BabsZ
      REAL(KIND=dp), PARAMETER :: Saturation_Induction = 1.0d0
      REAL(KIND=dp), PARAMETER :: mu0 = PI * 4.0d-7
      REAL(KIND=dp), PARAMETER :: mu_r = 1.0d0
      ! TYPE(Variable_t), POINTER :: nuVar
      TYPE(ValueList_t), POINTER :: Material
      ! INTEGER :: el,j
      LOGICAL :: Visited = .FALSE.
      !-------------------------------------------------------------------------------
      
      SAVE Visited, Material
      
      IF(.NOT. Visited ) THEN
        ! We have introduced an ip-field where the reluctivity may be saved.
        ! This is an "exported variable" in the sif file. 
        ! nuVar => VariableGet( Model % Mesh % Variables,'nu')
        ! IF(.NOT. ASSOCIATED(nuVar) ) THEN
          ! CALL Fatal('relectfun','No variable "nu" exists!')
        ! END IF
        Material => GetMaterial()
        Visited = .TRUE.
      END IF
      
      ! Here the three first values of the input X are automatically set to be
      ! the components of the magnetic induction B.  
      ! B(1:3) = X(1:3)
      BabsX = MAX( ABS(X(1)), 1.0e-8 )  ! MAX( SQRT(X(1)**2), 1.0e-8 ) 
      BabsY = MAX( ABS(X(2)), 1.0e-8 )  ! MAX( SQRT(X(2)**2), 1.0e-8 ) 
      ! BabsZ = MAX( SQRT(X(3)**2), 1.0e-8 ) 
      ! Babs = MAX( SQRT(SUM(B**2)), 1.0e-8 ) 
    
      ! We cannot use the standard name "h-b curve" since it is taken.
      ! Renaming the keyword allows us to use this gimick. 
      HabsX = ListGetFun( Material,'my X h-b curve',BabsX )
      HabsY = ListGetFun( Material,'my Y h-b curve',BabsY )
      ! HabsZ = ListGetFun( Material,'my Z h-b curve',BabsZ )
      ! nuX = HabsX / BabsX
      ! nuY = HabsY / BabsY
      
      nuX = MIN( HabsX / BabsX, 1 / mu0 ) 
      nuY = MIN( HabsY / BabsY, 1 / mu0 ) 

      nuZ = 1 / mu0
    
      !PRINT *,'Babs', Babs, Habs, nu
      
      ! IF( n < 0 ) THEN
      !   el = Model % CurrentElement % ElementIndex
      !   j = NuVar % Perm(el) + ABS(n) 
      !   nuVar % Values(j) = nu    
      ! ELSE
      !   CALL Fatal('reluctafun','Expecting negative n for gauss point!')
      ! END IF
        
      ! X(4) would be the first input argument after the input B, and so on, 
      ! but in this example the additional fields are not used in the computation 
      ! of the reluctivity
      
      ! The values of the reluctivity tensor are finally returned via Y: 
      Y = 0.0_dp
      Y(1,1) = nuX
      Y(2,2) = nuY
      Y(3,3) = nuZ
    !-------------------------------------------------------------------------------
    END SUBROUTINE reluctaxfun
    !-------------------------------------------------------------------------------
    