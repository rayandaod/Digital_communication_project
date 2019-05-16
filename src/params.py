import numpy as np

# General variables
verbose = True
message_file_path = "../data/input_text.txt"
output_file_path = "../data/output_text.txt"
message_sample_path = "../data/input_samples.txt"
output_sample_path = "../data/output_samples.txt"
server_hostname = "iscsrv72.epfl.ch"
server_port = 80

# /!\ DO NOT CHANGE THE FOLLOWING VARIABLES /!\
NOISE_VAR = 0.05  # channel noise variance
Fs = 22050  # sampling frequency / sampling rate / samples per second (in Hz)
ABS_SAMPLE_INTERVAL = 1  # samples amplitude must be between -1 and 1
MIN_FREQ = 1000
MAX_FREQ = 9000
PREAMBLE = [-1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1,  # preamble sequence
            -1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1,
            1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 1,
            -1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1,
            1, -1, 1, -1, -1, -1, -1, -1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1,
            -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1,
            1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1]
# /!\ -------------------------------------- /!\

# Communication parameters (you should only tweak the first 5 ones for this project)
M = 16  # length of the mapping (must be of the form 2^2k if QAM is chosen)
MOD_TYPE = "qam"  # modulation type: qam or psk or pam for now
BITS_PER_SYMBOL = int(np.log2(M))  # number of bits we transmit per symbol
BETA = 0.5  # rolloff factor of our root-raised-cosine pulse
T = 0.0005  # symbol period (in seconds), i.e time before we can repeat the pulse while satisfying Nyquist criterion
USF = int(np.ceil(T * Fs))  # up-sampling factor, i.e the number of zeros to add between
# any 2 samples before pulse shaping
SPAN = 8 * USF  # size of our pulse in number of samples

# mapping = mapping/np.sqrt(np.mean(np.abs(mapping)**2))

# TODO check that the length of the pn-sequence is optimal
# TODO How to choose SPAN?
