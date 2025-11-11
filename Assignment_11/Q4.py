import numpy as np

def polyfit_matrix(x, y, m):
    """
    Polynomial least squares fitting using normal equations.
    
    Parameters:
        x : array-like, input x data
        y : array-like, input y data
        m : int, degree of polynomial
        
    Returns:
        coeffs : numpy array of coefficients [a0, a1, ..., am]
        std_dev : standard deviation of residuals
    """
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)

    # Construct A and b as per given formulas
    A = np.zeros((m+1, m+1))
    b = np.zeros(m+1)

    for k in range(m+1):
        for j in range(m+1):
            A[k, j] = np.sum(x**(k+j))
        b[k] = np.sum(y * x**k)

    # Solve for coefficients
    coeffs = np.linalg.solve(A, b)

    # Compute fitted values and residuals
    y_fit = sum(coeffs[j] * x**j for j in range(m+1))
    residuals = y - y_fit

    # Sum of squares and standard deviation
    SSR = np.sum(residuals**2)
    std_dev = np.sqrt(SSR / (n - (m + 1)))

    return coeffs, std_dev


# Example usage (test)
if __name__ == "__main__":
    # demo/test section
    print("Testing polynomial fitting...")
