
def simpleSampling(r, nTries):
    """simple sampling estimator

    Implements simple-sampling Monte Carlo (MC) 
    strategy to estimate pi

    Args: 
        r (object) pseudo random number generator
        nTries (int) number of trial points

    Returns:
        pi (float) simple sampling estimate of pi
    """
    nSucc = 0
    for n in xrange(nTries):
        x, y = r(), r()
        if (x*x + y*y <= 1):
            nSucc += 1
    return 4*float(nSucc)/nTries

