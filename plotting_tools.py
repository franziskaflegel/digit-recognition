import matplotlib.pyplot as plt
import numpy as np

def display_plot(x_space, cv_scores, cv_scores_std, param_name='Hyperparameter'):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(x_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel(param_name)
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([x_space[0], x_space[-1]])
    ax.set_xscale('log')
    plt.show()