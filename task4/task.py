import math

def calculate_matrices():
    sum_values = []
    product_values = []

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            sum_of_dice = dice1 + dice2
            product_of_dice = dice1 * dice2
            sum_values.append(sum_of_dice)
            product_values.append(product_of_dice)
    
    sum_values = list(set(sum_values))
    product_values = list(set(product_values))
    
    ab_matrix = [[0 for _ in range(len(product_values))] for _ in range(len(sum_values))]

    for dice1 in range(1, 7):
        for dice2 in range(1, 7):
            sum_of_dice = dice1 + dice2
            product_of_dice = dice1 * dice2
            ab_matrix[sum_values.index(sum_of_dice)][product_values.index(product_of_dice)] += 1

    return ab_matrix

def calculate_probabilities(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] /= 36
    
    return matrix

def calculate_entropy(matrix, axis='row'):
    total_entropy = 0.0
    
    if axis == 'row':
        for row in matrix:
            row_entropy = sum(row)
            if row_entropy > 0:
                total_entropy += -1 * row_entropy * math.log2(row_entropy)
    
    elif axis == 'column':
        for column in range(len(matrix[0])):
            column_entropy = sum(matrix[row][column] for row in range(len(matrix)))
            if column_entropy > 0:
                total_entropy += -1 * column_entropy * math.log2(column_entropy)
    
    return total_entropy

def calculate_joint_entropy(matrix):
    joint_entropy = 0.0
    for row in matrix:
        for value in row:
            if value > 0:
                joint_entropy += -1 * value * math.log2(value)

    return joint_entropy

def calculate_conditional_entropy(matrix, prob_matrix):
    conditional_prob_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    for row in range(len(matrix)):
        row_sum = sum(matrix[row])
        for column in range(len(matrix[row])):
            conditional_prob_matrix[row][column] = matrix[row][column] / row_sum if row_sum > 0 else 0

    conditional_entropy = 0.0
    for row in range(len(conditional_prob_matrix)):
        row_entropy = sum(-value * math.log2(value) for value in conditional_prob_matrix[row] if value > 0)
        conditional_entropy += row_entropy * sum(prob_matrix[row])

    return conditional_entropy

def task():
    matrix = calculate_matrices()
    prob_matrix = calculate_probabilities(matrix)
    
    entropy_sum = calculate_entropy(prob_matrix, axis='row')
    entropy_product = calculate_entropy(prob_matrix, axis='column')
    joint_entropy = calculate_joint_entropy(prob_matrix)
    conditional_entropy = calculate_conditional_entropy(matrix, prob_matrix)

    mutual_information = entropy_product - conditional_entropy

    return entropy_sum, entropy_product, joint_entropy, conditional_entropy, mutual_information

if __name__ == '__main__':
    print(task())
