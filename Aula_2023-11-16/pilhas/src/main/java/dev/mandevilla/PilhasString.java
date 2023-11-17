package dev.mandevilla;

// Biblioteca de pilhas
import java.util.Stack;

public class PilhasString {
    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------------------");

        // Criando pilha
        Stack<String> pilhaLivros = new Stack<>();

        // Adicionando itens na pilha
        pilhaLivros.push("O Diário de Annie Frank");
        pilhaLivros.push("A ética protestante e o \"espiríto\" do capitalismo");
        pilhaLivros.push("O que aconteceu com Annie?");
        pilhaLivros.push("Jogos Vorazes");

        // Exibindo a pilha
        System.out.println("Exibindo a pilha:");
        for (String livro : pilhaLivros) {
            System.out.println("\t-> " + livro);
        }

        System.out.println("-------------------------------------------------------------------------");

        // Retorna o elemento no topo sem remover da pilha
        String livroTopo = pilhaLivros.peek();
        System.out.println("Livro no topo da pilha:\n\t-> " + livroTopo);

        System.out.println("-------------------------------------------------------------------------");

        // Retorna e remove o elemento do topo da pilha
        livroTopo = pilhaLivros.pop();
        System.out.println("Livro a ser removido do topo:\n\t-> " + livroTopo);

        System.out.println("-------------------------------------------------------------------------");

        // Tamanho da pilha
        int tamanhoPilha = pilhaLivros.size();

        System.out.println(
            String.format(
                "Quantidade de livros na pilha:\n\t-> %d livros.",
                tamanhoPilha
            )
        );

        System.out.println("-------------------------------------------------------------------------");

        // Limpa a pilha
        pilhaLivros.clear();

        System.out.println("Limpando a pilha...");

        System.out.println("-------------------------------------------------------------------------");

        // Verifica se a pilha não possuí elementos
        boolean pilhaVazia = pilhaLivros.isEmpty();

        System.out.println("A pilha está vazia:\n\t-> " + pilhaVazia);
        System.out.println("-------------------------------------------------------------------------");
    }
}
