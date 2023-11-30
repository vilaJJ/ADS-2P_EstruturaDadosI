package dev.mandevilla;

// Bibliotecas utilizadas
import java.util.Stack;

public class PilhasInteger {
    public static void main(String[] args) {
        System.out.println("-------------------------------------------------------------------------");

        // Criando pilha
        Stack<Integer> pilha = new Stack<>();

        // Adicionando itens na pilha
        pilha.push(10);
        pilha.push(15);
        pilha.push(20);

        // Exibindo a pilha
        System.out.println("Pilha atual:\n\t-> " + pilha);

        System.out.println("-------------------------------------------------------------------------");

        // Retorna o elemento no topo sem remover da pilha
        int valorTopo = pilha.peek();
        System.out.println("Elemento no topo da pilha:\n\t-> " + valorTopo);

        System.out.println("Pilha atual:\n\t-> " + pilha);

        System.out.println("-------------------------------------------------------------------------");

        // Retorna e remove o elemento do topo da pilha
        valorTopo = pilha.pop();
        System.out.println("Elemento no topo da pilha:\n\t-> " + valorTopo);

        System.out.println("Pilha atual:\n\t-> " + pilha);

        System.out.println("-------------------------------------------------------------------------");

        // Tamanho da pilha
        int tamanhoPilha = pilha.size();
        System.out.println("Tamanho da pilha:\n\t-> " + tamanhoPilha);

        System.out.println("-------------------------------------------------------------------------");

        // Limpa a pilha
        pilha.clear();
        System.out.println("Limpando pilha...");

        System.out.println("Pilha atual:\n\t-> " + pilha);

        System.out.println("-------------------------------------------------------------------------");

        // Verifica se a pilha não possuí elementos
        boolean pilhaVazia = pilha.isEmpty();
        System.out.println("Pilha vazia:\n\t-> " + pilhaVazia);

        System.out.println("-------------------------------------------------------------------------");
    }
}