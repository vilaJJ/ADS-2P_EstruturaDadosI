package dev.mandevilla;

import java.util.Deque;
import java.util.LinkedList;

public class Filas {
    public static void main(String[] args) {
        System.out.println("--------------------------------------------------------------\n");

        Deque<String> filaAlmoco = new LinkedList<>();

        // Adiciona o elemento na fila
        adicionarElemento(filaAlmoco, "Juan Felipe");
        adicionarElemento(filaAlmoco, "Allan Batista");
        adicionarElemento(filaAlmoco, "Ayalon Emanuel");
        adicionarElemento(filaAlmoco, "Victor Ferraz");
        adicionarElemento(filaAlmoco, "Samylla Marinho");
        adicionarElemento(filaAlmoco, "Beatriz Coelho");

        // Exibe a fila
        exibirFila(filaAlmoco);

        // Obtém e exibe o primeiro elemento da fila
        exibirPrimeiroFila(filaAlmoco);

        // Obtém, exibe e remove o primeiro elemento da fila
        removerPrimeiroElemento(filaAlmoco);

        // Obtém e exibe se a fila está vazia
        exibirEstaVazia(filaAlmoco);

        // Obtém e exibe a quantidade de elementos da fila
        exibirQntdeElementosFila(filaAlmoco);

        // Limpa os valores da fila, remove todos os elementos
        limparFila(filaAlmoco);

        // Resultado final
        exibirFila(filaAlmoco);
        exibirQntdeElementosFila(filaAlmoco);
        exibirEstaVazia(filaAlmoco);
    }

    private static void adicionarElemento(Deque<String> fila, String elemento) {
        // Adiciona o elemento no final da fila
        fila.offer(elemento);
    }

    private static void exibirPrimeiroFila(Deque<String> fila) {
        // Obtém o primeiro elemento da fila, sem removê-lo.
        String elemento = fila.peek();

        System.out.println(
            String.format(
                "Próximo elemento da Fila: %s.",
                elemento
            )
        );
    }

    private static void removerPrimeiroElemento(Deque<String> fila) {
        // Obtém e remove o primeiro elemento da fila.
        String elemento = fila.poll();

        System.out.println(
            String.format(
                "Elemento '%s' removido da Fila.",
                elemento
            )
        );
    }

    private static void exibirEstaVazia(Deque<String> fila) {
        // Verifica se a fila está vazia (sem elementos)
        boolean estaVazia = fila.isEmpty();

        System.out.println(
            String.format(
                "A fila está vazia? %s.",
                estaVazia ? "Sim" : "Não"
            )
        );
    }

    private static void exibirQntdeElementosFila(Deque<String> fila) {
        // Obtém a quantidade de elementos da fila
        int qntdeElementos = fila.size();

        System.out.println(
            String.format(
                "Quantidade de Elementos na Fila: %d %s.",
                qntdeElementos,
                qntdeElementos == 1 ? "elemento" : "elementos"
            )
        );
    }

    private static void limparFila(Deque<String> fila) {
        // Limpa os elementos da fila, deixando-a vazia
        fila.clear();
    }

    private static void exibirFila(Deque<String> fila) {
        // Imprime a fila e todos os seus elementos
        System.out.println("Exibindo a Fila: " + fila);
    }
}