package dev.mandevilla;

import java.util.ArrayDeque;
import java.util.Deque;

public class FilasInteger {
    public static void main(String[] args) {
        // Criando fila
        Deque<Integer> fila = new ArrayDeque<>();

        // Inserindo na fila
        fila.offer(17);
        fila.offer(1);
        fila.offer(2005);

        // Exibição
        System.out.println("Imprimindo fila: " + fila);

        // Exibir o valor do início da lista, sem remover
        int primeiroItem = fila.peek();
        System.out.println("\nPrimeiro item: " + primeiroItem);

        // Retorna e remove o elemento que está no início da lista
        int removerPrimeiro = fila.poll();
        System.out.println("\nElemento obtido e removido: " + removerPrimeiro);
        System.out.println("Imprimindo fila: " + fila);

        // Limpar a fila
        fila.clear();

        // Verifica se está vazia
        boolean filaVazia = fila.isEmpty();
        System.out.println("\nFila esvaziada: " + filaVazia);
    }
}