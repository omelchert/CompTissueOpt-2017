0. General

CompTissueOpt-2017: Supplementary material for the lecture focus on "Tissue 
Optics - Monte Carlo Modeling of light transport in turbid media", held as
part of the lecture on "Computational Photonics" at Leibniz University 
Hannover during Summer term 2017

1. Content:

L1 - 2017-04-26: Random Variables
  1.1 - Distribution of random variables
  1.2 - Basic summary measures
  1.3 - Pseudo random number generators 
      1.3.1 - True random numbers
      1.3.2 - Pseudo random numbers
      1.3.3 - Types of PRNGs
      1.3.4 - Quality control - A simple PRNG test
      1.3.5 - Elaborate test suites
  1.4 - Sampling strategies
      1.4.1 - Uniform sampling from surface of unit 3-sphere
      1.4.2 - Sampling from Henyey-Greenstein phase function

L2 - 2017-05-03: Monte Carlo (MC) Basics  
  2.1 - The Monte Carlo method 
  2.2 - Paradigmatic MC simulations
      2.2.1 - Estimating pi (acceptance-rejection method)
      2.2.2 - The 1D random walk
            2.2.2.1 - Simulation of discrete symmetric 1D rando walks
            2.2.2.2 - Endpoint distribution
            2.2.2.3 - The 1D RW as  limiting case
      2.2.3 - The 3D random walk
            2.2.3.1 - The "isotropic" 3D RW - easy special case
            2.2.3.2 - The "non-isotropic" 3D RW - tricky general case

L3 - 2017-05-10: Light transport in turbid media 
  3.1 - The radiative transfer equation (TE) 
      3.1.1 - Limiting case I: unscattered transmission
      3.1.2 - Limiting case II: diffusion approximation
  3.2 - MC modeling of photon propagation 
      3.2.1 - Photon packet propagation
      3.2.2 - Scattering events
      3.2.3 - Photon termination
      3.2.4 - Interaction with tissue - monitoring observables
      3.2.5 - Irradiation source profiles
      3.2.6 - Performing a simulation
  3.3 - Validation testing 
      3.3.1 - Comparison to diffusion approximation
      3.3.2 - Semi-analytic solution for anisotropic scattering

L4 - 2017-05-17:  Light transport in turbid media II 
  4.1 - Implicit assumptions of the RTE 
  4.2 - The statistical minutiae of photon trails
  4.3 - Modeling the irradiation source
      4.3.1 - Simple beam
      4.3.2 - Realistic source fiber
  4.4 - Measuring the volumetric energy density
  4.5 - Exemplary use-case: Murine liver



2. DEPENDENCIES

CompTissueOpt-2017 requires the functionality of NumPy, a fundamental package 
for scientific computing (see www.numpy.org).

3. LICENSE

None, yet

4. ACKNOWLEDGEMENTS

O. Melchert acknowledges support from the VolkswagenStiftung within the
Nieders\"achsisches Vorab program in the framework of the project Hybrid
Numerical Optics
