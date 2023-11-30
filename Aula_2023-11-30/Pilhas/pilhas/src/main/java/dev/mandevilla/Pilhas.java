package dev.mandevilla;

import java.util.Stack;

public class Pilhas {
    public static void main(String[] args) {
        System.out.println("--------------------------------------------------------------\n");
        
        Stack<String> pilhaFilmes = new Stack<>();

        // Adicionando elementos na pilha
        adicionarElemento(pilhaFilmes, "O menu");
        adicionarElemento(pilhaFilmes, "Pearl");
        adicionarElemento(pilhaFilmes, "Corra");
        adicionarElemento(pilhaFilmes, "IT a coisa");
        adicionarElemento(pilhaFilmes, "Batman");

        // Exibir pilha completa
        exibirPilha(pilhaFilmes);

        // Exibe elemento do topo da pilka
        exibirElementoTopo(pilhaFilmes);

        // Exibe e remove elemento do topo da pilka
        removerElementoTopo(pilhaFilmes);

        // Verifica se a pilha está vazia
        verificarPilhaVazia(pilhaFilmes);

        // Obtém e exibe a quantidade de elementos na pilha
        qntdeElementosPilha(pilhaFilmes);

        // Exclui todos os elementos da pilha
        excluirTodosElementos(pilhaFilmes);
        
        // Mostrando resultado final
        exibirPilha(pilhaFilmes);
        qntdeElementosPilha(pilhaFilmes);
        verificarPilhaVazia(pilhaFilmes);
    }
    
    private static void adicionarElemento(Stack<String> pilha, String elemento){
        // Adiciona elementos ao topo da pilha 
        pilha.push(elemento);
    }

    private static void exibirElementoTopo(Stack<String> pilha){
        // Retorna o elemento no topo da pilha sem removê-lo
        String elemento = pilha.peek();

        System.out.println(
            String.format(
                "Elemento do topo da pilha: %s.",
                elemento
            )
        );

    }

    private static void removerElementoTopo(Stack<String> pilha){
        // Retorna e remove o elemento no topo da pilha
        String elemento = pilha.pop();

        System.out.println(
            String.format(
                "Elemento removido da pilha: %s.",
                elemento
            )
        );
    }

    private static void verificarPilhaVazia(Stack<String> pilha){
        // Retorna se a pilha está vazia ou nao
        boolean estaVazia = pilha.isEmpty();

        System.out.println(
            String.format(
                "A lista está vazia? %s.",
                estaVazia ? "Sim" : "Não"
            )
        );
    }

    private static void qntdeElementosPilha(Stack<String> pilha){
        // Retorna o tamanho da pilha
        int tamanhoPilha = pilha.size();

        System.out.println(
            String.format(
                "Quantidade de elementos na pilha: %d %s.",
                tamanhoPilha,
                tamanhoPilha==1 ? "elemento" : "elementos"
            )
        );
    }

    private static void excluirTodosElementos(Stack<String> pilha){
        // Exclui todos os elementos da pilha
        pilha.clear();
    }

	private static void exibirPilha(Stack<String> pilha){
        // Exibe os elementos pilha
        System.out.println(
            "Elementos da pilha: "+pilha
        );
    }		
}