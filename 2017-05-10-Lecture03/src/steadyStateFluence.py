import numpy as np

def LM0FreqDomain((mua,mus,g),N,k):
        """lowest order Legendre moment in frequency domain

        Computes Legendre moment of order zero in frequency domain for given
        wavenumber by solving symmetric tridiagonal system, i.e. Eq. (10),
        derived by Ref. [1]

        Args:
            mua (float): absorption coefficient
            mus (float): scattering coefficient
            g (float): scattering anisotropy
            N (int): highest order used in Legendre expansion of radiance
            k (float): wavenumber

        Notes:
            Similar to the discussion in [1] we use Cramer's rule to obtain 
            the lowest order Legendre moment.

        Refs:
            [1] Analytical solution of the radiative transfer equation for 
                infinite-space fluence
                Liemert, A. and Kienle, A.
                Phys. Rev. A, 83 (2011) 015804
        """
        nn = np.arange(N)

        # ABSORPTION COEFFICIENTS OF ORDER N, SEE EQ. (5), REF. [1]
        muan = lambda n: mua + (1.-g**n)*mus

        # RIGHT HAND SIDE OF SYSTEM OF LINEAR EQUATIONS DERIVED IN WAVENUMBER
        # DOMAIN, SEE EQ. (8) OF REF. [1] 
        delta = [1] + [0]*(N-1) 

        # SYMMETRIC TRIDIAGONAL MATRIX FOR SYSTEM OF LINEAR EQUATION DERIVED
        # IN WAVENUMBER DOMAIN, SEE EQS. (8-10) OF REF. [1]
        T = np.diag(1j*nn[1:]*k, 1) + \
             np.diag(1j*nn[1:]*k,-1) + \
             np.diag((2*nn+1)*muan(nn))

        # COMPUTE DETERMINANTS NEEDED TO OBTAIN LOWEST LEGENDRE MOMENT VIA
        # CRAMERS RULE, SEE EQ. (11) OF REF. [1]
        detT =np.linalg.det(T)
        T[:,0] = delta 
        detT0 =np.linalg.det(T)

        return detT0/detT


def LM0ReprFreqDom((mua,mus,g),N,k):
        """full representation of Legendre moment in frequency domain

        Computes full representation of Legendre moment of order zero in
        frequency domain by repeatedly solving symmetric tridiagonal system,
        i.e. Eq.  (10), derived by Ref. [1]

        Args:
            mua (float): absorption coefficient
            mus (float): scattering coefficient
            g (float): scattering anisotropy
            N (int): highest order used in Legendre expansion of radiance
            k (numpy array, ndim=1): sequence of wavenumbers

        Refs:
            [1] Analytical solution of the radiative transfer equation for 
                infinite-space fluence
                Liemert, A. and Kienle, A.
                Phys. Rev. A, 83 (2011) 015804
        """
        return [(ki,LM0FreqDomain((mua,mus,g),N,ki)) for ki in k]


def LM0Repr(LM0FDR,x,dk):
        return [(1./2/np.pi)*np.sum([LM0k*np.exp(1j*k*xi)*dk 
                   for (k,LM0k) in LM0FDR]).real for xi in x ]

def fluence(x,LM0):
        return -np.gradient(LM0)/2/np.pi/x/(x[1]-x[0])

