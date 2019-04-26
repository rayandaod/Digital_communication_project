import numpy as np


# Returns a M-QAM constellation
def qam_map(M):
    """
    :param M: the size of our mapping, i.e the number of symbols we can send
    :return: the array of symbols of the M-QAM (Quadrature Amplitude Modulation)
    """
    log_sqrt_m = np.log2(np.sqrt(M))
    if log_sqrt_m != np.ceil(log_sqrt_m):
        raise ValueError('Parameter[M] is not of the form 2^2K, K a positive integer.')
    N = np.sqrt(M) - 1
    aux = np.arange(-N, N+1, 2)
    x, y = np.meshgrid(aux, aux[::-1])
    return (x + 1j*y).T.flatten()


# Returns a M-PSK constellation
def psk_map(M):
    """
        :param M: the size of our mapping, i.e the number of symbols we can send
        :return: the array of symbols of the M-PSK (Pulse Shift Keying)
        """
    return np.exp(1j*2*np.pi*np.arange(0, M)/M)

# TODO make qam_map output in the trigonometric order, starting with 1+j
