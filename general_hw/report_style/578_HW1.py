import numpy as np
from scipy import constants as sc
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(
    context="paper",
    style="ticks",
    palette="deep",
    font="serif",
    font_scale=1,
    color_codes=True,
    rc=None,
)
sns.despine()


def f1(x):
    """
    Function returns the pulse function PERIODICALLY
    :param x: input value
    :return:
    """
    while x < -1:
        x += 2
    if -0.5 <= x <= 0.5:
        return 1
    else:
        return 0


def f2(x):
    return np.sin(2 * sc.pi * x)


def calc_u_exact(f, x, t):
    """
    Returns the exact value of the PDE solution at x,t
    :param f: forcing function
    :param x: location
    :param t: time
    :return:
    """
    return f(x - t)


def FTBS_one_step(Lambda, v0, v1):
    vnp1 = (1 - Lambda) * v1 + Lambda * v0
    return vnp1


def LaxF_one_step(Lambda, v0, v2):
    vnp1 = 1 / 2 * (1 - Lambda) * v2 + 1 / 2 * (1 + Lambda) * v0
    return vnp1


def LeapFrog_one_step(Lambda, v0, vnm1, v2):
    """

    :param Lambda: Lambda
    :param v0: v_(i-1)
    :param vnm1: v_i at previous time step
    :param v2: v_(i+1)
    :return: one step of Leap Frog
    """
    vnp1 = vnm1 - Lambda * v2 + Lambda * v0
    return vnp1


def L2norm(e, h):
    """
    Take the discrete L2 norm of e. Function uses Trapezoid method.
    :param e: error array
    :param h: grid size
    :return:
    """
    # ensure e has a compatible shape for taking a dot-product
    e = e.reshape(-1, )

    # Task:
    # Return the L2-norm, i.e., the square root of the integral of e^2
    # Assume a uniform grid in x and y, and apply the midpoint rule.
    # Assume that each grid point represents the midpoint of an equally sized region

    l2_norm_squared = np.sum(e ** 2)

    l2_norm = h * np.sqrt(l2_norm_squared)

    if l2_norm > 1000:
        return np.format_float_scientific(l2_norm, precision=3)
    else:
        return round(l2_norm, 4)


h = 0.01
lamb = [0.5, 0.8, 1, 2]

for i, f in enumerate([f1, f2]):
    for L in lamb:
        # we are now going to *attempt* to solve all the schemes at the same time for each
        # lambda value:

        k = L * h

        # create answer arrays:

        # we are just solving for t=2 and the total range of [-1,1]
        FTBS_ans = np.zeros((int(2 / k) + 1,
                             int(2 / h)))
        LaxF_ans = np.zeros_like(FTBS_ans)
        LeapFrog_ans = np.zeros_like(FTBS_ans)

        # create initial data. this will be at the 'top' of the array
        for j in range(FTBS_ans.shape[1]):
            FTBS_ans[0, j] = f(j * h - 1)
            LaxF_ans[0, j] = f(j * h - 1)
            LeapFrog_ans[0, j] = f(j * h - 1)

        # Loop over time:
        for s in range(1, FTBS_ans.shape[0]):
            current_time = s * k

            # Loop over space:
            for j in range(FTBS_ans.shape[1]):
                if j == 0:  # Handles the case of needing one point before
                    FTBS_ans[s, j] = FTBS_one_step(L, FTBS_ans[s - 1, -1],
                                                   FTBS_ans[s - 1, j])
                    LaxF_ans[s, j] = LaxF_one_step(L, LaxF_ans[s - 1, -1],
                                                   LaxF_ans[s - 1, j + 1])
                    if current_time == k:
                        LeapFrog_ans[s, j] = FTBS_one_step(L, FTBS_ans[s - 1, -1],
                                                           FTBS_ans[s - 1, j])  # Use FTBS
                    else:
                        LeapFrog_ans[s, j] = LeapFrog_one_step(L, LeapFrog_ans[s - 1, -1],
                                                               LeapFrog_ans[s - 2, j],
                                                               LeapFrog_ans[s - 1, j + 1])

                elif j == FTBS_ans.shape[
                    1] - 1:  # Handles the case of needing one extra point beyond
                    FTBS_ans[s, j] = FTBS_one_step(L, FTBS_ans[s - 1, j - 1],
                                                   FTBS_ans[s - 1, j])
                    LaxF_ans[s, j] = LaxF_one_step(L, LaxF_ans[s - 1, j - 1],
                                                   LaxF_ans[s - 1, 0])
                    if current_time != k:  # this handles only when LeapFrom can be used
                        LeapFrog_ans[s, j] = LeapFrog_one_step(L,
                                                               LeapFrog_ans[s - 1, j - 1],
                                                               LeapFrog_ans[s - 2, j],
                                                               LeapFrog_ans[s - 1, 0])

                else:
                    FTBS_ans[s, j] = FTBS_one_step(L, FTBS_ans[s - 1, j - 1],
                                                   FTBS_ans[s - 1, j])
                    LaxF_ans[s, j] = LaxF_one_step(L, LaxF_ans[s - 1, j - 1],
                                                   LaxF_ans[s - 1, j + 1])
                    if current_time == k:
                        LeapFrog_ans[s, j] = FTBS_one_step(L, FTBS_ans[s - 1, j - 1],
                                                           FTBS_ans[s - 1, j])
                    else:
                        LeapFrog_ans[s, j] = LeapFrog_one_step(L,
                                                               LeapFrog_ans[s - 1, j - 1],
                                                               LeapFrog_ans[s - 2, j],
                                                               LeapFrog_ans[s - 1, j + 1])

        # Plot figures for current Lambda and initial condition. Need to export each
        # figure once done plotting
        x_vals = np.linspace(-1, 1, int(2 / h))
        u_exact = np.array([calc_u_exact(f, x, 2) for x in x_vals])

        L2 = L2norm(FTBS_ans[-1, :] - u_exact, h)
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('u(t=2,x)')
        plt.title(f'FTBS: $\lambda = {L},f_{i + 1}$\n$L2={L2}$')
        sns.lineplot(x=x_vals, y=FTBS_ans[-1, :], label=r'$v_i^n$', markers=True)
        sns.lineplot(x=x_vals, y=u_exact, label=r'$u_{exact}$')
        plt.legend()
        plt.savefig(fr'figures/FTBS/FTBS_lambda={L},f{i + 1}.png')
        plt.close()

        L2 = L2norm(LaxF_ans[-1, :] - u_exact, h)
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('u(t=2,x)')
        sns.lineplot(x=x_vals, y=LaxF_ans[-1, :], label=r'$v_i^n$', markers=True)
        sns.lineplot(x=x_vals, y=u_exact, label=r'$u_{exact}$')
        plt.title(f'LaxFriedrichs: $\lambda = {L},f_{i + 1}$\n$L2={L2}$')
        plt.legend()
        plt.savefig(fr'figures/LaxFriedrichs/LaxFriedrichs_lambda={L},f{i + 1}.png')
        plt.close()

        L2 = L2norm(LeapFrog_ans[-1, :] - u_exact, h)
        plt.figure()
        plt.xlabel('x')
        plt.ylabel('u(t=2,x)')
        sns.lineplot(x=x_vals, y=LeapFrog_ans[-1, :], label=r'$v_i^n$', markers=True)
        sns.lineplot(x=x_vals, y=u_exact, label=r'$u_{exact}$')
        plt.title(f'LeapFrog: $\lambda = {L}, f_{i + 1}$\n$L2={L2}$')
        plt.legend()
        plt.savefig(fr'figures/LeapFrog/LeapFrog_lambda={L},f{i + 1}.png')
        plt.close()
