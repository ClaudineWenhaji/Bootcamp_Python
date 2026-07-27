def simple_predict(x, theta):
    """Computes the vector of prediction y_hat from two non-empty numpy.ndarray.
        y(i) = θ0 + θ1x(i) for i = 1, ..., m
    Args:
        x: has to be an numpy.ndarray, a one-dimensional array of size m.
        theta: has to be an numpy.ndarray, a one-dimensional array of size 2.
    Returns:
        y_hat as a numpy.ndarray, a one-dimensional array of size m.
        None if x or theta are empty numpy.ndarray.
        None if x or theta dimensions are not appropriate.
    Raises:
        This function should not raise any Exception.
    """

    y_hat = []

    theta0 = theta[0]
    theta1 = theta[1]

    for xi in x:
        y_hat.append(theta0 + theta1 * xi)
    return y_hat
