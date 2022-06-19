#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    # Write your code here
    if len(brackets) % 2 != 0:
        # Se a sequência é ímpar, já sabemos que não está balanceada.
        return "NO"

    brackets_pairs = ['()', '[]', '{}']
    aux = brackets

    # Definindo a closure com o algoritmo
    def check_balance():
        nonlocal brackets_pairs, aux

        if len(aux) == 0:
            # Condição de parada 1: Se a lista está vazia, ela está balanceada.
            return "YES"

        elif not any(pair in aux for pair in brackets_pairs):
            # Condição de parada 2: Se ela não está vazia,
            # e não tem nenhum par de brackets balanceado, ela não está balanceada.
            return "NO"

        else:
            # A lista não está vazia e possui pares de brackets balanceados.
            # Então removemos eles e realizamos uma recursão.
            for pair in brackets_pairs:
                aux = aux.replace(pair, '')
            return check_balance()

    return check_balance()


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
