import numpy as np

def calculate_kendall_tau(expert_opinions):
    opinion_matrix = [[0 for _ in range(len(expert_opinions))] for _ in range(len(expert_opinions[0]))]
    eta_matrix = [[len(expert_opinions[0]) - i for _ in range(len(expert_opinions))] for i in range(len(expert_opinions[0]))]
    ordered_elements = sorted(expert_opinions[0])

    for expert_index in range(len(expert_opinions)):
        for opinion_index in range(len(expert_opinions[expert_index])):
            item = ordered_elements[opinion_index]
            opinion_matrix[opinion_index][expert_index] = len(expert_opinions[expert_index]) - expert_opinions[expert_index].index(item)

    opinion_matrix = np.array(opinion_matrix)
    eta_matrix = np.array(eta_matrix)

    dispersion_eta = ((eta_matrix.sum(axis=-1) - eta_matrix.sum(axis=-1).mean())**2).sum() / (len(expert_opinions[0]) - 1)
    dispersion_opinions = ((opinion_matrix.sum(axis=-1) - opinion_matrix.sum(axis=-1).mean())**2).sum() / (len(expert_opinions[0]) - 1)

    print(dispersion_opinions)
    print(dispersion_eta)

    return dispersion_opinions / dispersion_eta

def task():
    A = ["O1", "O2", "O3"]
    B = ["O1", "O3", "O2"]
    C = ["O1", "O3", "O2"]

    expert_views = [A, B, C]

    result = calculate_kendall_tau(expert_views)
    return result

if __name__ == "__main__":
    print(task())
