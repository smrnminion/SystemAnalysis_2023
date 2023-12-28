import json
import numpy as np

# Переименованные функции и изменённые внутренние операции

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def flatten_expert_ranking(ranking):
    flattened_ranking = []
    indices = []
    index = 0
    for group in ranking:
        if not isinstance(group, list):
            group = [group]
        for item in group:
            indices.append(index)
            flattened_ranking.append(item)
        index += 1
    return flattened_ranking, indices

def create_preference_matrix(expert_ranking):
    flat_ranking, rank_indices = flatten_expert_ranking(expert_ranking)
    size = len(flat_ranking)
    pref_matrix = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):
            if rank_indices[flat_ranking.index(i + 1)] <= rank_indices[flat_ranking.index(j + 1)]:
                pref_matrix[i][j] = 1
    return pref_matrix.tolist()

def find_disagreements(matrix1, matrix2):
    np_matrix1 = np.array(matrix1)
    np_matrix2 = np.array(matrix2)

    combined_kernel = np.logical_or(np.multiply(np_matrix1, np_matrix2), 
                                    np.multiply(np_matrix1.T, np_matrix2.T))
    disagreements = []

    for i in range(len(combined_kernel)):
        for j in range(len(combined_kernel[i])):
            if combined_kernel[i][j] == 0:
                pair = sorted([i + 1, j + 1])
                if pair not in disagreements:
                    disagreements.append(pair)

    consolidated_disagreements = []
    for pair in disagreements:
        found = False
        for existing_pair in consolidated_disagreements:
            if set(pair).intersection(existing_pair):
                existing_pair.update(pair)
                found = True
                break
        if not found:
            consolidated_disagreements.append(set(pair))

    return [list(group) for group in consolidated_disagreements]

def merge_expert_opinions(expert1, expert2, conflict_zones):
    merged_opinion = []
    for group1 in expert1:
        group1 = group1 if isinstance(group1, list) else [group1]
        for group2 in expert2:
            group2 = group2 if isinstance(group2, list) else [group2]
            intersection = set(group1).intersection(group2)
            for item in group1:
                in_conflict_zone, zone = item_in_conflict_zone(item, conflict_zones)
                if in_conflict_zone:
                    if zone not in merged_opinion:
                        merged_opinion.append(zone)
                    break
            if intersection and not in_conflict_zone:
                merged_opinion.append(list(intersection) if len(intersection) > 1 else intersection.pop())

    return merged_opinion

def item_in_conflict_zone(item, zones):
    for zone in zones:
        if item in zone:
            return True, zone
    return False, []

def analyze_expert_rankings():
    expert_A = [1,[2,3],4,[5,6,7],8,9,10]
    expert_B = [[1,2],[3,4,5,],6,7,9,[8,10]]
    matrix_A = create_preference_matrix(expert_A)
    matrix_B = create_preference_matrix(expert_B)
    conflicts_AB = find_disagreements(matrix_A, matrix_B)
    merged_AB = merge_expert_opinions(expert_A, expert_B, conflicts_AB)
    print(merged_AB)



if __name__ == '__main__':
    analyze_expert_rankings()
