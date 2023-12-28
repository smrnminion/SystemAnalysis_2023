import csv
from io import StringIO

def parse_csv_to_graph(csv_string):
    graph = {}
    reader = csv.reader(StringIO(csv_string))
    for row in reader:
        if row[0] not in graph:
            graph[row[0]] = row[1:]
        else:
            graph[row[0]] += row[1:]
    return graph

def calculate_matrix(graph):
    nodes = sorted(set(graph.keys()).union(*graph.values()))
    matrix = [[0 for _ in nodes] for _ in nodes]

    for node, edges in graph.items():
        for edge in edges:
            matrix[int(node) - 1][int(edge) - 1] = 1
            matrix[int(edge) - 1][int(node) - 1] = -1
    return matrix

def task(csv_string):
    graph = parse_csv_to_graph(csv_string)
    matrix = calculate_matrix(graph)

    result = []
    for i in range(len(matrix)):
        outgoing = sum(1 for val in matrix[i] if val == 1)
        incoming = sum(1 for val in matrix[i] if val == -1)

        second_level_outgoing = 0
        second_level_incoming = 0
        cross_links = 0

        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                second_level_outgoing += sum(1 for val in matrix[j] if val == 1)
                for k in range(len(matrix)):
                    if matrix[j][k] == -1 and k != i:
                        cross_links += 1

            if matrix[i][j] == -1:
                second_level_incoming += sum(1 for val in matrix[j] if val == -1)

        result.append([outgoing, incoming, second_level_outgoing, second_level_incoming, cross_links])

    output = StringIO()
    csv_writer = csv.writer(output, delimiter=',', lineterminator='\n')
    csv_writer.writerows(result)
    return output.getvalue()

input_str = '1,2\n2,3\n2,4\n3,5\n3,6'
output_csv = task(input_str)
print(output_csv)
