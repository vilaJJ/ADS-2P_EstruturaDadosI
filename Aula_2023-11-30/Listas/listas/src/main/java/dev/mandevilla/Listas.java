package dev.mandevilla;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Listas {
    public static void main(String[] args) {
        System.out.println("--------------------------------------------------------------\n");
        
        List<String> cores = new ArrayList<>();

        // Adicionando valores na lista
        adicionarValor(cores, "Vermelho");
        adicionarValor(cores, "Azul");
        adicionarValor(cores, "Amarelo");
        adicionarValor(cores, "Roxo");
        adicionarValor(cores, "Rosa");

        // Exibindo a lista
        exibirLista(cores);

        // Substituindo valor
        substituirValor(cores, 2, "Laranja");

        // Exibindo a lista
        exibirLista(cores);

        // Exibindo valor a partir da posição passada
        exibirValor(cores, 3);

        // Removendo valor da lista
        removerValor(cores, 0);
        removerValor(cores, "Azul");

        // Exibindo a lista
        exibirLista(cores);

        // Verifica se existe o valor na lista
        exibirContemValor(cores, "Vermelho");
        exibirContemValor(cores, "Roxo");

        // Exibindo a lista de forma crescente e decrescente
        exibirLista(cores, true);
        exibirLista(cores, false);

        // Verifica se a lista está vazia
        exibirEstaVazia(cores);

        // Obtém o tamanho (quantidade de elementos) da lista
        exibirTamanhoLista(cores);

        // Limpa todos os valores da lista
        limparLista(cores);

        // Mostrando resultado final
        exibirLista(cores);
        exibirTamanhoLista(cores);
        exibirEstaVazia(cores);
    }
    
    private static void adicionarValor(List<String> lista, String valor) {
        // Adiciona o valor na última posição da lista.
        lista.add(valor);
    }

    private static void substituirValor(List<String> lista, int posicao, String valor) {
        // Substitui o valor na posição desejada
        lista.set(posicao, valor);
    }

    private static void exibirValor(List<String> lista, int posicao) {
        // Exibe o valor baseado no índice passado
        String valor = lista.get(posicao);

        System.out.println(
            String.format(
                "Valor da posição [%d]: %s",
                posicao,
                valor
            )
        );
    }

    private static void removerValor(List<String> lista, int posicao) {
        // Remove um valor da lista, baseado na sua posição
        lista.remove(posicao);
    }

    private static void removerValor(List<String> lista, String valor) {
        // Remove a primeira ocorrência encotrada do valor passado
        lista.remove(valor);
    }

    private static void exibirContemValor(List<String> lista, String valor) {
        // Verdadeiro caso o parâmetro passado exista na lista
        boolean contemValor = lista.contains(valor);

        System.out.println(
            String.format(
                "O valor '%s' %s na Lista.",
                valor,
                contemValor ? "existe" : "não existe"
            )
        );
    }

    private static void exibirLista(List<String> lista) {
        // Imprime a lista completa
        System.out.println("Exibindo a Lista: " + lista);
    }

    private static void exibirLista(List<String> lista, boolean isAsc) {
        if (isAsc) {
            // Ordena a lista em ordem crescente
            Collections.sort(lista);
        }
        else {
            // Ordena a lista em ordem decrescente
            Collections.reverse(lista);
        }
        
        System.out.println(
            String.format(
                "Lista em ordem %s: " + lista,
                isAsc ? "crescente" : "decrescente"
            )
        );
    }

    private static void exibirEstaVazia(List<String> lista) {
        // Verdadeiro caso a lista esteja vazia.
        boolean estaVazia = lista.isEmpty();

        System.out.println(
            String.format(
                "A Lista está vazia? %s.",
                estaVazia ? "Sim" : "Não"
            )
        );
    }
    
    private static void exibirTamanhoLista(List<String> lista) {
        // Retorna a quantidade de elementos da lista
        int tamanho = lista.size();

        System.out.println(
            String.format(
                "Tamanho da Lista: %d %s.",
                tamanho,
                tamanho == 1 ? "item" : "itens"
            )
        );
    }
    
    private static void limparLista(List<String> lista) {
        // Apaga todos os valores da lista, deixando-a vazia
        lista.clear();
    }
}