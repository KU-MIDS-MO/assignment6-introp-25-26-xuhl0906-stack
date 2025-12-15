def random_unit_vectors(num_vectors, dim):
    import numpy as np
    M = np.random.randn(num_vectors, dim)
    norms = np.linalg.norm(M, ord=2, axis=1)
    norms[norms == 0] = 1
    M_normalized = M / norms[:, np.newaxis]
    return M_normalized
