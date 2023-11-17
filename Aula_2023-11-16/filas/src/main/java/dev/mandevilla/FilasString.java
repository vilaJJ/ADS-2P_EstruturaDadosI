package dev.mandevilla;

// Bibliotecas necessárias
import java.util.ArrayDeque;
import java.util.Deque;

public class FilasString {
    public static void main(String[] args) {
        // Criando fila
        Deque<String> filaAlmoco = new ArrayDeque<>();

        System.out.println("-------------------------------------------------------------------------");

        // Inserindo na fila
        filaAlmoco.offer("Bárbara Ohana");
        filaAlmoco.offer("Juan Felipe");
        filaAlmoco.offer("Maria Eduarda");
        filaAlmoco.offer("Sara Ghabrielly");

        // Exibição
        System.out.println("Exibindo lista:");
        for (String nome : filaAlmoco) {
            System.out.println("\t-> " + nome);
        }

        System.out.println("-------------------------------------------------------------------------");

        // Exibir o valor do início da lista, sem remover
        String proximoChamar = filaAlmoco.peek();
        System.out.println("Próximo da fila:\n\t-> " + proximoChamar);

        // Retorna e remove o elemento que está no início da lista
        String proximoChamado = filaAlmoco.poll();
        System.out.println("Chamando:\n\t-> " + proximoChamado);

        System.out.println("-------------------------------------------------------------------------");

        // Exibir o valor do início da lista, sem remover
        proximoChamar = filaAlmoco.peek();
        System.out.println("Próximo da fila:\n\t-> " + proximoChamar);

        // Retorna e remove o elemento que está no início da lista
        proximoChamado = filaAlmoco.poll();
        System.out.println("Chamando:\n\t-> " + proximoChamado);

        System.out.println("-------------------------------------------------------------------------");

        // Tamanho da fila
        System.out.println("Fila atual:\n\t-> " + filaAlmoco);

        int tamanhoFila = filaAlmoco.size();
        System.out.println(
            String.format(
                "Tamanho da fila:\n\t -> %d pessoas",
                tamanhoFila
            )
        );

        System.out.println("-------------------------------------------------------------------------");
        
        // Limpar a fila
        filaAlmoco.clear();

        // Verifica se está vazia
        boolean filaVazia = filaAlmoco.isEmpty();
        System.out.println("A fila contém elementos:\n\t-> " + filaVazia);
        
        System.out.println("-------------------------------------------------------------------------");
    }
}
